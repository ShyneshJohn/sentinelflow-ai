import json
import re
from typing import Any


UNSUPPORTED_LABELS = re.compile(
    r"\b(?:low|medium|high|critical)\s+"
    r"(?:risk|severity|priority|likelihood|confidence|impact|urgency)\b",
    re.IGNORECASE,
)

INVENTED_ID_PATTERN = re.compile(
    r'"(?:incident|event)[\s_-]*id"\s*:\s*'
    r'"(?!TEST-\d+\b)[A-Z0-9][A-Z0-9_-]{8,}\b"',
    re.IGNORECASE,
)


def validate_incident_report(
    report: dict[str, Any],
    supplied_evidence: str,
) -> dict[str, Any]:
    """Basic prototype checks; not a complete security guarantee."""
    if not isinstance(report, dict):
        return {
            "valid": False,
            "errors": ["Report must be a JSON object."],
        }

    errors: list[str] = []
    rendered = json.dumps(report, ensure_ascii=False, default=str)

    if INVENTED_ID_PATTERN.search(rendered):
        errors.append("Potential unsupported incident or event ID.")

    if UNSUPPORTED_LABELS.search(rendered):
        errors.append("Potential unsupported risk/severity/priority label.")

    confirmed = report.get("confirmed_actions", [])

    if confirmed is None:
        confirmed = []

    if not isinstance(confirmed, list):
        errors.append("'confirmed_actions' must be a list.")
    elif confirmed:
        errors.append(
            "Confirmed actions require independently verified execution records."
        )

    if not supplied_evidence.strip():
        errors.append("No source evidence was supplied.")

    return {"valid": not errors, "errors": errors}


if __name__ == "__main__":
    evidence = "Synthetic test: two failed logins and one successful login."

    safe_report = {
        "observed_facts": ["Two failed logins and one successful login."],
        "risk": "Undetermined",
        "confirmed_actions": [],
    }

    unsafe_report = {
        "incident_id": "SF-AI-2024-0720-FAILED_LOGINS_TEST_ACCOUNT",
        "risk": "High risk",
        "confirmed_actions": ["Reviewed authentication logs"],
    }

    for name, report in [
        ("SAFE SAMPLE", safe_report),
        ("UNSAFE SAMPLE", unsafe_report),
    ]:
        result = validate_incident_report(report, evidence)
        print(f"\n{name}: {'PASS' if result['valid'] else 'REJECT'}")
        print(json.dumps(result, indent=2))
