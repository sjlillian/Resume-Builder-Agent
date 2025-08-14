import streamlit as st
from pathlib import Path
import json
from ai_engine.ollama_client import OllamaClient
from ai_engine.skills_extractor import SkillsExtractor

st.set_page_config(
    page_title="Resume Builder Agent",
    page_icon="📄",
    layout="wide"
)

# Initialize session state for storing selected skills
if 'selected_skills' not in st.session_state:
    st.session_state.selected_skills = {}

if 'extracted_skills' not in st.session_state:
    st.session_state.extracted_skills = None

# Initialize AI clients
ollama_client = OllamaClient()
skills_extractor = SkillsExtractor(ollama_client)

def main():
    st.title("Resume Builder Agent")
    st.write("Transform your resume with AI-powered job-specific customization")
    
    # File upload section
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Upload Your Resume")
            resume_file = st.file_uploader("Choose your resume file", type=["pdf", "docx"])
            
        with col2:
            st.subheader("Job Description")
            job_description = st.text_area("Paste the job description here")
    
    if job_description:
        if st.button("Analyze Job Description"):
            with st.spinner("Analyzing job description..."):
                # Extract skills from job description
                skills_data = skills_extractor.extract_skills(job_description)
                st.session_state.extracted_skills = skills_data

    # Display extracted skills if available
    if st.session_state.extracted_skills:
        st.markdown("## Skills from Job Description")
        st.markdown("Click on skills you have experience with to add them to your resume.")

        # Create columns for different skill categories
        tech_col, soft_col, domain_col = st.columns(3)

        with tech_col:
            st.markdown("### Technical Skills")
            for skill in st.session_state.extracted_skills.get('technical_skills', []):
                skill_key = f"tech_{skill['skill']}"
                if st.button(
                    f"🔵 {skill['skill']}",
                    help=f"Context: {skill['context']}",
                    key=skill_key,
                    disabled=skill_key in st.session_state.selected_skills
                ):
                    # Create a form for adding notes to the skill
                    with st.form(key=f"notes_form_{skill_key}"):
                        st.markdown(f"**Add notes for: {skill['skill']}**")
                        notes = st.text_area(
                            "Describe your experience with this skill",
                            help="Include specific examples and achievements"
                        )
                        submitted = st.form_submit_button("Add to Resume")
                        if submitted:
                            st.session_state.selected_skills[skill_key] = {
                                'skill': skill['skill'],
                                'category': 'technical',
                                'context': skill['context'],
                                'notes': notes
                            }
                            st.success(f"Added {skill['skill']} to your resume!")

        with soft_col:
            st.markdown("### Soft Skills")
            for skill in st.session_state.extracted_skills.get('soft_skills', []):
                skill_key = f"soft_{skill['skill']}"
                if st.button(
                    f"🟢 {skill['skill']}",
                    help=f"Context: {skill['context']}",
                    key=skill_key,
                    disabled=skill_key in st.session_state.selected_skills
                ):
                    with st.form(key=f"notes_form_{skill_key}"):
                        st.markdown(f"**Add notes for: {skill['skill']}**")
                        notes = st.text_area(
                            "Describe your experience with this skill",
                            help="Include specific examples and achievements"
                        )
                        submitted = st.form_submit_button("Add to Resume")
                        if submitted:
                            st.session_state.selected_skills[skill_key] = {
                                'skill': skill['skill'],
                                'category': 'soft',
                                'context': skill['context'],
                                'notes': notes
                            }
                            st.success(f"Added {skill['skill']} to your resume!")

        with domain_col:
            st.markdown("### Domain Knowledge")
            for skill in st.session_state.extracted_skills.get('domain_knowledge', []):
                skill_key = f"domain_{skill['skill']}"
                if st.button(
                    f"🟡 {skill['skill']}",
                    help=f"Context: {skill['context']}",
                    key=skill_key,
                    disabled=skill_key in st.session_state.selected_skills
                ):
                    with st.form(key=f"notes_form_{skill_key}"):
                        st.markdown(f"**Add notes for: {skill['skill']}**")
                        notes = st.text_area(
                            "Describe your experience with this skill",
                            help="Include specific examples and achievements"
                        )
                        submitted = st.form_submit_button("Add to Resume")
                        if submitted:
                            st.session_state.selected_skills[skill_key] = {
                                'skill': skill['skill'],
                                'category': 'domain',
                                'context': skill['context'],
                                'notes': notes
                            }
                            st.success(f"Added {skill['skill']} to your resume!")

        # Display selected skills
        if st.session_state.selected_skills:
            st.markdown("## Selected Skills")
            st.json(st.session_state.selected_skills)

            if st.button("Clear Selected Skills"):
                st.session_state.selected_skills = {}
                st.rerun()

if __name__ == "__main__":
    main()
