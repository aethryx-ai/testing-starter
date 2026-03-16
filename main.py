import json
from typing import Any, Dict, List

from audit import save_audit_log
from evaluator import evaluate_test_case


def load_test_cases(path: str = "test_cases.json") -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_summary(records: List[Dict[str, Any]]) -> None:
    total = len(records)
    passed = sum(1 for r in records if r["overall_pass"])
    failed = total - passed

    print("\nAETHRYX TESTING SUMMARY")
    print("=" * 40)
    print(f"Total test cases: {total}")
    print(f"Passed:           {passed}")
    print(f"Failed:           {failed}")
    print("=" * 40)

    for record in records:
        print(f"\n[{record['test_case_id']}] overall_pass={record['overall_pass']}")
        if not record["guardrail_result"]["passed"]:
            print("  Guardrail violations:")
            for violation in record["guardrail_result"]["violations"]:
                print(f"   - {violation}")

        for result in record["risk_results"]:
            print(
                f"  - {result['check_name']}: passed={result['passed']} "
                f"score={result['score']:.2f} details={result['details']}"
            )


def main() -> None:
    test_cases = load_test_cases()
    records = [evaluate_test_case(tc) for tc in test_cases]
    save_audit_log(records)
    print_summary(records)


if __name__ == "__main__":
    main()
