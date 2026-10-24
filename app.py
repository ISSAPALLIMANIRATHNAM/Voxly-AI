import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from config.settings import APP_NAME, TAGLINE
from components.ui import inject_css, render_header, render_sidebar, render_hero
from database.db import init_db
from pages.home import render_home
from pages.text_to_speech import render_tts
from pages.translator import render_translator
from pages.ai_chat import render_chat
from pages.history import render_history
from pages.saved_audio import render_saved_audio
from pages.settings import render_settings

load_dotenv()
st.set_page_config(page_title=APP_NAME, page_icon="🎙️", layout="wide", initial_sidebar_state="auto")
Path("data/audio").mkdir(parents=True, exist_ok=True)
init_db()

if "theme" not in st.session_state:
    st.session_state.theme = "Light"
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "tts_result" not in st.session_state:
    st.session_state.tts_result = None

inject_css(st.session_state.theme)
render_header()
page = render_sidebar()
if page == "Home":
    render_hero()
    render_home()
elif page == "Text to Speech":
    render_tts()
elif page == "Translator":
    render_translator()
elif page == "AI Chat":
    render_chat()
elif page == "History":
    render_history()
elif page == "Saved Audio":
    render_saved_audio()
elif page == "Settings":
    render_settings()
else:
    render_home()
