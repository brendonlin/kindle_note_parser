# -*-coding:utf-8-*-
"""
Convert kindle html note to markdown format
"""
import os
import re
import urllib.parse
import bs4
from bs4.element import NavigableString


def parse(html_path, output_dir, remove_space=False):
    input_path = _format_html_path(html_path)
    title = os.path.basename(input_path).split(".")[0]
    soup = _read(html_path)
    doc = _transform(soup, remove_space)
    output_path = _output(doc, title, output_dir)
    return output_path


def _read(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = bs4.BeautifulSoup(html, features="html.parser")
    return soup


def _output(doc, title, output_dir):
    output_path = os.path.join(output_dir, f"{title}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return output_path


def _transform(soup, remove_space=False):
    pattern = re.compile("(noteText)|(noteHeading)|(sectionHeading)|(bookTitle)")
    parts = soup.find_all(class_=pattern)
    text_list = []

    for part in parts:
        text = "".join([x for x in part.children if isinstance(x, NavigableString)])
        text = format_text(text, remove_space=remove_space)
        classes = part.attrs.get("class")
        if "noteHeading" in classes:
            text = f"**{text}**"
        elif "sectionHeading" in classes:
            text = f"## {text}"
        elif "bookTitle" in classes:
            text = f"# {text}"
        text_list.append(text)
    doc = "\n\n".join(text_list)
    return doc


def format_text(text, remove_space=False):
    _text = re.sub(r"(^\n)|(\n$)", "", text)
    if remove_space:
        new_words = []
        EMPTY_WORD = " "
        for word in re.split(r"\s+", _text):
            new_words.append(word)
            if re.match("^[a-zA-Z]+$", word):
                new_words.append(EMPTY_WORD)
        return "".join(new_words)
    else:
        return _text


def _format_html_path(path):
    loc = "file:///"
    fp = urllib.parse.unquote(path.replace(loc, ""))
    return fp
