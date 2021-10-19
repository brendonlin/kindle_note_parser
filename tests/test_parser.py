import pytest
from kindle_note_parser import parser


@pytest.mark.parametrize(
    "input,expected",
    [("你 看， 这是 我 买的 小说 《 War and Peace》", "你看，这是我买的小说《War and Peace》")],
)
def test_format_text(input, expected):
    assert parser._format_text(input, remove_space=True) == expected
