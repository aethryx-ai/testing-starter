from typing import Any, Dict

from audit import build_audit_record
from guardrails import check_guardrails
from risk_checks import (
    check_accuracy,
    check_bias,
    check_data_leakage,
    check_hallucination,
    check_unsafe_content,
)


def evaluate_test_case(test_case: Dict[str, Any]) -> Dict[str, Any]:
    test_id = test_case["id"]
    prompt = test_case["prompt"]
    response = test_case["response"]
    expected_keywords = test_case.get("expected_keywords", [])
    risk_tags = test_case.get("risk_tags", [])

    guardrail = check_guardrails(response)
    risk_results = []

    if "accuracy" in risk_tags or "completeness" in risk_tags:
        risk_results.append(check_accuracy(response, expected_keywords).__dict__)

    if "hallucination" in risk_tags or "rag_grounding" in risk_tags:
        risk_results.append(check_hallucination(response, expected_keywords).__dict__)

    if "data_leakage" in risk_tags or "security" in risk_tags or "prompt_injection" in risk_tags:
        risk_results.append(check_data_leakage(response).__dict__)

    if "unsafe_content" in risk_tags:
        risk_results.append(check_unsafe_content(response).__dict__)

    if "bias" in risk_tags:
        risk_results.append(check_bias(response).__dict__)

    return build_audit_record(
        test_case_id=test_id,
        prompt=prompt,
        response=response,
        guardrail_result=guardrail.__dict__,
        risk_results=risk_results,
    )
