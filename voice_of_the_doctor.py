from dotenv import load_dotenv
load_dotenv()

from gtts import gTTS


def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Converts text to speech using Google Text-to-Speech (gTTS).

    Args:
        input_text (str): Text to convert into speech.
        output_filepath (str): Output MP3 file path.

    Returns:
        str: Path of the generated MP3 file.
    """

    language = "en"

    audio = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )

    audio.save(output_filepath)

    print(f"✅ Audio saved successfully: {output_filepath}")

    return output_filepath


# =====================================================
# Test
# =====================================================

if __name__ == "__main__":

    sample_text = (
        "Hello! I am HealthLens AI. "
        "Your medical report has been analyzed successfully."
    )

    audio_path = text_to_speech_with_gtts(
        input_text=sample_text,
        output_filepath="gtts_testing.mp3"
    )

    print(f"Audio generated successfully: {audio_path}")