import json
from typing import Any
from neuro_san.interfaces.coded_tool import CodedTool
from coded_tools.validate_incident_report import validate_incident_report


class IncidentReportValidatorTool(CodedTool):
    """Validate a proposed incident report."""

    def invoke(self, args: dict[str, Any], sly_data: dict[str, Any]) -> str:
        raw_report = args.get("report_json", "")
        evidence = args.get("supplied_evidence", "")

        if not isinstance(raw_report, str):
            return json.dumps({
                "valid": False,
                "errors": ["report_json must be a JSON string."]
            })

        try:
            report = json.loads(raw_report)
        except (json.JSONDecodeError, TypeError):
            return json.dumps({
                "valid": False,
                "errors": ["Invalid report JSON."]
            })

        result = validate_incident_report(report, evidence)
        return json.dumps(result, ensure_ascii=False)
