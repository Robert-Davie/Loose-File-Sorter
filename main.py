import os
import sys
import shutil

if len(sys.argv) < 2:
    raise Exception("no folder location given")

given_folder_location = sys.argv[1]

print(f"folder location given: {given_folder_location}")
response = input("proceed[y/n]")

if response != "y":
    print("program terminated")
    exit()


if not os.path.isdir(given_folder_location):
    raise Exception("folder given does not exist")


list_of_files = os.listdir(given_folder_location)
list_of_file_types = set()
for file in list_of_files:
    extension = file.split(".")[-1]
    list_of_file_types.add(extension)

new_folder_location = f"{given_folder_location}\\..\\SortedFiles"

if os.path.isdir(new_folder_location):
    raise Exception(
        "SortedFiles folder already present, remove this folder and rerun program"
    )
os.mkdir(new_folder_location)

for file_type in list_of_file_types:
    os.mkdir(f"{new_folder_location}\\{file_type}")

print("-" * 40)
print("file copies")

for file in list_of_files:
    this_file_type = file.split(".")[-1]
    source_address = f"{given_folder_location}\\{file}"
    destination_address = f"{new_folder_location}\\{this_file_type}"
    print(f"{file}:".rjust(40), "successful")

    shutil.copy(source_address, destination_address)

print("all files copied successfully to new folders")
print("program finished")
