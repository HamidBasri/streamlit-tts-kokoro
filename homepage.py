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

sample_texts = [
    "Text-to-Speech technology allows computers to convert written text into natural-sounding speech. It is widely used in accessibility tools, voice assistants, and language learning applications.",
    "Once upon a time in a quiet village, there was a little library where books could speak. Every evening, the shelves would whisper stories, bringing joy to anyone who listened.",
    "Artificial intelligence has transformed the way we interact with technology. Neural TTS models now deliver realistic voices, supporting multiple languages and accents.",
    "Learning a new language becomes easier with the help of TTS systems, which provide accurate pronunciation and intonation for learners around the world.",
    "In the future, personalized voice synthesis will enable users to create digital voices that sound just like them, opening new possibilities for communication and creativity.",
]


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

    if "text" not in st.session_state:
        st.session_state.text = ""

    def set_text(text):
        st.session_state.text = text

    # Textbox for input
    text = st.text_area(
        "Enter text: (cmd/ctrl+enter to run)",
        placeholder="Enter text here...",
        key="text",
        height=200,
    )

    # --- Display buttons in one row ---
    with st.container(horizontal=True):
        st.button("① Sample 1", key="sample_1_btn", on_click=lambda: set_text(sample_texts[0]))
        st.button("② Sample 2", key="sample_2_btn", on_click=lambda: set_text(sample_texts[1]))
        st.button("③ Sample 3", key="sample_3_btn", on_click=lambda: set_text(sample_texts[2]))
        st.button("④ Sample 4", key="sample_4_btn", on_click=lambda: set_text(sample_texts[3]))
        st.button("Clear", key="clear_btn", on_click=lambda: set_text(""))

    # Generate speech button
    if "text" in st.session_state and st.session_state.text.strip() != "":
        st.divider()
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

            with st.container(horizontal=True, width="stretch"):
                # Play audio in Streamlit
                audio = st.audio(audio_path, format="audio/wav", autoplay=True, width="stretch")
                with st.container(horizontal=True, gap="small", width=230):
                    # Download button
                    with open(audio_path, "rb") as f:
                        st.download_button(
                            label="💾 Download", data=f, file_name="generated_audio.wav", mime="audio/wav"
                        )
                    # Replay button
                    st.button("🔄 Replay", key="replay_btn")
                    add_shortcuts(replay_btn=["cmd+enter", "ctrl+enter"])

    else:
        st.warning("Please enter some text.")


if __name__ == "__main__":
    main()
