from os import chdir, path
import subprocess

DIRS = ("train", "validation", "test")
DEBUG = True

def print_msg(msg, isDebug=False):
    if not isDebug:
        print(msg)
    elif isDebug and DEBUG:
        print(msg)

def get_classes(classes_file):
    with open(classes_file) as f:
        return [l.strip().lower().replace(" ", "_") for l in f.readlines()]

######## Move annotation files to parent folders ########

chdir(path.join("OIDv6", "multidata"))

for DIR in DIRS:
    if not path.isdir(DIR):
        print_msg(f"Directory {DIR} doesn't exists", True)
        continue
    subprocess.run(["mv", DIR + "/labels/*", DIR + "/"])
    print_msg(f"Labels from directory {DIR} moved to parent folder")

######## Change Labels inside annotation files to Label Indexes  ########

classes = get_classes(path.join("..", "..", "classes.txt"))
num_clases = len(classes)
