import os
import click
from . import parser


@click.command()
@click.argument("file_name")
@click.option(
    "--source_dir",
    type=str,
    help="The source directory of the file, the default is the Documents directory.",
)
@click.option(
    "--output_dir",
    type=str,
    help="The file storage directory, the default is the Documents directory ",
)
@click.option(
    "--remove_space",
    "-r",
    is_flag=True,
    help="Delete the spaces between words, which is very suitable for languages that are not separated by spaces, such as Chinese.",
)
@click.option(
    "--view_result",
    "-v",
    is_flag=True,
    help="Whether to automatically open after processing ",
)
def main(file_name, source_dir, output_dir, remove_space: bool, view_result: bool):
    if source_dir is None:
        os.path.join(os.path.expanduser("~"), "Documents")
    else:
        _source_dir = source_dir
    if output_dir is None:
        _output_dir = os.path.join(os.path.expanduser("~"), "Documents")
    else:
        _output_dir = output_dir
    source_file_path = os.path.join(_source_dir, file_name)
    save_fp = parser.html_to_doc(
        source_file_path, _output_dir, remove_space=remove_space
    )
    if view_result:
        os.startfile(save_fp)


if __name__ == "__main__":
    main()
