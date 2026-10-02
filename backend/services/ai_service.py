from openai import AsyncOpenAI
import json
from typing import List, Dict, Any
from config import settings
from models.api_models import RoadmapStep, ChatMessage

# Initialize the OpenAI client only if the key is present
client = None
if settings.openai_api_key:
    client = AsyncOpenAI(api_key=settings.openai_api_key)

async def generate_roadmap(target_role: str, missing_skills: List[str]) -> List[RoadmapStep]:
    """Generates a learning roadmap using OpenAI based on missing skills."""
    if not client:
        # Fallback if no API key is provided
        return [
            RoadmapStep(
                title="API Key Missing",
                description="Please configure OPENAI_API_KEY to generate a real roadmap.",
                resources=["Configure .env file"],
                estimated_time="10 mins"
            )
        ]
        
    prompt = f"""
    You are an expert career coach. Create a learning roadmap for someone trying to become a {target_role}.
    They are missing the following skills: {', '.join(missing_skills)}.
    
    Provide the response as a JSON array of objects, where each object represents a step in the roadmap.
    Each object must have the following keys:
    - title: (string) The title of the step/skill to learn
    - description: (string) A brief description of what to learn
    - resources: (array of strings) 2-3 links or names of resources (courses, books, docs)
    - estimated_time: (string) Estimated time to complete (e.g., "2 weeks")
    
    Ensure the output is ONLY valid JSON.
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo", # Use a cheaper model for now, can upgrade to gpt-4o if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" } # Note: needs gpt-3.5-turbo-1106 or newer
        )
        
        # Some models return the array directly, others wrap it in an object.
        # Handling the generic JSON response format.
        content = response.choices[0].message.content
        
        try:
            data = json.loads(content)
            # If wrapped in an object like {"steps": [...]}, extract it
            if isinstance(data, dict):
                for key in data.keys():
                    if isinstance(data[key], list):
                        data = data[key]
                        break
            
            steps = []
            for item in data:
                steps.append(RoadmapStep(**item))
            return steps
        except json.JSONDecodeError:
            print("Failed to decode JSON from OpenAI response:", content)
            return []
            
    except Exception as e:
        print(f"Error generating roadmap: {e}")
        return []

async def get_chat_response(messages: List[ChatMessage], context: Dict[str, Any] = None) -> str:
    """Handles chatbot interactions with OpenAI."""
    if not client:
        return "Please configure the OPENAI_API_KEY in the .env file to use the chatbot."

    system_message = {
        "role": "system", 
        "content": "You are an AI Career Gap Analyzer Assistant. Your goal is to help users understand their skill gaps and guide them on their learning journey."
    }
    
    if context:
        context_str = json.dumps(context, indent=2)
        system_message["content"] += f"\n\nHere is the context of the user's current analysis:\n{context_str}"

    openai_messages = [system_message]
    for msg in messages:
        openai_messages.append({"role": msg.role, "content": msg.content})

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=openai_messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in chat service: {e}")
        return "I'm having trouble connecting right now. Please try again later."
