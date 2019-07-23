import argparse
import os
import datetime
from PIL import Image
from shutil import copyfile

supported_file_extensions = [
    "jpg"
]


def get_arg_parser():
    parser = argparse.ArgumentParser(description="Image file separator")
    parser.add_argument('-t', '--target_folder', required=True, type=str, help="Target folder")
    parser.add_argument('-s', '--source_folder', required=True, type=str, help="Source folder")
    return parser


def get_file_names_dates(source_folder: str) -> list:
    a = []
    for s in os.listdir(source_folder):
        filename, fileextension = os.path.splitext(s)
        if os.path.isfile(os.path.join(source_folder, s)) and fileextension[1:].lower() in supported_file_extensions:
            d_s = Image.open(os.path.join(source_folder, s))._getexif()[36867]
            a.append((s, datetime.datetime.strptime(d_s, "%Y:%m:%d %H:%M:%S")))
    return a


def copy_files(files_dates: list, target_folder: str, source_folder: str) -> None:
    for name, date in files_dates:
        date_str = "{:02d}.{:02d}.".format(date.month, date.day)
        if not os.path.isdir(os.path.join(target_folder, date_str)):
            os.makedirs(os.path.join(target_folder, date_str))
        copyfile(os.path.join(source_folder, name), os.path.join(target_folder, date_str, name))


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    file_dates = get_file_names_dates(args.source_folder)
    copy_files(file_dates, args.target_folder, args.source_folder)
