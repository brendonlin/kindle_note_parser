import pytest
from kindle_note_parser import parser
import bs4
from bs4.element import NavigableString
import re


@pytest.mark.parametrize(
    "input,expected",
    [("你 看， 这是 我 买的 小说 《 War and Peace》", "你看，这是我买的小说《War and Peace》")],
)
def test_format_text(input, expected):
    assert parser.format_text(input, remove_space=True) == expected


def test_new_parser():
    test_html_path = "tests/data/kindel_html_sample_cn_mobile.html"
    # test_html_path = "tests/data/kindel_html_sample_cn.html"
    soup = parser._read(test_html_path)
    doc = parser._transform(soup=soup)
    print(doc)
    assert doc.startswith(f"# ")
    assert doc.count("##") > 1
