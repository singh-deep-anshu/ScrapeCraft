# ScrapeCraft AI 🌐

**AI-Powered Web Scraping & Content Parsing Tool**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/Beautiful_Soup-4.9.3-green?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek_R1-LLM_Model-61DAFB?style=for-the-badge)](https://deepseek.com/)
[![Ollama](https://img.shields.io/badge/Ollama-LLM_Integration-orange?style=for-the-badge)](https://ollama.com/)


## Features
- **DeepSeek-R1 LLM Integration** - Advanced natural language processing for intelligent content extraction
- **End-to-End Workflow** - URL input → Scraping → AI Parsing → Results
- **Error Resilient** - Robust handling of failed requests and parsing errors
- **Session Management** - Preserves user state between interactions

## Tech Stack
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Frontend Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white) |
| **Core Language**       | ![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat&logo=python&logoColor=white) |
| **Web Scraping**        | ![BeautifulSoup](https://img.shields.io/badge/Beautiful_Soup-4.9.3-green?style=flat) + ![lxml](https://img.shields.io/badge/lxml-4.6.3-blue?style=flat) |
| **AI Engine**           | ![DeepSeek](https://img.shields.io/badge/DeepSeek_R1-LLM_Integration-61DAFB?style=flat) |
| **HTTP Client**         | ![Requests](https://img.shields.io/badge/Requests-2.26.0-red?style=flat) |

## Installation

To run this project locally, you need to install **Ollama** for LLM integration. Follow the steps below:

1. **Install Ollama**:
   - Visit the [Ollama website](https://ollama.com/) to download and install it on your system.
   - After installation, ensure that Ollama is running locally before starting the project.

2. **Clone the Repository**:
```bash
# Clone repository
git clone https://github.com/yourusername/scrapecraft-ai.git
cd scrapecraft-ai

# Install dependencies
pip install -r requirements.txt

# Launch application
streamlit run app.py
```

## Contributing

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

## License

Distributed under the MIT License. See `LICENSE` for more information.

