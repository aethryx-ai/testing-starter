import json
from datetime import datetime, timezone
from typing import Any, Dict, List


def build_audit_record(
    test_case_id: str,
    prompt: str,
    response: str,
    guardrail_result: Dict[str, Any],
    risk_results: List[Dict[str, Any]],
) -> Dict[str, Any]:
    overall_pass = guardrail_result["passed"] and all(r["passed"] for r in risk_results)

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "test_case_id": test_case_id,
        "prompt": prompt,
        "response": response,
        "guardrail_result": guardrail_result,
        "risk_results": risk_results,
        "overall_pass": overall_pass,
    }


def save_audit_log(records: List[Dict[str, Any]], path: str = "audit_log.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
