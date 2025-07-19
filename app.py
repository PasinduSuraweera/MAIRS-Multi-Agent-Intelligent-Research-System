import streamlit as st
import os
import time
from dotenv import load_dotenv
from crew import research_crew

# Initialize environment variables
load_dotenv()

def verify_api_keys():
    """Validate presence of necessary API keys"""
    required_keys = ['SERPER_API_KEY', 'GROQ_API_KEY']
    absent_keys = [key for key in required_keys if not os.getenv(key)]
    return absent_keys

def execute_research_thread(research_assistant, subject, progress_area,
                          status_area):
    """Perform research in a background thread"""
    try:
        output = research_assistant.run_research(subject)
        st.session_state.study_output = output
        st.session_state.study_finished = True
        st.session_state.study_error = None
    except Exception as e:
        st.session_state.study_error = str(e)
        st.session_state.study_finished = True

def app():
    """Primary Streamlit application"""
    st.set_page_config(
        page_title="MAIRS: Multi-Agent Intelligent Research System",
        layout="wide"
    )

    st.title("MAIRS: Multi-Agent Intelligent Research System")
    st.markdown("*An AI Research Platform built with CrewAI*")

    # Set up session state
    if 'study_finished' not in st.session_state:
        st.session_state.study_finished = False
    if 'study_output' not in st.session_state:
        st.session_state.study_output = None
    if 'study_error' not in st.session_state:
        st.session_state.study_error = None

    # Sidebar for configuration status
    with st.sidebar:
        st.header("Settings")
        absent_keys = verify_api_keys()

        if absent_keys:
            st.error("API Keys Not Found")
            st.write("Please configure these environment variables:")
            for key in absent_keys:
                st.code(f"{key}=your_key_value")
            st.info("Add keys to a .env file in the project directory")
        else:
            st.success("API Keys Properly Set")

        st.header("Agent System")
        st.markdown("""
        - **Info Collector**: Gathers and compiles relevant data  
        - **Data Processor**: Analyzes and interprets collected information  
        - **Report Generator**: Produces structured research outputs
        """)

    # Main content layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Study Subject")
        subject = st.text_input(
            "Input your research subject:",
            placeholder="e.g., AI developments in 2025",
            help="Enter any subject for investigation"
        )

        if st.button("Begin Investigation", type="primary", disabled=bool(absent_keys)):
            if not subject.strip():
                st.error("Please provide a valid subject")
            else:
                st.session_state.study_finished = False
                st.session_state.study_output = None
                st.session_state.study_error = None

                # Display progress indicators
                progress_area = st.container()
                status_area = st.container()

                with progress_area:
                    st.info("Investigation underway...")
                    progress_indicator = st.progress(0)

                    # Simulate progress
                    for i in range(101):
                        progress_indicator.progress(i)
                        time.sleep(0.1)

                with status_area:
                    st.write("Agents processing request...")
                    st.write("Evaluating information...")
                    st.write("Generating report...")

                # Execute research
                try:
                    output = research_crew.kickoff({"topic": subject})
                    st.session_state.study_output = output
                    st.session_state.study_finished = True
                    st.session_state.study_error = None
                except Exception as e:
                    st.session_state.study_error = str(e)
                    st.session_state.study_finished = True

                # Remove progress indicators
                progress_area.empty()
                status_area.empty()

    with col2:
        st.header("Status")
        if st.session_state.study_finished:
            if st.session_state.study_error:
                st.error(f"Error: {st.session_state.study_error}")
            else:
                st.success("Research Completed!")
        else:
            st.info("Waiting for research topic...")

    # Results display
    if st.session_state.study_finished and not st.session_state.study_error:
        st.header("Investigation Outcomes")

        # Display output documents
        output_documents = {
            "research_findings.md": "Initial Findings",
            "analysis_report.md": "Detailed Analysis",
            "final_report.md": "Complete Report",
        }

        tabs = st.tabs(list(output_documents.values()))

        for i, (filename, title) in enumerate(output_documents.items()):
            with tabs[i]:
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    st.markdown(content)

                    # Download option
                    st.download_button(
                        label=f"Save {title}",
                        data=content,
                        file_name=filename,
                        mime="text/markdown"
                    )
                else:
                    st.warning(f"Document {filename} not available")

    # Footer
    st.markdown("---")
    st.markdown("_Powered by CrewAI agents, accelerated by Groq, and deployed with Streamlit_")


if __name__ == "__main__":
    app()