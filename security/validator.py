"""
==================================================
Kai Security Validator
==================================================

This module validates every incoming request before
it reaches Kai's brain.

Responsibilities:
- Validate input type
- Validate input length
- Reject empty requests
- Reject oversized requests
- Reject malformed requests
- Flag suspicious content

This module DOES NOT sanitize input.
It only decides whether input is acceptable.
"""

from dataclasses import dataclass
from typing import Optional
import re


# ==================================================
# CONFIGURATION
# ==================================================

MAX_MESSAGE_LENGTH = 5000

MIN_MESSAGE_LENGTH = 1


# ==================================================
# RESULT OBJECT
# ==================================================

@dataclass
class ValidationResult:

    valid: bool

    reason: Optional[str] = None


# ==================================================
# VALIDATOR
# ==================================================

class InputValidator:

    @staticmethod
    def validate(message) -> ValidationResult:

        # ------------------------------------------
        # None
        # ------------------------------------------

        if message is None:

            return ValidationResult(
                False,
                "Message is None."
            )

        # ------------------------------------------
        # Type
        # ------------------------------------------

        if not isinstance(message, str):

            return ValidationResult(
                False,
                "Message must be text."
            )

        # ------------------------------------------
        # Remove whitespace
        # ------------------------------------------

        message = message.strip()

        # ------------------------------------------
        # Empty
        # ------------------------------------------

        if len(message) < MIN_MESSAGE_LENGTH:

            return ValidationResult(
                False,
                "Message cannot be empty."
            )

        # ------------------------------------------
        # Too long
        # ------------------------------------------

        if len(message) > MAX_MESSAGE_LENGTH:

            return ValidationResult(
                False,
                f"Message exceeds "
                f"{MAX_MESSAGE_LENGTH} characters."
            )

        # ------------------------------------------
        # Null bytes
        # ------------------------------------------

        if "\x00" in message:

            return ValidationResult(
                False,
                "Invalid characters detected."
            )

        # ------------------------------------------
        # Excessive repetition
        # ------------------------------------------

        if re.search(r"(.)\1{99,}", message):

            return ValidationResult(
                False,
                "Suspicious repeated characters."
            )

        # ------------------------------------------
        # Passed
        # ------------------------------------------

        return ValidationResult(True)