# Resume Builder Agent

A local-first resume customization tool that uses Ollama to help tailor resumes to specific job descriptions while optimizing for ATS compatibility.

## Prerequisites

Before running the application, you'll need to install and verify several components. Follow these steps in order:

### 1. Install Python 3.8 or higher

1. Download Python from the [official website](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"
3. Verify the installation by opening PowerShell and running:
```powershell
python --version
```
You should see something like `Python 3.8.x` or higher

### 2. Install Ollama

1. Download Ollama from [https://ollama.ai/download](https://ollama.ai/download)
2. Run the installer
3. Open PowerShell and verify the installation:
```powershell
ollama --version
```
4. Pull the Mistral model (we'll use this for AI processing):
```powershell
ollama pull mistral
```

### 3. Set Up the Resume Builder Agent

1. Clone or download this repository to your local machine
2. Open PowerShell and navigate to the project directory:
```powershell
cd "C:\Path\To\Resume-Builder-Agent"
```

3. Create and activate a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

4. Install the required dependencies:
```powershell
pip install -r requirements.txt
```

5. Verify Streamlit installation:
```powershell
streamlit --version
```

## Running the Application

1. Make sure Ollama is running:
   - Open PowerShell and run:
```powershell
ollama serve
```
   - Keep this window open

2. In a new PowerShell window, navigate to the project directory and activate the virtual environment:
```powershell
cd "C:\Path\To\Resume-Builder-Agent"
.\venv\Scripts\Activate
```

3. Start the application:
```powershell
streamlit run src/app.py
```

The application should automatically open in your default web browser. If it doesn't, you can manually visit:
```
http://localhost:8501
```

## Troubleshooting

### Python Issues
- If `python` command isn't recognized, try using `python3` instead
- Ensure Python is properly added to PATH during installation
- Try restarting PowerShell after installation

### Ollama Issues
- If Ollama isn't recognized, restart your computer after installation
- Ensure the Ollama service is running (`ollama serve`)
- If you get connection errors, make sure Ollama is running on port 11434

### Streamlit Issues
- If the web interface doesn't open automatically, try accessing it manually at `http://localhost:8501`
- If you get "Address already in use", try using a different port:
```powershell
streamlit run src/app.py --server.port 8502
```

## Current Features
- Upload resume (PDF/DOCX)
- Input job description
- Basic AI analysis using Ollama

## Coming Soon
- ATS optimization
- Skill matching
- Resume generation
- Custom formatting options

## Support
If you encounter any issues, please check:
1. All prerequisites are properly installed
2. Ollama service is running
3. You're using the virtual environment
4. All dependencies are installed

For further assistance, please open an issue on this repository.
