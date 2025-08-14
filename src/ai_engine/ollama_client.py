import requests
from typing import Dict, Any, Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        
    def generate(self, 
                prompt: str, 
                model: str = "mistral:latest", 
                system: Optional[str] = None,
                temperature: float = 0.7) -> str:
        """
        Generate a response using Ollama
        
        Args:
            prompt (str): The user prompt
            model (str): The model to use
            system (str, optional): System prompt to set context
            temperature (float): Sampling temperature
            
        Returns:
            str: The generated response
        """
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
        }
        
        if system:
            payload["system"] = system
            
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            # Ollama streams responses, so we need to collect all parts
            full_response = ""
            for line in response.iter_lines():
                if line:
                    response_data = response.json()
                    if 'response' in response_data:
                        full_response += response_data['response']
            
            return full_response.strip()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to communicate with Ollama: {str(e)}")
            
    def analyze_job_description(self, text: str) -> Dict[str, Any]:
        """
        Analyze a job description to extract key requirements
        
        Args:
            text (str): The job description text
            
        Returns:
            Dict[str, Any]: Extracted information including required skills,
                           experience levels, etc.
        """
        system_prompt = """
        You are an expert resume consultant. Analyze the following job description
        and extract key information including:
        - Required technical skills
        - Required soft skills
        - Years of experience
        - Education requirements
        - Key responsibilities
        
        Format the response as a JSON object.
        """
        
        response = self.generate(
            prompt=text,
            system=system_prompt,
            temperature=0.2  # Lower temperature for more focused analysis
        )
        
        # TODO: Parse response into structured data
        return {"raw_analysis": response}
