"""Unit tests for the Markdown table validator."""
from __future__ import annotations

import unittest

from scripts.validation.validate_markdown_tables import table_errors


class MarkdownTableValidatorTests(unittest.TestCase):
    def test_valid_table_with_outer_pipes(self) -> None:
        text = "| ID | Expected result |\n| --- | --- |\n| TC-01 | Login succeeds |"
        self.assertEqual(table_errors(text), [])

    def test_valid_table_without_outer_pipes(self) -> None:
        text = "ID | Expected result\n--- | ---\nTC-01 | Login succeeds"
        self.assertEqual(table_errors(text), [])

    def test_blank_header_cell_is_reported(self) -> None:
        text = "| ID |  | Rule |\n| --- | --- | --- |\n| TC-01 | x | BR-01 |"
        errors = table_errors(text)
        self.assertTrue(any("blank header cell" in error for error in errors))

    def test_header_separator_cell_count_mismatch_is_reported(self) -> None:
        text = "| ID Objective Rule trace | Expected |\n| --- | --- | --- |\n| TC-01 | x | BR-01 |"
        errors = table_errors(text)
        self.assertTrue(any("header has 2 cell(s), separator has 3" in error for error in errors))

    def test_data_row_cell_count_mismatch_is_reported(self) -> None:
        text = "| ID | Expected |\n| --- | --- |\n| TC-01 | x | extra |"
        errors = table_errors(text)
        self.assertTrue(any("table row has 3 cell(s); expected 2" in error for error in errors))

    def test_escaped_pipe_is_not_a_delimiter(self) -> None:
        text = r"| ID | Description |\n| --- | --- |\n| TC-01 | literal \\| pipe |"
        self.assertEqual(table_errors(text), [])

    def test_fenced_code_block_is_ignored(self) -> None:
        text = "```markdown\n| A | B |\n| --- | --- | --- |\n```"
        self.assertEqual(table_errors(text), [])

    def test_table_after_non_table_pipe_text_is_detected(self) -> None:
        text = "Intro\nA | B\n--- | ---\nx | y"
        self.assertEqual(table_errors(text), [])


if __name__ == "__main__":
    unittest.main()
