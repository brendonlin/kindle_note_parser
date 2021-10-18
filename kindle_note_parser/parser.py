# -*-coding:utf-8-*-
"""
Convert kindle html note to markdown format
"""
import bs4
import os
import re
import urllib.parse


def format_text(text, is_remove_space=False):
    new_words = []
    EMPTY_WORD = " "
    if is_remove_space:
        for word in re.split(r"\s+", text):
            new_words.append(word)
            if re.match("^[a-zA-Z]+$", word):
                new_words.append(EMPTY_WORD)
        return "".join(new_words)
    else:
        return text


def parse_text_soup(textSoup: bs4.BeautifulSoup, is_remove_space=False):
    section_head = textSoup.find("h2", attrs={"class": "sectionHeading"})
    section_head_text = ""
    if section_head is not None:
        section_head_text = f"## {format_text(section_head.text, is_remove_space)}"
        section_head.replace_with("")
    note_head = textSoup.find("h3", attrs={"class": "noteHeading"})
    note_head_text = ""
    if note_head is not None:
        note_head_text = f"**{format_text(note_head.text, is_remove_space)}**"
        note_head.replace_with("")
    content_text = format_text(textSoup.text, is_remove_space)
    return "\n\n".join(
        [x for x in [content_text, section_head_text, note_head_text] if x != ""]
    )


def parse(path, save_dir, is_remove_space=False):
    loc = "file:///"
    fp = urllib.parse.unquote(path.replace(loc, ""))
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    title = os.path.basename(fp).split(".")[0]
    save_fp = os.path.join(save_dir, f"{title}.txt")
    soup = bs4.BeautifulSoup(html, features="html.parser")
    note_text_list = [
        parse_text_soup(x, is_remove_space)
        for x in soup.findAll("div", attrs={"class": "noteText"})
    ]
    note_text = "\n\n".join(note_text_list)
    with open(save_fp, "w", encoding="utf-8") as f:
        f.write(note_text)
    return save_fp
