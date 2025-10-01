import os
import tempfile
import warnings

import soundfile as sf
import streamlit as st
from kokoro import KPipeline
from streamlit_shortcuts import add_shortcuts

from constants import LANGUAGES, VOICE_MAP


warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Configuration
THROTTLE_DELAY = 1.0  # seconds after last keystroke


@st.cache_resource
def get_pipeline(lang_code):
    return KPipeline(lang_code=lang_code, repo_id="hexgrad/Kokoro-82M")


def main():
    st.set_page_config(page_title="🗣️ Text-to-Speech Assistant", page_icon=":speech_balloon:", layout="centered")
    st.title("🗣️ Text-to-Speech Kokoro")
    st.write("Enter text and generate speech using Kokoro TTS.")
    language_label = st.selectbox("Choose language:", list(LANGUAGES.keys()), index=1)
    language_code = LANGUAGES[language_label]

    # Dropdown for voice
    voices = VOICE_MAP.get(language_code, [])
    voices = sorted(voices, key=lambda x: x["overall"], reverse=False)

    def formatted_options(idx):
        voice = voices[idx]
        return f"{idx} | {voice['gender']} {voice['name']} ({voice['overall']})"

    # Streamlit selectbox with HTML rendering
    selected_idx = st.selectbox(
        "Choose voice:",
        range(len(voices)),
        format_func=formatted_options,
    )
    selected_voice = voices[selected_idx]["code"]
    pipeline = get_pipeline(language_code)

    # Textbox for input
    text = st.text_area("Enter text: (cmd/ctrl+enter to run)", placeholder="Enter text here...", key="text", height=200)

    # Generate speech button

    if "text" in st.session_state and st.session_state.text.strip() != "":
        with st.spinner("Generating audio..."):
            generator = pipeline(text, voice=selected_voice, speed=1.0, split_pattern=r"\n+")

            # Kokoro returns multiple segments; concatenate them
            audio_segments = []
            for _, _, audio in generator:
                audio_segments.extend(audio)

            # Save to temporary wav file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
                sf.write(tmpfile.name, audio_segments, 24000)
                audio_path = tmpfile.name

            col1, col2 = st.columns([12, 7], width="stretch")
            with col1:
                # Play audio in Streamlit
                audio = st.audio(audio_path, format="audio/wav", autoplay=True)
            with col2:
                # Download button
                with open(audio_path, "rb") as f:
                    coll1, coll2 = st.columns([1, 1], width="stretch")
                    with coll1:
                        with st.container():
                            st.download_button(
                                label="💾 Download", data=f, file_name="generated_audio.wav", mime="audio/wav"
                            )
                    with coll2:
                        st.button("🔄 Replay", key="replay_btn")
                        add_shortcuts(replay_btn=["cmd+enter", "ctrl+enter"])

    else:
        st.warning("Please enter some text.")


if __name__ == "__main__":
    main()
