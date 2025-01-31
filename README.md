# ScrapeCraft AI

**AI-Powered Web Scraping & Content Parsing Tool**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/Beautiful_Soup-4.9.3-green?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek_R1-LLM_Model-61DAFB?style=for-the-badge)](https://deepseek.com/)
[![Ollama](https://img.shields.io/badge/Ollama-LLM_Integration-orange?style=for-the-badge)](https://ollama.com/)
[![ScrapingBee](https://img.shields.io/badge/ScrapingBee-Client-FF6A00?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABJ0lEQVQ4jZ2T0U7CUBCFZ7q0QAEFX4wvGh98Mv7/g4kPxgejJkQhQVoKtL3t3B4fSlsKJN6kk3Rn5pw5Z2Z2wY/ED7BfAD4BX8A3MAH7AG4A/0N8B4wK0D2wB6bAgmQk2QO7wK4A3wB7YFmAt8A1sABOQClJADPgHNgU4C0wB5bA6QJ8RLLyV5LzHwF8B1wBp0oVkqyBQwF+BNbA8QJ8QLLyV5Jz4A3YFOBn4AAc/oHXwBvwWoCfgA1w/AdeAW/ApgC/AHvg+A+8Al6BTQF+AQ7A8QK8JFn5K8kF8AbsCvArcACOF+Alkq3/kpwD78C2AL8BB+B4AV6R7PyX5AJ4B3YF+B04AKcL8JpkH0CSC+AD2BfgD+AIxAvwBsnBf0kugU9gX4C/gBMQL8BbJEf/JbkCvoBDAd4AJyBegHdITv5Lcg18AccC/A2cgXgB3iM5BZCcA1/AqQD/AGcgXoAPSM4B/gB7iB4WJwpl5wAAAABJRU5ErkJggg==)](https://www.scrapingbee.com/)

## Features
- **DeepSeek-R1 LLM Integration** - Advanced natural language processing for intelligent content extraction
- **Ad Blocking & Resource Management** - ScrapingBee integration blocks ads and unnecessary resources
- **End-to-End Workflow** - URL input → Scraping → AI Parsing → Results
- **Error Resilient** - Robust handling of failed requests and parsing errors
- **Session Management** - Preserves user state between interactions

## Tech Stack
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Frontend Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white) |
| **Backend**       | ![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat&logo=python&logoColor=white) |
| **Web Scraping**        | ![BeautifulSoup](https://img.shields.io/badge/Beautiful_Soup-4.9.3-green?style=flat)
| **AI Engine**           | [![Ollama](https://img.shields.io/badge/Ollama-orange?style=for-the-badge)](https://ollama.com/) + ![DeepSeek](https://img.shields.io/badge/DeepSeek_R1-LLM_Model-61DAFB?style=flat) |
| **HTTP Client**         | [![ScrapingBee](https://img.shields.io/badge/ScrapingBee_API-blue?style=flat)](https://www.scrapingbee.com/documentation/)|

## Installation

To run this project locally, you need to install **Ollama** for LLM integration. Follow the steps below:

1. **Install Ollama**:
   - Visit the [Ollama website](https://ollama.com/) to download and install it on your system.
   - After installation, ensure that Ollama is running locally before starting the project.
  
2. **Configure ScrapingBee**:
   - Create free account at [ScrapingBee](https://www.scrapingbee.com/)
   - Get your API key from dashboard
   - Update `YOUR_UNIQUE_API_KEY` in `scrape.py` with your actual key

3. **Setup Project**:
```bash
# Clone repository
git clone https://github.com/singh-deep-anshu/scrapecraft.git
cd scrapecraft

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

