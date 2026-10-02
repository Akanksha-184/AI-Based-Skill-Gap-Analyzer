from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from config import settings

client = None
db = None

def get_db():
    """Returns the database instance."""
    global client, db
    if client is None:
        client = AsyncIOMotorClient(settings.mongodb_uri)
        db = client[settings.database_name]
    return db

async def save_gap_analysis(data: dict) -> str:
    """Saves gap analysis results to the database."""
    database = get_db()
    result = await database.analyses.insert_one(data)
    return str(result.inserted_id)

async def get_gap_analysis(analysis_id: str) -> dict:
    """Retrieves a gap analysis by ID."""
    database = get_db()
    try:
        document = await database.analyses.find_one({"_id": ObjectId(analysis_id)})
        if document:
            document["_id"] = str(document["_id"])
        return document
    except Exception:
        return None

async def save_roadmap(data: dict) -> str:
    """Saves a generated roadmap to the database."""
    database = get_db()
    result = await database.roadmaps.insert_one(data)
    return str(result.inserted_id)

async def get_roadmap(roadmap_id: str) -> dict:
    """Retrieves a roadmap by ID."""
    database = get_db()
    try:
        document = await database.roadmaps.find_one({"_id": ObjectId(roadmap_id)})
        if document:
            document["_id"] = str(document["_id"])
        return document
    except Exception:
        return None
