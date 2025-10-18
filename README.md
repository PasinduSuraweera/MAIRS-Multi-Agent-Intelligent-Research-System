<div align="center">

# 🤖 MAIRS: Multi-Agent Intelligent Research System

![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-8B5CF6?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-AI_Inference-00ADD8?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**An advanced AI-powered research platform leveraging multi-agent systems to conduct comprehensive investigations and generate professional reports**

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Coming_Soon-46E3B7?style=for-the-badge)](#)

[Features](#-key-features) • [Tech Stack](#️-tech-stack) • [Installation](#-installation) • [Usage](#-how-to-use) • [Architecture](#-system-architecture)

---

</div>

## 📋 Overview

**MAIRS (Multi-Agent Intelligent Research System)** is a cutting-edge research automation platform that harnesses the power of collaborative AI agents to revolutionize how research is conducted. Built on **CrewAI** and powered by **Groq's** lightning-fast inference engine, MAIRS orchestrates specialized AI agents that work together seamlessly to gather, analyze, and synthesize information into comprehensive, publication-ready reports.

Whether you're a researcher exploring emerging technologies, an analyst investigating market trends, or a professional seeking deep insights on complex topics, MAIRS streamlines your research workflow from initial data collection to final report generation — all through an intuitive, interactive interface.

## ✨ Key Features

### 🔍 **Automated Multi-Source Research**
Leverages **SerperDevTool** to collect current, reliable data from diverse web sources, ensuring comprehensive coverage of your research topic.

### 📊 **Advanced AI-Driven Analysis**
Employs sophisticated data processing algorithms to identify patterns, trends, correlations, and key insights from collected information.

### 📝 **Professional Report Generation**
Produces structured, publication-ready reports complete with:
- Executive summaries
- Detailed findings
- In-depth analysis sections
- Proper citations and references
- Markdown formatting for easy conversion

### 🖥️ **Interactive User Interface**
Beautiful **Streamlit**-powered interface featuring:
- Real-time progress tracking
- Live status updates
- Tabbed result viewing
- Download functionality for all outputs

### 🛠️ **Intelligent Multi-Agent Workflow**
Coordinates three specialized AI agents:
- **Info Collector** - Research specialist for data gathering
- **Data Processor** - Analysis expert for insight extraction
- **Report Generator** - Content writer for professional documentation

### ⬇️ **Flexible Output Management**
Download individual components (findings, analysis, final report) in Markdown format for presentations, publications, or further processing.

### 🔒 **Secure API Management**
Environment-based configuration system for secure API key storage and management.

### ⚡ **High-Performance Inference**
Powered by **Groq's** cutting-edge inference technology for rapid response times and efficient processing.

## 🛠️ Tech Stack

<div align="center">

### **Core Technologies**

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Primary programming language | 3.8+ |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web framework for interactive UI | Latest |
| ![CrewAI](https://img.shields.io/badge/CrewAI-8B5CF6?style=flat) | Multi-agent orchestration framework | Latest |
| ![Groq](https://img.shields.io/badge/Groq-00ADD8?style=flat) | High-performance AI inference engine | Latest |

### **Tools & Integrations**

| Tool | Purpose |
|------|---------|
| **SerperDevTool** | Real-time web search and data collection |
| **FileReadTool** | Reading and processing Markdown files |
| **FileWriterTool** | Writing and saving research outputs |
| **Python-dotenv** | Secure environment variable management |
| **Markdown** | Structured document formatting |

</div>

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   STREAMLIT USER INTERFACE                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │ Input Topic  │  │  Progress    │  │  Results Tabs    │ │
│  │   Form       │  │  Tracking    │  │  - Findings      │ │
│  │              │  │              │  │  - Analysis      │ │
│  │              │  │              │  │  - Report        │ │
│  └──────────────┘  └──────────────┘  └──────────────────┘ │
└─────────────────────────────┬───────────────────────────────┘
                              │
                       app.py (Main)
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                  CREWAI ORCHESTRATION LAYER                 │
│                         (crew.py)                           │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            MULTI-AGENT COORDINATION                  │  │
│  │                                                      │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │  │
│  │  │   Agent 1   │  │   Agent 2   │  │   Agent 3   │ │  │
│  │  │    Info     │→ │    Data     │→ │   Report    │ │  │
│  │  │  Collector  │  │  Processor  │  │  Generator  │ │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘ │  │
│  │       ↓                 ↓                 ↓         │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │  │
│  │  │  Research   │  │  Analysis   │  │   Writing   │ │  │
│  │  │    Task     │  │    Task     │  │    Task     │ │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────┬────────────────────────────────┬─────────────┘
               │                                │
        ┌──────▼──────┐                  ┌─────▼──────┐
        │   Groq AI   │                  │  Serper    │
        │   Engine    │                  │   Search   │
        │  (LLM-70b)  │                  │    API     │
        └─────────────┘                  └────────────┘
                │                                │
                └────────────┬───────────────────┘
                             │
                   ┌─────────▼──────────┐
                   │  Output Files      │
                   │  - findings.md     │
                   │  - analysis.md     │
                   │  - final_report.md │
                   └────────────────────┘
```

## 🎯 How It Works

### Phase 1: Data Collection 🔍
The **Info Collector** agent initiates comprehensive web searches using SerperDevTool, gathering current and reliable information from multiple sources relevant to your research topic.

### Phase 2: Intelligent Analysis 📊
The **Data Processor** agent analyzes collected data, identifying:
- Key patterns and trends
- Statistical correlations
- Important insights
- Notable findings
- Emerging themes

### Phase 3: Report Synthesis 📝
The **Report Generator** agent compiles findings into a professional document with:
- Executive summary
- Methodology section
- Detailed findings
- Comprehensive analysis
- Conclusions and recommendations
- Properly formatted citations

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git
- API Keys:
  - Serper API Key ([Get it here](https://serper.dev/))
  - Groq API Key ([Get it here](https://groq.com/))

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/PasinduSuraweera/MAIRS-Multi-Agent-Intelligent-Research-System.git
cd MAIRS-Multi-Agent-Intelligent-Research-System
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root:
```env
SERPER_API_KEY=your_serper_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Access the interface**
Open your browser and navigate to:
```
http://localhost:8501
```

## 📦 Required Dependencies

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
crewai>=0.1.0
groq>=0.4.0
python-dotenv>=1.0.0
langchain>=0.1.0
langchain-groq>=0.0.1
```

## 🚀 How to Use

### Step 1: Launch the Application

Start the Streamlit server and access the web interface through your browser.

### Step 2: Configure API Keys 🔑

Ensure your `.env` file contains valid API keys:
```env
SERPER_API_KEY=your_actual_serper_key
GROQ_API_KEY=your_actual_groq_key
```

### Step 3: Input Research Topic 📝

Enter your research subject in the text input field. Examples:
- "Artificial Intelligence developments in 2025"
- "Climate change impact on agriculture"
- "Blockchain technology in healthcare"
- "Quantum computing breakthroughs"

### Step 4: Begin Investigation 🚀

Click the **"Begin Investigation"** button to start the multi-agent research process.

### Step 5: Monitor Progress 📊

Watch real-time updates as each agent completes its tasks:
- ✅ Research data collection
- ✅ Analysis processing
- ✅ Report generation

### Step 6: Review Results 📄

Navigate through three comprehensive tabs:

**Initial Findings**
- Raw research data
- Source information
- Key facts discovered

**Detailed Analysis**
- Pattern identification
- Trend analysis
- Insight extraction
- Statistical observations

**Complete Report**
- Executive summary
- Full methodology
- Comprehensive findings
- In-depth analysis
- Conclusions and recommendations
- Citations and references

### Step 7: Download Outputs ⬇️

Save your research in Markdown format:
- `findings.md` - Initial research data
- `analysis.md` - Detailed analysis
- `final_report.md` - Complete report

## 💡 Example Workflow

```python
# Example research topic
topic = "Impact of Large Language Models on Education in 2025"

# MAIRS Process:
# 1. Info Collector searches educational databases, news, research papers
# 2. Data Processor identifies trends in AI adoption, student outcomes, challenges
# 3. Report Generator creates comprehensive 10-page report with citations

# Output: Professional report ready for presentation or publication
```

## 📁 Project Structure

```
MAIRS-Multi-Agent-Intelligent-Research-System/
│
├── app.py                          # Main Streamlit application
├── crew.py                         # CrewAI orchestration configuration
│
├── agents/                         # Agent configurations
│   ├── __init__.py
│   ├── research_specialist.py     # Data collection agent
│   ├── data_analyst.py            # Analysis agent
│   └── content_writer.py          # Report generation agent
│
├── tasks/                          # Task definitions
│   ├── __init__.py
│   ├── research_task.py           # Research task configuration
│   ├── analysis_task.py           # Analysis task configuration
│   └── writing_task.py            # Writing task configuration
│
├── tools/                          # Custom tools and utilities
│   ├── __init__.py
│   └── serper_tool.py             # Web search integration
│
├── outputs/                        # Generated reports
│   ├── findings.md
│   ├── analysis.md
│   └── final_report.md
│
├── .env                            # Environment variables (not in git)
├── .env.example                    # Environment template
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # Project documentation
```

## 🎨 User Interface Design

MAIRS features a clean, modern interface built with Streamlit:

### **Navigation & Layout**
- Sidebar for configuration and settings
- Main content area for input and results
- Progress indicators for real-time feedback

### **Visual Elements**
- Color-coded status messages
- Progress bars for task completion
- Tabbed interface for organized results
- Download buttons for easy file access

### **Responsive Design**
- Adapts to different screen sizes
- Mobile-friendly interface
- Accessible color schemes

## 🔒 Security Best Practices

- ✅ API keys stored in `.env` files (never in code)
- ✅ `.env` added to `.gitignore`
- ✅ Environment variable validation
- ✅ Secure API communication
- ✅ No sensitive data in outputs

## ⚡ Performance Optimizations

- 🚀 **Groq Integration** - Sub-second inference times
- 🔄 **Async Processing** - Parallel agent execution where possible
- 💾 **Caching** - Streamlit caching for repeated queries
- 📦 **Efficient File I/O** - Optimized read/write operations

## 🔮 Roadmap & Future Features

### 🚧 In Development
- [ ] 📊 **Data Visualization** - Charts and graphs in reports
- [ ] 🌐 **Multiple Languages** - Support for non-English research
- [ ] 💾 **Database Integration** - Store research history
- [ ] 📧 **Email Reports** - Automated delivery of completed research

### 💡 Planned Features
- [ ] 🤝 **Collaboration Tools** - Share research with team members
- [ ] 🎨 **Custom Templates** - Define your own report formats
- [ ] 🔗 **API Access** - Programmatic access to MAIRS capabilities
- [ ] 📱 **Mobile App** - iOS and Android applications
- [ ] 🎯 **Advanced Filtering** - Fine-tune data sources and credibility
- [ ] 🧠 **Learning System** - Improve based on user feedback
- [ ] 📚 **Citation Styles** - APA, MLA, Chicago formatting
- [ ] 🔍 **Source Verification** - Automatic fact-checking integration

## 🐛 Known Issues & Limitations

- API rate limits may affect research speed on free tiers
- Complex topics may require multiple iterations
- Very recent events (< 24 hours) may have limited coverage
- Large research topics may take 5-10 minutes to complete

## 🤝 Contributing

Contributions are welcome! Help us make MAIRS even better.

### How to Contribute:

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Ideas:
- 🐛 Bug fixes and error handling improvements
- 📚 Documentation enhancements
- 🎨 UI/UX improvements
- 🔧 New agent capabilities
- 🌐 Language support
- 📊 Data visualization features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Pasindu Suraweera**

- 🐙 GitHub: [@PasinduSuraweera](https://github.com/PasinduSuraweera)
- 💼 LinkedIn: [Connect with me](#)
- 📧 Email: [Contact me](#)

## 🙏 Acknowledgments

- 🤖 [CrewAI](https://www.crewai.io/) - Revolutionary multi-agent framework
- ⚡ [Groq](https://groq.com/) - Lightning-fast AI inference
- 🔍 [Serper](https://serper.dev/) - Reliable web search API
- 🎨 [Streamlit](https://streamlit.io/) - Beautiful web app framework
- 🐍 [Python](https://www.python.org/) - The language that powers it all
- 🌟 The open-source AI community

## 📞 Support

Need help or have questions?

- 🐛 [Report a Bug](https://github.com/PasinduSuraweera/MAIRS-Multi-Agent-Intelligent-Research-System/issues)
- 💡 [Request a Feature](https://github.com/PasinduSuraweera/MAIRS-Multi-Agent-Intelligent-Research-System/issues)
- 💬 [Ask a Question](https://github.com/PasinduSuraweera/MAIRS-Multi-Agent-Intelligent-Research-System/discussions)
- 📖 [Read the Docs](#) (Coming Soon)

## 📊 Use Cases

### Academic Research
- Literature reviews
- Topic exploration
- Background research
- Citation gathering

### Business Intelligence
- Market analysis
- Competitive research
- Trend identification
- Industry reports

### Content Creation
- Article research
- Fact-checking
- Topic ideation
- Source compilation

### Personal Learning
- Deep dives into new topics
- Skill development research
- Current events analysis
- Educational exploration

---

<div align="center">

### ⭐ **If you find MAIRS useful, please give it a star!** ⭐

**Made with 🤖 and ❤️ by Pasindu Suraweera**

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=PasinduSuraweera.MAIRS-Multi-Agent-Intelligent-Research-System)

*Revolutionizing research through intelligent automation* 🚀

</div>
