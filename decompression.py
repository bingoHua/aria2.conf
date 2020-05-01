#!/usr/bin/env python3
import os
import zipfile
from unrar import rarfile


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
	print('unzip success!!')
    else:
        print('This is not zip')


def operation(path):
    print(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            file_extension = os.path.splitext(name)[1]
            if file_extension == ".zip":
                print("check file " + os.path.join(root, name) + ".aria2 exists")
                if os.path.exists(os.path.join(root, name) + ".aria2") is not True:
                    print("unzip file=" + os.path.join(root, name))
                    print("test log")
                    unzip_file(os.path.join(root, name), os.path.join(root, os.path.splitext(name)[0]))
                    print("delete file:" + os.path.join(name))
                    print("current file path" + os.path.join(root, os.path.splitext(name)[0]))
                    os.remove(os.path.join(root, name))
                else:
                    print(name + " dose not download complete.")
            elif file_extension == ".rar":
                print("check file " + os.path.join(root, name) + ".aria2 exists")
                if os.path.exists(os.path.join(root, name) + ".aria2") is not True:
                    rar = rarfile.RarFile(os.path.join(root, name))
                    rar.extractall(os.path.join(root, os.path.splitext(name)[0]))
                    print("unrar file:" + os.path.join(root, name))
                    os.remove(os.path.join(root, name))
                    print("delete file:" + name)
                else:
                    print(name + "dose not download complete.")
