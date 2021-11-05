import os

path = os.getcwd()

index = path.find("99z-Capstone_Team_Project-202210-05-martinms-fletchj1-aquaslc")
for k in range(len(path) - index + 2):
    path = path.removeprefix(path[0])

if path == "99z-Capstone_Team_Project-202210-05-martinms-fletchj1-aquaslc":
    ide = "vscode"
else:
    ide = "pycharm"

def thing():
    pass

def file(file):
    file = str(file)
    if ide == "vscode":
        location = "02_Model_View_Controller_starting_code/" + file
    else:
        location = file
    return location
