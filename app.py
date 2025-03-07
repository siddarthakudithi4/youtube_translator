# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from langchain_groq import ChatGroq
# from langchain.schema import SystemMessage, HumanMessage
# from pytube import extract
# import os

# # Load environment variables
# from dotenv import load_dotenv
# load_dotenv()

# def extract_transcript(video_url):
#     try:
#         video_id = extract.video_id(video_url)
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         return " ".join([entry['text'] for entry in transcript])
#     except Exception as e:
#         st.error(f"Error extracting transcript: {str(e)}")
#         return None

# def translate_text(text, target_language):
#     llm = ChatGroq(
#         temperature=0.1,
#         model_name="mixtral-8x7b-32768",
#         groq_api_key=os.getenv("GROQ_API_KEY")
#     )
    
#     messages = [
#         SystemMessage(content=f"Translate the following text to {target_language}. Maintain original formatting."),
#         HumanMessage(content=text)
#     ]
#     return llm(messages).content

# def main():
#     st.title("YouTube Transcript Translator 🌐 (Groq)")
    
#     video_url = st.text_input("Enter YouTube Video URL:")
#     target_language = st.text_input("Enter Target Language (e.g., 'French'):")
    
#     if st.button("Translate Transcript"):
#         if video_url and target_language:
#             with st.spinner("Processing..."):
#                 transcript = extract_transcript(video_url)
#                 if transcript:
#                     translated = translate_text(transcript, target_language)
#                     st.subheader("Translated Transcript:")
#                     st.write(translated)
#         else:
#             st.warning("Please provide both YouTube URL and target language")

# if __name__ == "__main__":
#     main()







# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from langchain_groq import ChatGroq
# from langchain.schema import SystemMessage, HumanMessage
# from pytube import extract
# from gtts import gTTS
# import os
# import tempfile

# # Load environment variables
# from dotenv import load_dotenv
# load_dotenv()

# # Language code mapping
# LANGUAGE_CODES = {
#     'english': 'en',
#     'spanish': 'es',
#     'french': 'fr',
#     'german': 'de',
#     'italian': 'it',
#     'hindi': 'hi',
#     'japanese': 'ja',
#     'korean': 'ko',
#     'chinese': 'zh-CN',
#     'arabic': 'ar'
# }

# def extract_transcript(video_url):
#     try:
#         video_id = extract.video_id(video_url)
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         return " ".join([entry['text'] for entry in transcript])
#     except Exception as e:
#         st.error(f"Error extracting transcript: {str(e)}")
#         return None

# def translate_text(text, target_language):
#     llm = ChatGroq(
#         temperature=0.1,
#         model_name="mixtral-8x7b-32768",
#         groq_api_key=os.getenv("GROQ_API_KEY")
#     )
    
#     messages = [
#         SystemMessage(content=f"Translate the following text to {target_language}. Maintain original formatting."),
#         HumanMessage(content=text)
#     ]
#     return llm(messages).content

# def text_to_speech(text, language):
#     try:
#         # Get language code
#         lang_code = LANGUAGE_CODES.get(language.lower(), 'en')
        
#         # Create temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
#             tts = gTTS(text=text, lang=lang_code, slow=False)
#             tts.save(fp.name)
#             return fp.name
#     except Exception as e:
#         st.error(f"Error in text-to-speech conversion: {str(e)}")
#         return None

# def main():
#     st.title("YouTube Transcript Translator 🌐 (Groq)")
    
#     video_url = st.text_input("Enter YouTube Video URL:")
#     target_language = st.text_input("Enter Target Language (e.g., 'French'):")
    
#     translated_text = None
    
#     if st.button("Translate Transcript"):
#         if video_url and target_language:
#             with st.spinner("Processing translation..."):
#                 transcript = extract_transcript(video_url)
#                 if transcript:
#                     translated_text = translate_text(transcript, target_language)
#                     st.subheader("Translated Transcript:")
#                     st.write(translated_text)
#         else:
#             st.warning("Please provide both YouTube URL and target language")

#     # Show speech button only if translation exists
#     if translated_text:
#         if st.button("Convert to Speech 🔊"):
#             with st.spinner("Generating audio..."):
#                 audio_file = text_to_speech(translated_text, target_language)
#                 if audio_file:
#                     st.audio(audio_file, format='audio/mp3')
#                     # Clean up temporary file
#                     os.unlink(audio_file)

# if __name__ == "__main__":
#     main()



import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from pytube import extract
from gtts import gTTS
import os
import tempfile
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Expanded language code mapping
LANGUAGE_CODES = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'italian': 'it',
    'hindi': 'hi',
    'japanese': 'ja',
    'korean': 'ko',
    'chinese': 'zh-CN',
    'arabic': 'ar',
    'portuguese': 'pt',
    'russian': 'ru',
    'turkish': 'tr'
}

def extract_transcript(video_url):
    try:
        st.write("🔍 Extracting video ID...")
        video_id = extract.video_id(video_url)
        st.write(f"📹 Video ID found: {video_id}")
        
        st.write("📄 Fetching transcript...")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        st.error(f"❌ Error extracting transcript: {str(e)}")
        return None

def translate_text(text, target_language):
    try:
        st.write("🌐 Starting translation...")
        llm = ChatGroq(
            temperature=0.1,
            model_name="mixtral-8x7b-32768",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        
        messages = [
            SystemMessage(content=f"Translate the following text to {target_language}. Maintain original formatting."),
            HumanMessage(content=text)
        ]
        result = llm(messages).content
        st.write("✅ Translation successful!")
        return result
    except Exception as e:
        st.error(f"❌ Translation error: {str(e)}")
        return None

def text_to_speech(text, language):
    try:
        lang_code = LANGUAGE_CODES.get(language.lower(), None)
        if not lang_code:
            st.error(f"❌ Language '{language}' not supported for speech")
            return None
            
        st.write("🔊 Generating speech...")
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts = gTTS(text=text, lang=lang_code, slow=False)
            tts.save(fp.name)
            st.write(f"💾 Audio saved to: {fp.name}")
            return fp.name
    except Exception as e:
        st.error(f"❌ Text-to-speech error: {str(e)}")
        return None

def main():
    st.title("YouTube Transcript Translator 🌐 (Groq)")
    
    # Initialize session state
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = None
    
    video_url = st.text_input("Enter YouTube Video URL:")
    target_language = st.text_input("Enter Target Language (e.g., 'French'):").strip().lower()
    
    if st.button("Translate Transcript"):
        if video_url and target_language:
            with st.spinner("Processing..."):
                transcript = extract_transcript(video_url)
                if transcript:
                    st.session_state.translated_text = translate_text(transcript, target_language)
        else:
            st.warning("⚠️ Please provide both YouTube URL and target language")

    if st.session_state.translated_text:
        st.subheader("Translated Transcript:")
        st.write(st.session_state.translated_text)
        
        if st.button("Convert to Speech 🔊"):
            with st.spinner("Generating audio..."):
                audio_file = text_to_speech(
                    st.session_state.translated_text,
                    target_language
                )
                if audio_file:
                    st.audio(audio_file, format='audio/mp3')
                    try:
                        os.unlink(audio_file)
                        st.write("♻️ Temporary audio file cleaned up")
                    except Exception as e:
                        st.error(f"❌ Error cleaning up audio file: {str(e)}")

if __name__ == "__main__":
    main()