import ollama

from memory.memory_manager import (
    load_system_prompt
)

# ==================================================
# MODEL CONFIG
# ==================================================

MODEL_NAME = "qwen2.5:3b"

TEMPERATURE = 0.95

TOP_P = 0.9

NUM_PREDICT = 100

MAX_HISTORY = 6

# ==================================================
# SYSTEM PROMPT
# ==================================================

SYSTEM_PROMPT = (
    load_system_prompt()
)

# ==================================================
# CONVERSATION
# ==================================================

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

# ==================================================
# GENERATE RESPONSE
# ==================================================

def generate_response(user_input):

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    messages_to_send = (
        [conversation[0]]
        +
        conversation[-MAX_HISTORY:]
    )

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