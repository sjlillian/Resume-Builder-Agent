import json
from typing import List, Dict, Any
from .ollama_client import OllamaClient

class SkillsExtractor:
    def __init__(self, ollama_client: OllamaClient):
        self.ollama = ollama_client

    def extract_skills(self, job_description: str) -> Dict[str, Any]:
        """
        Extract skills from job description using Ollama
        """
        system_prompt = """
        You are a skilled resume analyst. Analyze the job description and extract ALL skills mentioned.
        Group them into categories and return them in the following JSON format:
        {
            "technical_skills": [
                {"skill": "Python", "context": "for backend development"},
                {"skill": "React", "context": "building user interfaces"}
            ],
            "soft_skills": [
                {"skill": "Communication", "context": "working with cross-functional teams"},
                {"skill": "Leadership", "context": "leading small teams"}
            ],
            "domain_knowledge": [
                {"skill": "Agile methodologies", "context": "in software development"},
                {"skill": "CI/CD", "context": "implementing pipelines"}
            ]
        }
        Include the context where each skill was mentioned to help users understand how it's relevant.
        """
        
        response = self.ollama.generate(
            prompt=job_description,
            system=system_prompt,
            temperature=0.2
        )
        
        try:
            # Parse the JSON response
            skills_data = json.loads(response)
            return skills_data
        except json.JSONDecodeError:
            # Fallback in case of parsing error
            return {
                "technical_skills": [],
                "soft_skills": [],
                "domain_knowledge": []
            }
