# KINDLE NOTE PARSER

A tool for converting Kindle HTML notes to Markdown format.

一个用于将 Kindle 的 HTML 笔记转换为 Markdown 格式的工具。

## Usage

```
kindle-p.exe --help
Usage: kindle-p [OPTIONS] FILE_NAME

Options:
  --source_dir TEXT   The source directory of the file, the
                      default is the Documents directory.
  --save_dir TEXT     The file storage directory, the
                      default is the Documents directory
  -r, --remove_space  Delete the spaces between words,
                      which is very suitable for languages
                      that are not separated by spaces,
                      such as Chinese.
  -v, --view_result   Whether to automatically open after
                      processing
  --help              Show this message and exit.
```

## Example

For English notes under "Documents"

```
kindle-p note.html -v
```

For Chinese notes under "Documents",

```
kindle-p note.html -vr
```
