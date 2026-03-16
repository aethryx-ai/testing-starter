from dataclasses import dataclass
from typing import List


@dataclass
class GuardrailResult:
    passed: bool
    violations: List[str]


BLOCKED_PATTERNS = [
    "admin password",
    "supersecret123",
    "api key",
    "ssn",
    "credit card number",
]

UNSAFE_PATTERNS = [
    "one group is naturally better",
    "hate",
    "kill",
    "violence",
]


def check_guardrails(response: str) -> GuardrailResult:
    text = response.lower()
    violations: List[str] = []

    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            violations.append(f"Sensitive data disclosure detected: '{pattern}'")

    for pattern in UNSAFE_PATTERNS:
        if pattern in text:
            violations.append(f"Unsafe content detected: '{pattern}'")

    return GuardrailResult(
        passed=len(violations) == 0,
        violations=violations,
    )
