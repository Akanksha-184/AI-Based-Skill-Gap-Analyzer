# Predefined skills for common roles to check against

ROLE_SKILLS = {
    "software engineer": [
        "python", "java", "c++", "javascript", "typescript", "react", "node.js",
        "sql", "nosql", "git", "docker", "kubernetes", "aws", "gcp", "azure",
        "data structures", "algorithms", "system design", "rest api", "graphql",
        "agile", "scrum", "ci/cd", "linux"
    ],
    "data scientist": [
        "python", "r", "sql", "machine learning", "deep learning", "statistics",
        "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy", "matplotlib",
        "seaborn", "data visualization", "nlp", "computer vision", "big data",
        "hadoop", "spark", "aws", "gcp"
    ],
    "product manager": [
        "agile", "scrum", "jira", "confluence", "product strategy", "roadmap",
        "user research", "a/b testing", "data analysis", "sql", "ui/ux",
        "stakeholder management", "market research", "go-to-market", "wireframing"
    ],
    "frontend developer": [
        "html", "css", "javascript", "typescript", "react", "vue", "angular",
        "next.js", "tailwind css", "sass", "webpack", "vite", "git", "responsive design",
        "web performance", "accessibility", "ui/ux", "jest", "cypress"
    ],
    "backend developer": [
        "python", "java", "node.js", "go", "ruby", "c#", "php", "sql", "postgresql",
        "mysql", "mongodb", "redis", "docker", "kubernetes", "aws", "rest api",
        "graphql", "microservices", "system design", "git", "ci/cd"
    ]
}

def get_skills_for_role(role: str) -> list[str]:
    """Returns a list of predefined skills for a given role."""
    return ROLE_SKILLS.get(role.lower(), [])
