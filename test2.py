from os import listdir
from os.path import isfile, join, getsize
from itertools import groupby

directory = "C:/Users/kicur/Desktop/Data Science/Python_exercises"
onlyfiles = [f for f in listdir(directory)]

def files_in_dir(directory):
   files = [f for f in listdir(directory) if isfile(join(directory, f))]
   return sorted(files)

def get_files_with_sizes(directory):
    file_size = []
    for file in files_in_dir(directory):
        size = getsize(join(directory, file))
        file_size.append((size, file))
    return file_size

def sorted_by_size(files_dict):
    dict_sorted = {}
    for key, value in files_dict.items():
        sorted_by_size = sorted(value, key=lambda tup: tup[0])
        dict_sorted[key] = sorted_by_size
    return dict_sorted

files_with_sizes = get_files_with_sizes(directory)

files_dict = {key: list(ele) for key, ele in groupby(files_with_sizes, key=lambda x: x[1][0:3])}
print(sorted_by_size(files_dict))


