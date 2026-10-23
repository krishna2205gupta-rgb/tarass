"""Tests for TARA's Ponytail-style QA reporting."""
from app.agents.qa import PonytailFinding, QAReport, analyze_code_qa_fallback


def test_qa_report_keeps_ponytail_findings_optional():
    report = QAReport(passed=True, summary="ok", issues=[])
    assert report.ponytail_findings == []


def test_ponytail_finding_has_expected_fields():
    finding = PonytailFinding(
        tag="stdlib",
        file_path="utils.py",
        finding="A custom timestamp formatter duplicates datetime functionality.",
        suggested_replacement="Use datetime.isoformat().",
        risk_note="Verify timezone behavior and existing output format.",
    )
    assert finding.tag == "stdlib"
    assert finding.file_path == "utils.py"


def test_fallback_does_not_invent_ponytail_findings():
    report = analyze_code_qa_fallback({"sample.py": "def hello():\n    return 'hello'\n"})
    assert report.ponytail_findings == []
    assert "full repository-wide" in report.summary
