import os
import datetime
from PIL import Image
from shutil import copyfile

source_folder = 'c:\\Users\\frany\\Pictures\\2019.07.05 - 17 Norvégia'
target_folder = 'c:\\Users\\frany\\Pictures\\Norway'

supported_file_extensions = [
    "jpg"
]


a = []
for s in os.listdir(source_folder):
    filename, fileextension = os.path.splitext(s)
    if os.path.isfile(os.path.join(source_folder, s)) and fileextension[1:].lower() in supported_file_extensions:
        d_s = Image.open(os.path.join(source_folder, s))._getexif()[36867]
        a.append((s, datetime.datetime.strptime(d_s, "%Y:%m:%d %H:%M:%S")))

separated = {}
for name, date in a:
    date_str = "{:02d}.{:02d}.".format(date.month, date.day)
    if not os.path.isdir(os.path.join(target_folder, date_str)):
        os.makedirs(os.path.join(target_folder, date_str))
    copyfile(os.path.join(source_folder, name), os.path.join(target_folder, date_str, name))

print(a)

