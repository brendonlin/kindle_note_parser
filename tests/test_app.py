from click.testing import CliRunner
from kindle_note_parser import app


def test_main():
    runner = CliRunner()
    result = runner.invoke(app.main, ["资本论（第一卷）-笔记本.html", "-v", "-r"])
