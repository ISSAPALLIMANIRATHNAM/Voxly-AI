# Voxly AI — Speak. Translate. Connect.

A Streamlit multilingual voice assistant with text-to-speech, translation, AI chat, history, saved audio and theme settings.

## Features
- Text to speech using Google Text-to-Speech (internet required)
- Multilingual translation using deep-translator (internet required)
- Optional OpenAI-powered AI chat
- SQLite-backed history and saved audio metadata
- Light and dark theme
- Audio download and playback

## Run on Windows
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
streamlit run app.py
```
Add your own OpenAI API key to `.env` to enable AI Chat and OpenAI text-to-speech voices, including childlike styles:
`OPENAI_API_KEY=your_key_here`
Optionally set `OPENAI_TTS_MODEL` to choose the speech model.

OpenAI does not provide a shared free API key. API access and any free credits depend on your OpenAI account; usage may be billed. Keep your key private and never paste it into source code or commit it.

## Notes
Internet is required for gTTS, OpenAI speech generation, and Google translation. Childlike voice styles use the OpenAI Audio API; the available voices are AI-generated voice styles, not recordings of children. Do not commit `.env` or API keys.

The current OpenAI Speech API model (`gpt-4o-mini-tts`) is scheduled to shut down on January 6, 2027. OpenAI's documented replacement requires a different Realtime API workflow, so the integration will need a code migration before that date.
