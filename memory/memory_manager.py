# ==================================================
# CORE PROMPT
# ==================================================

CORE_PROMPT = """
You are Kai.

You are witty, warm, observant, slightly teasing.
Keep responses conversational and concise.

Memory Rules:
- Only remember things when user explicitly says:
  "remember"
- Never automatically save sensitive mental health,
  crisis, medical, or deeply personal information.
"""


# ==================================================
# LOAD SYSTEM PROMPT
# ==================================================

def load_system_prompt():

    try:

        with open(
            "memory/projects.txt",
            "r",
            encoding="utf-8"
        ) as f:

            projects = f.read()

    except:

        projects = (
            "No project data found."
        )

    try:

        with open(
            "memory/memories.txt",
            "r",
            encoding="utf-8"
        ) as f:

            memories = f.read()

    except:

        memories = (
            "No memories found."
        )

    return f"""
{CORE_PROMPT}

PROJECTS:
{projects}

MEMORIES:
{memories}
"""


# ==================================================
# SAVE MEMORY
# ==================================================

def save_memory(
    category,
    memory_text
):

    try:

        with open(
            "memory/memories.txt",
            "r",
            encoding="utf-8"
        ) as f:

            content = (
                f.readlines()
            )

        updated_lines = []
        inserted = False

        for line in content:

            updated_lines.append(
                line
            )

            if (
                line.strip()
                ==
                f"[{category}]"
            ):

                updated_lines.append(
                    f"- {memory_text}\n"
                )

                inserted = True

        # category doesn't exist
        if not inserted:

            updated_lines.append(
                f"\n[{category}]\n"
            )

            updated_lines.append(
                f"- {memory_text}\n"
            )

        with open(
            "memory/memories.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.writelines(
                updated_lines
            )

        print(
            f"\n🧠 Memory saved "
            f"[{category}]: "
            f"{memory_text}"
        )

        return True

    except Exception as e:

        print(
            f"\nMemory save error: {e}"
        )

        return False


# ==================================================
# FORGET MEMORY
# ==================================================

def forget_memory(
    memory_text
):

    try:

        with open(
            "memory/memories.txt",
            "r",
            encoding="utf-8"
        ) as f:

            lines = (
                f.readlines()
            )

        updated_lines = []
        removed = False

        for line in lines:

            if (
                line.strip().startswith("-")
                and
                memory_text.lower()
                in line.lower()
            ):

                removed = True
                continue

            updated_lines.append(
                line
            )

        with open(
            "memory/memories.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.writelines(
                updated_lines
            )

        return removed

    except Exception as e:

        print(
            f"\nForget memory error: {e}"
        )

        return False


# ==================================================
# GET MEMORIES
# ==================================================

def get_memories():

    try:

        with open(
            "memory/projects.txt",
            "r",
            encoding="utf-8"
        ) as f:

            projects = (
                f.read()
            )

        with open(
            "memory/memories.txt",
            "r",
            encoding="utf-8"
        ) as f:

            memories = (
                f.read()
            )

        return f"""
PROJECTS:
{projects}

MEMORIES:
{memories}
"""

    except Exception as e:

        print(
            f"\nMemory read error: {e}"
        )

        return (
            "No memories found."
        )
# ==================================================
# HANDLE MEMORY COMMANDS
# ==================================================

def handle_memory_command(
    user_input
):

    user_input_lower = (
        user_input
        .lower()
        .strip()
    )

    # ==================================================
    # REMEMBER
    # ==================================================

    if user_input_lower.startswith(
        "remember"
    ):

        category = (
            "LONG_TERM_FACTS"
        )

        memory_text = ""

        if user_input_lower.startswith(
            "remember preference"
        ):

            category = (
                "PREFERENCES"
            )

            memory_text = (
                user_input
                .replace(
                    "remember preference",
                    ""
                )
                .replace(":", "")
                .strip()
            )

        elif user_input_lower.startswith(
            "remember task"
        ):

            category = (
                "TASKS"
            )

            memory_text = (
                user_input
                .replace(
                    "remember task",
                    ""
                )
                .replace(":", "")
                .strip()
            )

        elif user_input_lower.startswith(
            "remember project"
        ):

            category = (
                "PROJECTS"
            )

            memory_text = (
                user_input
                .replace(
                    "remember project",
                    ""
                )
                .replace(":", "")
                .strip()
            )

        else:

            memory_text = (
                user_input
                .replace(
                    "remember",
                    ""
                )
                .replace(":", "")
                .strip()
            )

        if not memory_text:

            return (
                True,
                "You forgot to tell me what to remember 😌"
            )

        success = (
            save_memory(
                category,
                memory_text
            )
        )

        if success:

            return (
                True,
                f"Got it. I'll remember that under {category.lower()}."
            )

        return (
            True,
            "Something went wrong while saving memory."
        )

    # ==================================================
    # FORGET
    # ==================================================

    if user_input_lower.startswith(
        "forget"
    ):

        memory_text = (
            user_input
            .replace(
                "forget",
                ""
            )
            .replace(":", "")
            .strip()
        )

        success = (
            forget_memory(
                memory_text
            )
        )

        if success:

            return (
                True,
                "Got it. I forgot that."
            )

        return (
            True,
            "I couldn't find anything matching that memory."
        )

    # ==================================================
    # MEMORY RECALL
    # ==================================================

    if (
        "what do you remember"
        in user_input_lower
    ):

        memories = (
            get_memories()
        )

        return (
            True,
            f"Here's what I remember.\n{memories}"
        )

    return (
        False,
        None
    )