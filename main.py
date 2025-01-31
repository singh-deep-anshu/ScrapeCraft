import streamlit as st
from scrape import scrape_web, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

# Page Configuration
st.set_page_config(
    page_title="ScrapeCraft",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Light Pink Accent Theme Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #121212;
            color: #e0e0e0;
        }
        
        .stButton>button {
            background-color: #FF69B4 !important;  /* Light Pink */
            color: #ffffff !important;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            border: none;
        }
        
        h1, h2, h3 {
            color: #FF69B4 !important;  /* Light Pink */
            padding-left: 0.5rem !important;
            border-left: 3px solid #FF69B4;
        }
        
        .stTextInput>div>div>input, .stTextArea textarea {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            border: 1px solid #373737 !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }
        
        .stExpander {
            background-color: #1e1e1e !important;
            border: 1px solid #373737 !important;
            border-radius: 8px !important;
        }
        
        .stMarkdown {
            color: #e0e0e0 !important;
        }
        
        .success-box {
            background-color: #2e7d32;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .error-box {
            background-color: #c62828;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .warning-box {
            background-color: #f9a825;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# User Name Handling
if 'username' not in st.session_state:
    with st.container():
        st.title("Welcome to ScrapeCraft AI! 👋")
        st.markdown("**Your AI-powered web scraping and parsing assistant.**")
        with st.form("user_form"):
            name = st.text_input("**Please enter your name to continue:**", 
                               placeholder="Deepanshu Singh")
            submitted = st.form_submit_button("Continue")
            if submitted and name:
                st.session_state.username = name
                st.rerun()
        st.stop()

# Main Content
st.title(f"Hi {st.session_state.username}! Welcome to **ScrapeCraft AI**")
st.markdown("**Your AI-powered web scraping and parsing assistant.**")
st.divider()

# Usage Instructions
with st.container():
    st.subheader("📋 How to Use")
    with st.expander("**Workflow Guide**", expanded=True):
        st.markdown("""
        1. **Enter URL** - Provide a website address
        2. **Scrape Content** - Extract website content
        3. **Parse Data** - Describe what to extract
        4. **Get Results** - View and save your data
        """)
    st.divider()

# URL Input and Processing
url = st.text_input("**🌐 Enter Website URL**", 
                   placeholder="https://example.com",
                   help="Include http:// or https://")

if st.button("Start Scraping", use_container_width=True):
    if url:
        try:
            with st.spinner("🕷️ Crawling website..."):
                result = scrape_web(url)
                body_content = extract_body_content(result)
                cleaned_content = clean_body_content(body_content)
                st.session_state.dom_content = cleaned_content
                st.markdown("<div class='success-box'>✅ Content successfully scraped!</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"<div class='error-box'>Scraping failed: {str(e)}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='warning-box'>Please enter a valid URL first</div>", unsafe_allow_html=True)

# Display Scraped Content
if "dom_content" in st.session_state:
    with st.expander("🔍 View Scraped Content", expanded=False):
        st.code(st.session_state.dom_content, language="html")

    st.divider()
    st.subheader("Content Analysis")
    parse_desc = st.text_input("**What would you like to extract?**",
                              placeholder="e.g., 'Extract all email addresses' or 'List main headings'")
    
    if st.button("✨ Parse Content", type="primary"):
        if parse_desc:
            with st.spinner("Analyzing content..."):
                try:
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks, parse_desc)
                    
                    st.markdown("<div class='success-box'>✅ Parsing complete!</div>", unsafe_allow_html=True)
                    st.subheader("Results")
                    st.markdown(f"```\n{result}\n```")
                except Exception as e:
                    st.markdown(f"<div class='error-box'>Parsing error: {str(e)}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='warning-box'>Please describe what to extract</div>", unsafe_allow_html=True)