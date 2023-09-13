import os
import sys
import json

arg = sys.argv
if len(arg)!=2:
    raise Exception("Please pass the json file")
json_file = arg[1]
if os.path.exists(json_file):
    file = open(json_file, "r")
    json.load(file)
    file.close
    print("The json file is valid!")
