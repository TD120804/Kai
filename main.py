import time
import ollama


from voice.input import (
    listen,
    get_text_input
)

from voice.output import (
    speak
)

from memory.memory_manager import (
    load_system_prompt,
    handle_memory_command
)

from automation.router import (
    handle_automation
)


# ==================================================
# CONFIG
# ==================================================

MODEL_NAME = "qwen2.5:3b"

TEMPERATURE = 0.95

TOP_P = 0.9

NUM_PREDICT = 100

MAX_HISTORY = 6


EXIT_WORDS = [

    "exit",

    "quit",

    "bye",

    "goodbye"
]


# ==================================================
# SYSTEM PROMPT
# ==================================================

SYSTEM_PROMPT = (
    load_system_prompt()
)


# ==================================================
# MODE SELECTION
# ==================================================

mode = input(
    "\nChoose mode (voice/text): "
).strip().lower()

TEXT_MODE = (
    mode == "text"
)


# ==================================================
# CONVERSATION MEMORY
# ==================================================

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


# ==================================================
# RESPONSE GENERATION
# ==================================================

def generate_response(
    user_input,
    conversation
):

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    print(
        "\n🖤 Kai is thinking..."
    )

    messages_to_send = (
        [conversation[0]]
        +
        conversation[
            -MAX_HISTORY:
        ]
    )

    total_chars = sum(
        len(msg["content"])
        for msg in (
            messages_to_send
        )
    )

    print(
        f"\n📚 Messages being sent: "
        f"{len(messages_to_send)}"
    )

    print(
        f"🧠 Total chars sent: "
        f"{total_chars}"
    )

    start = time.time()

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages_to_send,
        options={
            "temperature":
            TEMPERATURE,

            "num_predict":
            NUM_PREDICT,

            "top_p":
            TOP_P
        }
    )

    print(
        f"\n⚡ Ollama took "
        f"{time.time() - start:.2f} sec"
    )

    kai_reply = (
        response["message"]["content"]
    )

    conversation.append(
        {
            "role": "assistant",
            "content": kai_reply
        }
    )

    return kai_reply


# ==================================================
# STARTUP
# ==================================================

speak("Morning. Kai.")


# ==================================================
# MAIN LOOP
# ==================================================

while True:

    # ==================================================
    # INPUT
    # ==================================================

    if TEXT_MODE:

        user_input = (
            get_text_input()
        )

    else:

        user_input = (
            listen()
        )

    if not user_input:
        continue

    user_input_lower = (
        user_input
        .lower()
        .strip()
    )

    # ==================================================
    # EXIT
    # ==================================================

    if (
        user_input_lower
        in EXIT_WORDS
    ):

        speak(
            "Alright. Try not to start fourteen new projects while I'm gone."
        )

        break

    # ==================================================
    # MEMORY
    # ==================================================

    handled, response = (
        handle_memory_command(
            user_input
        )
    )

    if handled:

        speak(
            response
        )

        continue

    # ==================================================
    # AUTOMATION
    # ==================================================

    handled, response = (
        handle_automation(
            user_input
        )
    )

    if handled:

        speak(
            response
        )

        continue

    # ==================================================
    # NORMAL CONVERSATION
    # ==================================================

    try:

        kai_reply = (
            generate_response(
                user_input,
                conversation
            )
        )

        speak(
            kai_reply
        )

    except Exception as e:

        print(
            f"\nError: {e}"
        )

        speak(
            "Okay... tiny issue. Something broke for a second. Give me a moment."
        )