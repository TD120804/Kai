"""
==================================================
Kai Security Sanitizer
==================================================

This module cleans incoming user input after it
has passed validation.

Responsibilities:
- Remove unnecessary whitespace
- Normalize casing
- Remove control characters
- Normalize repeated punctuation
- Keep user intent unchanged

This module NEVER rejects input.
Only transforms it.
"""

import re


class InputSanitizer:

    @staticmethod
    def sanitize(message: str) -> str:

        # ------------------------------------------
        # Remove leading/trailing whitespace
        # ------------------------------------------

        message = message.strip()

        # ------------------------------------------
        # Replace tabs/newlines with spaces
        # ------------------------------------------

        message = re.sub(
            r"[\t\r\n]+",
            " ",
            message
        )

        # ------------------------------------------
        # Collapse multiple spaces
        # ------------------------------------------

        message = re.sub(
            r"\s+",
            " ",
            message
        )

        # ------------------------------------------
        # Remove NULL bytes
        # ------------------------------------------

        message = message.replace(
            "\x00",
            ""
        )

        # ------------------------------------------
        # Remove other control characters
        # ------------------------------------------

        message = "".join(

            ch

            for ch in message

            if ch.isprintable()

        )

        # ------------------------------------------
        # Normalize repeated punctuation
        # ------------------------------------------

        message = re.sub(
            r"!{2,}",
            "!",
            message
        )

        message = re.sub(
            r"\?{2,}",
            "?",
            message
        )

        message = re.sub(
            r"\.{3,}",
            "...",
            message
        )

        # ------------------------------------------
        # Normalize repeated commas
        # ------------------------------------------

        message = re.sub(
            r",{2,}",
            ",",
            message
        )

        return message