# -*-coding:utf-8-*-
"""
Convert kindle html note to markdown format
"""
import os
import re
import urllib.parse
import bs4


def parse(html_path, output_dir, remove_space=False):
    fp = _parse_path(html_path)
    html = _read_html(fp)
    title = os.path.basename(fp).split(".")[0]
    ouput_path = os.path.join(output_dir, f"{title}.txt")
    soup = bs4.BeautifulSoup(html, features="html.parser")

    output_texts = [
        _get_output_text(x, remove_space)
        for x in soup.findAll("div", attrs={"class": "noteText"})
    ]

    header = f"# {title}"
    output_texts.insert(0, header)
    output_doc = "\n\n".join(output_texts)
    with open(ouput_path, "w", encoding="utf-8") as f:
        f.write(output_doc)
    return ouput_path


def _format_text(text, remove_space=False):
    new_words = []
    EMPTY_WORD = " "
    if remove_space:
        for word in re.split(r"\s+", text):
            new_words.append(word)
            if re.match("^[a-zA-Z]+$", word):
                new_words.append(EMPTY_WORD)
        return "".join(new_words)
    else:
        return text


def _get_output_text(textSoup: bs4.BeautifulSoup, remove_space=False):
    section_head = textSoup.find("h2", attrs={"class": "sectionHeading"})
    section_head_text = ""
    if section_head is not None:
        section_head_text = f"## {_format_text(section_head.text, remove_space)}"
        section_head.replace_with("")
    note_head = textSoup.find("h3", attrs={"class": "noteHeading"})
    note_head_text = ""
    if note_head is not None:
        note_head_text = f"**{_format_text(note_head.text, remove_space)}**"
        note_head.replace_with("")
    content_text = _format_text(textSoup.text, remove_space)
    return "\n\n".join(
        [x for x in [content_text, section_head_text, note_head_text] if x != ""]
    )


def _parse_path(path):
    loc = "file:///"
    fp = urllib.parse.unquote(path.replace(loc, ""))
    return fp


def _read_html(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    return html
