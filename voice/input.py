import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr


recognizer = sr.Recognizer()


def listen():
    """
    Voice input
    """

    duration = 8
    sample_rate = 44100

    print("\n🎙 Listening...")

    try:

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(
            "input.wav",
            sample_rate,
            recording
        )

        with sr.AudioFile(
            "input.wav"
        ) as source:

            audio = recognizer.record(
                source
            )

        text = recognizer.recognize_google(
            audio
        )

        text = text.strip()

        if text:

            print(
                f"\n🧍 You: {text}"
            )

            return text

        return None

    except Exception as e:

        print(
            f"\nDidn't catch that 😭 ({e})"
        )

        return None


def get_text_input():
    """
    Text mode input
    """

    text = input(
        "\n🧍 You: "
    ).strip()

    if text:
        return text

    return None