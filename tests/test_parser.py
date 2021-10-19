import pytest
from kindle_note_parser import parser


@pytest.mark.parametrize(
    "input,expected",
    [("你 看， 这是 我 买的 小说 《 War and Peace》", "你看，这是我买的小说《War and Peace》")],
)
def test_format_text(input, expected):
    assert parser.format_text(input, remove_space=True) == expected


def test_html_to_doc():
    test_html_path = "tests/data/kindel_html_sample_cn.html"
    title = "kindel_html_sample_cn"
    doc = parser.html_to_doc(html_path=test_html_path, title=title)
    assert doc.startswith(f"# {title}")
    assert doc.count("##") > 1
