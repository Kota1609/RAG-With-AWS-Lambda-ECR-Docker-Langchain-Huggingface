# 🎓 UNT Multi-Agent System

A sophisticated multi-agent system for the University of North Texas (UNT) that provides specialized assistance for various academic tasks using the 🧠 Gemma 3 27B model.

## 📺 Video Demonstration

[Watch Video](https://github.com/user-attachments/assets/07a63f0b-7b12-4bca-88d7-7ebbdb5f2f70)

## 📌 Overview

This project implements a multi-agent system with specialized agents for different academic tasks:

- 📧 **Email Composition Agent**: Helps draft professional academic emails
- 📑 **Research Paper Agent**: Assists with research paper composition and analysis
- 📚 **Academic Concepts Agent**: Explains academic concepts and theories
- 🔗 **Redirect Agent**: Directs users to appropriate UNT resources
- 🏫 **General Agent**: Handles general queries about UNT

The system uses a sophisticated classification mechanism to determine which agent should handle a user query, and each agent follows a structured, step-by-step reasoning approach to provide comprehensive responses.

## 🚀 Features

- 🤖 **Specialized Agents**: Each agent is tailored to a specific academic task
- 🎯 **Intelligent Classification**: Uses TF-IDF vectorization and cosine similarity to classify user queries
- 📝 **Structured Responses**: All agents provide well-formatted, comprehensive responses
- 🛠 **Pydantic Models**: Input validation and structured data handling
- 💻 **Chainlit Interface**: Modern web UI for interacting with the agents
- ⚡ **vLLM Integration**: Efficient inference using the Gemma 3 27B model

## 🏗️ Architecture

The system is built using a modern tech stack:

- **Web Scraping**: Automated collection of UNT website data
- **Vector Database**: ChromaDB for efficient document storage and retrieval
- **Containerization**: Docker for consistent deployment
- **Session Management**: Redis for managing user sessions
- **LLM Integration**: Ollama for accessing language models
- **Web Interface**: Chainlit for the user interface

## 🤖 Agent Capabilities

### 📧 Email Composition Agent
- Drafts professional academic emails
- Follows proper email structure and formatting
- Maintains appropriate tone and style
- Handles common scenarios like extension requests and meeting scheduling

### 📑 Research Paper Agent
- Helps with research paper planning and structure
- Provides guidance on research methodology
- Ensures proper academic writing standards
- Supports various citation styles and formats

### 📚 Academic Concepts Agent
- Explains academic concepts and theories
- Adapts explanations to different difficulty levels
- Provides learning support and resources
- Covers various subject areas

### 🔗 Redirect Agent
- Directs users to relevant UNT resources
- Provides detailed information about available services
- Includes direct links to resources
- Offers contact information and usage guidelines

## 🛠️ Development

To modify or extend the system:

1. Update the agent prompts in `src/config/prompts.py`
2. Modify the agent implementations in `src/agents/specialized_agents.py`
3. Adjust the classification system in `src/models/classification.py`
4. Update the Pydantic models in `src/models/query_models.py`

## 📦 Installation

```bash
# Clone the repository
git clone [repository-url]

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run the application
docker-compose up
```

## 🔧 Configuration

The system requires the following environment variables:

- `REDIS_URL`: Redis connection string
- `OLLAMA_API_URL`: Ollama API endpoint
- `CHROMA_DB_PATH`: Path to ChromaDB storage
- `MODEL_NAME`: Name of the LLM model to use

## 📞 Support

For support, please contact [Srichandan Kota](https://srichandan-kota.vercel.app/) or open an issue in the repository.

---

Made with ❤️ for UNT by [Srichandan Kota](https://srichandan-kota.vercel.app/)
