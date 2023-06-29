import os
from os.path import abspath, join, getsize
print("Enter_folder_path")
path = input()
print(f"You've entered {path} as folder path")
sizes = {}

for top_dir, directories, files in os.walk(path):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
items_displayed = 0
for f_path,size in sorted(sizes.items(),key=lambda x : x[1],reverse =True):
    if items_displayed > 20:
        break
    print(f"Size:{size}, File: {f_path}")
    items_displayed += 1