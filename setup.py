from setuptools import find_packages, setup

setup(
    name="kindle_note_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Click", "bs4"],
    entry_points={
        "console_scripts": [
            "kindle-p = kindle_note_parser.app:main",
        ],
    },
)
