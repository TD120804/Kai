import ollama

from pathlib import Path


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

PROMPT_FILE = (
    BASE_DIR
    / "brain"
    / "kyoya_lockin.txt"
)


def load_prompt():

    return (
        PROMPT_FILE.read_text(
            encoding="utf-8"
        )
    )


def generate_kyoya_message(

    focus_time,
    current_window,
    same_window_time

):

    template = (
        load_prompt()
    )

    prompt = template.format(

        focus_time=focus_time,

        current_window=current_window,

        same_window_time=same_window_time
    )

    response = ollama.chat(

        model="qwen3:8b",

        messages=[
            {
                "role": "user",

                "content": prompt
            }
        ]
    )

    return (

        response["message"]["content"]

        .strip()
    )