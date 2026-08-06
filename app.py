import streamlit as st
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts



st.set_page_config(
    page_title="HealthLens AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* ===========================
MAIN BACKGROUND
=========================== */

.stApp{
    background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
    color: white;
}


/* ===========================
HEADER
=========================== */

.main-title{
    font-size:60px;
    font-weight:800;
    color:#38BDF8;
    text-align:center;
    margin-bottom:5px;
}

.sub-title{
    font-size:24px;
    text-align:center;
    color:#CBD5E1;
    margin-bottom:40px;
}


/* ===========================
SIDEBAR
=========================== */

section[data-testid="stSidebar"]{
    background:#020617;
}

section[data-testid="stSidebar"] *{
    color:white;
}


/* ===========================
HEADINGS
=========================== */

h1,h2,h3,h4,h5,h6{
    color:white !important;
}


/* ===========================
TEXT
=========================== */

label,
p,
span,
div{
    color:#E5E7EB;
}


/* ===========================
FILE UPLOADER
=========================== */

[data-testid="stFileUploader"]{

    background:#1E293B;

    border:2px dashed #38BDF8;

    border-radius:18px;

    padding:20px;

}


/* ===========================
BUTTON
=========================== */

.stButton>button{

    width:100%;

    height:58px;

    font-size:20px;

    font-weight:bold;

    border-radius:15px;

    border:none;

    color:white;

    background:linear-gradient(90deg,#2563EB,#06B6D4);

}

.stButton>button:hover{

    background:linear-gradient(90deg,#1D4ED8,#0891B2);

}


/* ===========================
TEXTAREA
=========================== */

textarea{

    background:#1E293B !important;

    color:white !important;

}


/* ===========================
TEXT INPUT
=========================== */

input{

    background:#1E293B !important;

    color:white !important;

}


/* ===========================
SUCCESS BOX
=========================== */

.stSuccess{

    background:#064E3B;

    color:white;

    border-radius:12px;

}


/* ===========================
ERROR BOX
=========================== */

.stError{

    border-radius:12px;

}


/* ===========================
INFO BOX
=========================== */

.stInfo{

    background:#1E3A8A;

    color:white;

    border-radius:12px;

}


/* ===========================
TABS
=========================== */

button[data-baseweb="tab"]{

    color:white !important;

    font-size:17px;

    font-weight:600;

}


/* ===========================
AUDIO PLAYER
=========================== */

audio{

    width:100%;

}


/* ===========================
FOOTER
=========================== */

.footer{

    text-align:center;

    color:#94A3B8;

    margin-top:40px;

}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.image("https://img.icons8.com/color/480/stethoscope.png", width=90)

    st.title("HealthLens AI")

    st.markdown("---")

    st.markdown("""
### About

HealthLens AI is an AI-powered medical assistant capable of:

- 🩺 Medical Image Analysis
- 🎤 Voice-to-Text
- 🧠 AI Diagnosis
- 🔊 Voice Response

Powered by:

- Groq Whisper
- Groq Vision
- gTTS
""")

    st.markdown("---")

    st.success("AI Ready")


st.markdown("<div class='main-title'>🩺 HealthLens AI</div>", unsafe_allow_html=True)

st.markdown("<div class='sub-title'>AI Medical Assistant with Vision + Voice</div>", unsafe_allow_html=True)



SYSTEM_PROMPT = """
You have to act as a professional doctor.

What's in this image?

Do you find anything wrong medically?

Suggest possible remedies.

Do not use bullet points.

Do not use markdown.

Do not mention AI.

Keep answer under two sentences.

Answer naturally like a doctor.
"""


left, right = st.columns(2)


with left:

    st.markdown("### 📷 Upload Medical Image")

    image = st.file_uploader(
        "Choose Image",
        type=["jpg", "jpeg", "png"]
    )

    if image:

        st.image(image, use_container_width=True)


with right:

    st.markdown("### 🎤 Upload Patient Voice")

    audio = st.file_uploader(
        "Choose Audio",
        type=["mp3", "wav", "m4a"]
    )

    if audio:

        st.audio(audio)


st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button("🔍 Analyze")

if analyze:

    if image is None:
        st.error("⚠️ Please upload a medical image.")
        st.stop()

    if audio is None:
        st.error("⚠️ Please upload an audio file.")
        st.stop()

    try:

        with st.spinner("🧠 HealthLens AI is analyzing your case..."):


            temp_dir = tempfile.mkdtemp()

            image_path = os.path.join(
                temp_dir,
                image.name
            )

            audio_path = os.path.join(
                temp_dir,
                audio.name
            )


            with open(image_path, "wb") as f:
                f.write(image.getbuffer())


            with open(audio_path, "wb") as f:
                f.write(audio.getbuffer())


            speech_text = transcribe_with_groq(
                stt_model="whisper-large-v3",
                audio_filepath=audio_path,
                GROQ_API_KEY=os.getenv("GROQ_API_KEY")
            )


            encoded_image = encode_image(image_path)


            doctor_response = analyze_image_with_query(
                query=SYSTEM_PROMPT + "\n\nPatient says: " + speech_text,
                model="qwen/qwen3.6-27b",
                encoded_image=encoded_image
            )

            output_audio = os.path.join(
                temp_dir,
                "doctor_response.mp3"
            )

            generated_audio = text_to_speech_with_gtts(
                input_text=doctor_response,
                output_filepath=output_audio
            )

        st.success("✅ Analysis Complete!")

        tab1, tab2, tab3 = st.tabs(
            [
                "🎤 Speech",
                "🩺 Diagnosis",
                "🔊 Voice Response"
            ]
        )

        with tab1:

            st.markdown("## Patient Speech")

            st.info(speech_text)

        with tab2:

            st.markdown("## AI Doctor Diagnosis")

            st.success(doctor_response)

        with tab3:

            st.markdown("## Doctor Voice")

            st.audio(generated_audio)

            with open(generated_audio, "rb") as file:

                st.download_button(
                    "⬇ Download Voice",
                    file,
                    file_name="doctor_response.mp3",
                    mime="audio/mp3"
                )

    except Exception as e:

        st.error("Something went wrong.")

        st.exception(e)


st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:gray;padding:20px;'>

    🩺 <b>HealthLens AI</b><br>

    AI Medical Assistant with Vision, Speech & LLMs<br><br>

    Built using <b>Groq Whisper</b>, <b>Groq Vision</b> and <b>gTTS</b>.

    </div>
    """,
    unsafe_allow_html=True
)