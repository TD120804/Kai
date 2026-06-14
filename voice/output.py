import asyncio
import edge_tts
import tempfile
import subprocess


VOICE = "en-GB-ThomasNeural"

async def generate_voice(
    text,
    path
):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="-20%"
    )

    await communicate.save(path)


def speak(text):

    print(
        f"\n🖤 KAI: {text}\n"
    )

    import re


    clean_text = re.sub(
        r"[^\w\s.,!?':;()-]",
        "",
        text
    )

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp_audio:

            temp_path = (
                temp_audio.name
            )

        asyncio.run(
            generate_voice(
                clean_text,
                temp_path
            )
        )

        subprocess.run(
            [
                "C:/mpv/mpv.exe",
                "--no-terminal",
                "--force-window=no",
                "--really-quiet",
                temp_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception as e:

        print(
            f"\nVoice error: {e}"
        )