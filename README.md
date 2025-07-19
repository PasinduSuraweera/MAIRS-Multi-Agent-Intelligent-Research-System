# MAIRS: Multi-Agent Intelligent Research System

A sophisticated **Streamlit**-based research platform leveraging **CrewAI** and **Groq** to conduct comprehensive, AI-driven investigations across diverse topics, producing structured reports with key findings, analyses, and conclusions.

---

## Overview

**MAIRS: Multi-Agent Intelligent Research System** is a cutting-edge web application designed for researchers, analysts, and professionals seeking in-depth insights on any topic. Powered by a multi-agent AI framework, MAIRS automates the process of gathering, analyzing, and synthesizing information into professional reports. With an intuitive interface and real-time progress tracking, it streamlines complex research workflows, delivering actionable results efficiently.

---

## Key Features

- 🔍 **Automated Research**: Collects current and reliable data from multiple sources using **SerperDevTool**.
- 📊 **Insightful Analysis**: Identifies patterns, trends, and key insights through advanced data processing.
- 📝 **Professional Reports**: Generates structured, publication-ready reports with executive summaries and citations.
- 🖥️ **Interactive UI**: Streamlit-powered interface with real-time progress bars and downloadable outputs.
- 🛠️ **Multi-Agent Workflow**: Combines specialized AI agents for research, analysis, and content creation.
- ⬇️ **Downloadable Outputs**: Save research findings, analyses, and final reports in Markdown format.
- 🔒 **Secure Configuration**: API key management via `.env` files for seamless integration.

---

## Technologies Used

MAIRS is built with a robust stack of modern technologies to ensure efficiency, scalability, and reliability:

- **Streamlit**: Web framework for creating an interactive, user-friendly interface.
- **CrewAI**: Multi-agent orchestration framework for coordinating research, analysis, and writing tasks.
- **Groq**: High-performance AI inference engine powering the language models for all agents.
- **SerperDevTool**: Search tool for gathering real-time, reliable data from the web.
- **FileReadTool & FileWriterTool**: CrewAI tools for reading and writing Markdown files for seamless data handling.
- **Python-dotenv**: Secure management of API keys and environment variables.

---

## How to Use

### Step 1: Configure API Keys
- Set `SERPER_API_KEY` and `GROQ_API_KEY` in a `.env` file in the project root.
- Alternatively, configure environment variables manually in your system.

### Step 2: Input Research Subject
- Enter a research topic in the provided text input (e.g., "AI developments in 2025").
- Click **Begin Investigation** to initiate the research process.

### Step 3: Review Results
- Monitor progress via real-time status updates and a progress bar.
- View results in three tabs: **Initial Findings**, **Detailed Analysis**, and **Complete Report**.
- Download individual reports in Markdown format for further use.

---

## Example Workflow

1. Input a topic, such as "Quantum computing advancements in 2025."
2. The **Info Collector** agent gathers data using **SerperDevTool**.
3. The **Data Processor** agent analyzes findings for trends and insights.
4. The **Report Generator** agent compiles a comprehensive report with an executive summary and citations.
5. Download the resulting Markdown files for presentations, publications, or further analysis.

---

## Project Structure

- **app.py**: Main Streamlit application handling user interface and research execution.
- **crew.py**: Defines the CrewAI multi-agent system, coordinating agents and tasks.
- **agents/**:
  - `research_specialist.py`: Configures the research agent for data collection.
  - `data_analyst.py`: Configures the analysis agent for insight extraction.
  - `content_writer.py`: Configures the writing agent for report generation.
- **tasks/**:
  - `research_task.py`: Defines the research task for gathering data.
  - `analysis_task.py`: Defines the analysis task for processing data.
  - `writing_task.py`: Defines the writing task for report creation.

---