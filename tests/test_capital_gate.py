"""v3 interruption guards use the original synthetic FULL gate fixture."""
import unittest
from pathlib import Path
from test_closed_loop import Fixture, cl


class CapitalGateTests(Fixture):
    def update_evidence(self, spec, **changes):
        value = cl.read_json(spec["evidence"])
        value.update(changes)
        cl.write_json(spec["evidence"], value)
        self.refresh_gate_snapshot(spec)

    def test_active_stop_loss_blocks_an_otherwise_passing_full_gate(self):
        spec = self.gate_fixture()
        self.update_evidence(spec, capital_state="STOP_LOSS")
        with self.assertRaisesRegex(cl.Invalid, "STOP_LOSS"):
            cl.gate(spec)

    def test_invalid_capital_state_is_not_a_legacy_omission(self):
        for state in (None, True, [], {}, "", "PASS", "stop_loss"):
            with self.subTest(state=state):
                spec = self.gate_fixture()
                self.update_evidence(spec, capital_state=state)
                with self.assertRaisesRegex(cl.Invalid, "capital_state"):
                    cl.gate(spec)

    def test_reassessment_cannot_be_only_a_claim_or_unknown_reference(self):
        for refs in (None, [], "RAW", ["UNKNOWN"], [None], ["RAW", "RAW"]):
            with self.subTest(refs=refs):
                spec = self.gate_fixture()
                self.update_evidence(spec, capital_state="REASSESSED", reassessment_evidence=refs)
                with self.assertRaisesRegex(cl.Invalid, "[Rr]eassessment"):
                    cl.gate(spec)

    def test_reviewed_reassessment_allows_legacy_checks_to_continue(self):
        spec = self.gate_fixture()
        evidence = cl.read_json(spec["evidence"])
        record = self.root / "reassessment.txt"
        record.write_text("Synthetic root cause: incompatible input. New experiment: normalize once, then retest.\n")
        evidence["artifacts"].append(self.evidence_record(record, "DIRECTION"))
        evidence.update(capital_state="REASSESSED", reassessment_evidence=["DIRECTION"])
        cl.write_json(spec["evidence"], evidence)
        old = cl.read_json(spec["bundle"])
        bundle = cl.prepare(self.spec([Path(r["source_file"])
                                      for r in old["manifest"]["included"]] + [record]))
        cl.write_json(spec["bundle"], bundle)
        self.refresh_gate_snapshot(spec)
        self.assertEqual(cl.gate(spec)["status"], "READY_FOR_USER_ACCEPTANCE")
        spec["direction_reassessment_pending"] = True
        with self.assertRaisesRegex(cl.Invalid, "Direction reassessment"):
            cl.gate(spec)

    def test_unreviewed_reassessment_artifact_is_rejected(self):
        spec = self.gate_fixture()
        evidence = cl.read_json(spec["evidence"])
        record = self.root / "reassessment.txt"
        record.write_text("Synthetic diagnostic evidence not sent to the reviewer.\n")
        evidence["artifacts"].append(self.evidence_record(record, "DIRECTION"))
        self.update_evidence(spec, **evidence, capital_state="REASSESSED", reassessment_evidence=["DIRECTION"])
        with self.assertRaisesRegex(cl.Invalid, "not included for review"):
            cl.gate(spec)

    def test_explicit_continue_preserves_the_original_full_gate(self):
        spec = self.gate_fixture()
        self.update_evidence(spec, capital_state="CONTINUE")
        self.assertEqual(cl.gate(spec)["status"], "READY_FOR_USER_ACCEPTANCE")


if __name__ == "__main__":
    unittest.main()
