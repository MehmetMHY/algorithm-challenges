import pickle
import subprocess
import re
import os

# save basic python variables/data to a pickle file (.p)
def pickle_save(filename, data):
    if filename[-2:] == ".p":
        filename = filename
    else:
        filename = str(filename + ".p")

    with open(filename, 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    
    print("Saved data to file: " + filename)

# load a pickle file to python instance (.p)
def pickle_load(filename):
    data = {}
    with open(filename, 'rb') as fp:
        data = pickle.load(fp)
    
    print("Loaded File: ", data)

    return data

# get current pwd using python
def get_current_pwd():
    output2 = subprocess.check_output("pwd", shell=True)
    pwd_path = str(output2).replace("b'", "")
    pwd_path = pwd_path[:-3]
    pwd_path = pwd_path + "/"

    return pwd_path

# get a list of all the pickle file(s) paths
def find_all_pickle_files(path):
    path = str(path)

    command = "find $(pwd) -type f | grep '.pickle'"

    if(os.path.isfile(path) and path != "." and path != "./"):
        command = "find " + path + " -type f | grep '.pickle'"

    output = subprocess.check_output(command, shell=True)

    pickle_files = str(output).replace("b'", "")
    pickle_files = pickle_files[:-3]
    pickle_files = pickle_files.split("\\n")

    pwd_path = get_current_pwd()

    for i in range(len(pickle_files)):
        pickle_files[i] = pickle_files[i].replace(pwd_path, "./")

    return pickle_files


