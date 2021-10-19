from click.testing import CliRunner
from kindle_note_parser import app
import os
import tempfile
import shutil


def test_main():
    test_file_name = "kindel_html_sample_cn.html"
    test_source_dir = tempfile.TemporaryDirectory()
    shutil.copy(f"tests/data/{test_file_name}", test_source_dir.name)
    test_output_dir = tempfile.TemporaryDirectory()
    runner = CliRunner()
    result = runner.invoke(
        app.main,
        [
            test_file_name,
            "--source_dir",
            test_source_dir.name,
            "--output_dir",
            test_output_dir.name,
        ],
    )
    assert result.exit_code == 0
