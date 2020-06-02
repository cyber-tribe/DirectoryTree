import glob
import os
import sys
import json

def getDir(path):
    filelist = glob.glob(path+'/*')
    dir = list()
    child = None
    for file in filelist:
        # print(file)
        if file != '.' and file != '..':
            if os.path.isdir(file):
                child = getDir(file)
                if child != None:
                    # 子を持つディレクトリ
                    print(1)
                    dir.append({"name":file.split('\\')[-1], "children":child})
                else:
                    # 子を待たないディレクトリ
                    print(2)
                    dir.append({"name":file.split('\\')[-1]})
            else:
                print(3)
                dir.append({"name":file.split('\\')[-1], "file":os.path.splitext(file)[1][1:]})
    return dir

def generate_json(path):
    with open('directory.json', mode='w') as f:
        f.write(json.dumps(getDir(path)))

if __name__ == '__main__':
    args = sys.argv
    if len(args)!=2:
        print("This program takes the path of directory.")
        exit(1)
    else:
        generate_json(sys.argv[1])
        print("Generated JSON.")
