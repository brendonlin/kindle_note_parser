# -*-coding:utf-8-*-
"""
Convert kindle html note to markdown format
"""
import os
import re
import urllib.parse
import bs4


def parse(html_path, output_dir, remove_space=False):
    input_path = format_html_path(html_path)
    title = os.path.basename(input_path).split(".")[0]
    doc = html_to_doc(html_path, title, remove_space)
    output_path = output(doc, title, output_dir)
    return output_path


def html_to_doc(html_path, title, remove_space=False):
    html = read_html(html_path)
    soup = bs4.BeautifulSoup(html, features="html.parser")
    output_texts = [
        get_output_text(x, remove_space)
        for x in soup.findAll("div", attrs={"class": "noteText"})
    ]
    header = f"# {title}"
    output_texts.insert(0, header)
    output_doc = "\n\n".join(output_texts)
    return output_doc


def output(doc, title, output_dir):
    output_path = os.path.join(output_dir, f"{title}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return output_path


def format_text(text, remove_space=False):
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


def get_output_text(textSoup: bs4.BeautifulSoup, remove_space=False):
    section_head = textSoup.find("h2", attrs={"class": "sectionHeading"})
    section_head_text = ""
    if section_head is not None:
        section_head_text = f"## {format_text(section_head.text, remove_space)}"
        section_head.replace_with("")
    note_head = textSoup.find("h3", attrs={"class": "noteHeading"})
    note_head_text = ""
    if note_head is not None:
        note_head_text = f"**{format_text(note_head.text, remove_space)}**"
        note_head.replace_with("")
    content_text = format_text(textSoup.text, remove_space)
    return "\n\n".join(
        [x for x in [content_text, section_head_text, note_head_text] if x != ""]
    )


def format_html_path(path):
    loc = "file:///"
    fp = urllib.parse.unquote(path.replace(loc, ""))
    return fp


def read_html(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    return html
