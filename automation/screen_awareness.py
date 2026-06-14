import time
import mss
from PIL import Image
import ollama


def capture_screen():

    # =====================================
    # Countdown signal
    # =====================================

    print(
        "\n🖤 KAI: Alright. Show me."
    )

    for i in range(3, 0, -1):

        print(
            f"👀 Looking in {i}..."
        )

        time.sleep(1)

    screenshot_path = "screen.png"

    with mss.mss() as sct:

        monitor = sct.monitors[1]

        screenshot = sct.grab({

            "top": monitor["top"],
            "left": monitor["left"],
            "width": monitor["width"],
            "height": monitor["height"]
        })

        img = Image.frombytes(

            "RGB",

            screenshot.size,

            screenshot.rgb
        )

        # =====================================
        # Resize image
        # Faster + avoids token overflow
        # =====================================

        img.thumbnail(
            (960, 540)
        )

        img.save(

            screenshot_path,

            optimize=True,

            quality=70
        )

    return screenshot_path


def get_prompt(
    task
):

    prompts = {

        "general":
        """
You are Kai.

Describe ONLY what is visible.

Do not invent details.

Be concise.
        """,

        "debug":
        """
You are Kai.

Look at this screen carefully.

If code, terminal, or errors exist:

1. Identify the visible problem
2. Quote visible errors
3. Explain what likely happened
4. Suggest the next step

DO NOT invent details.
        """,

        "explain":
        """
You are Kai.

Explain what is on this screen clearly.

If code exists:
- explain what it does

If a website/document exists:
- explain the content simply

Be concise.
        """,

        "summary":
        """
You are Kai.

Summarize what is visible.

If this is a webpage, article,
document, Wattpad story, or PDF:

- summarize the key content
- explain the important idea

Be concise.
        """,

        "next_step":
        """
You are Kai.

Look at the screen and suggest:

What should the user do next?

Be practical.
        """
    }

    return prompts.get(
        task,
        prompts["general"]
    )

def analyze_screen(
    task="general"
):

    image_path = (
        capture_screen()
    )

    response = ollama.chat(

        model="qwen2.5vl:3b",

        options={
            "num_ctx": 2048
        },

        messages=[
            {
                "role":
                "user",

                "content":
                get_prompt(
                    task
                ),

                "images":
                [image_path]
            }
        ]
    )

    return (
        response["message"]
        ["content"]
    )