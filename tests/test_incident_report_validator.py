import unittest

from coded_tools.validate_incident_report import validate_incident_report

EVIDENCE = (
    "Synthetic test data: two failed logins and one successful login "
    "for demo_user from 192.0.2.10."
)


class IncidentReportValidatorTests(unittest.TestCase):

    def test_safe_report_passes(self):
        report = {
            "observed_facts": ["Two failed logins and one successful login."],
            "risk": "Undetermined",
            "confirmed_actions": [],
        }
        self.assertTrue(
            validate_incident_report(report, EVIDENCE)["valid"]
        )

    def test_unsupported_high_risk_is_rejected(self):
        report = {"risk": "High risk", "confirmed_actions": []}
        self.assertFalse(
            validate_incident_report(report, EVIDENCE)["valid"]
        )

    def test_completed_action_claim_is_rejected(self):
        report = {
            "confirmed_actions": ["Reviewed authentication logs"]
        }
        self.assertFalse(
            validate_incident_report(report, EVIDENCE)["valid"]
        )

    def test_empty_evidence_is_rejected(self):
        report = {"confirmed_actions": []}
        self.assertFalse(
            validate_incident_report(report, "")["valid"]
        )

    def test_invented_incident_id_is_rejected(self):
        report = {
            "incident_id": "SF-AI-2024-0720-FAILED_LOGINS_TEST_ACCOUNT",
            "confirmed_actions": [],
        }
        self.assertFalse(
            validate_incident_report(report, EVIDENCE)["valid"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
