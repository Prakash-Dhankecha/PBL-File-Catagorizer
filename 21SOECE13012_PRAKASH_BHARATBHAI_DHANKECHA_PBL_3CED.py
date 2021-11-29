import os
import shutil
from tkinter import *
from tkinter.filedialog import askdirectory


def source_path():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    source_p = askdirectory()  # show an "Open" dialog box and return the path to the selected file
    print('selected files:', source_p, '\n')
    return source_p


def destination_path():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    destination_p = askdirectory()  # show an "Open" dialog box and return the path to the selected file
    print('selected files:', destination_p, '\n')
    return destination_p


def move(file, path):
    shutil.move(file, path)


image = ['png', 'jpg', 'jpeg', 'ico', 'svg', 'gif', 'tif', 'bmp']
documnet = ['docx', 'doc', 'xlsx', 'xls', 'pptx', 'ppt', 'txt']
video = ['mkv', 'mp4', 'avi', 'wmv', 'mov', 'mpg', 'mpeg', 'h264']
audio = ['mp3', 'wav', 'aac', 'webm', 'mpa', 'cda', 'mid', 'wpl']
programs = ['php', 'html', 'css', 'py', 'js', 'ts', 'java', 'c', 'cpp', 'class', 'swift']
system = ['iso', 'dmg', 'dll', 'bin', 'dat', 'sys', 'msi']


def catagorize(sources, desti):
    folderpath = sources
    os.chdir(folderpath)
    os.getcwd()
    os.listdir()  # check the files.
    # get the extention
    list_extention = []

    for f1 in os.listdir():
        extention = f1.split(".")[-1]
        list_extention.append(extention)

    print(list_extention)
    path = desti

    # How we can trnsfer the files in spacific folder.
    for ex in list_extention:

        if ex in image:
            dest_path = desti + "/" + "Images" + '/' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex in documnet:
            dest_path = desti + "/" + "Documents" + '/' + ex
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex in video:
            dest_path = path + "\\" + "Videos" + '\\' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex in audio:
            dest_path = path + "\\" + "Musics" + '\\' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex in programs:
            dest_path = path + "\\" + "Programs" + '\\' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex in system:
            dest_path = path + "\\" + "System" + '\\' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        elif ex not in image or documnet or video or audio or programs or system:
            dest_path = path + "\\" + "Others" + '\\' + ex

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            for fl in os.listdir():
                if ex in fl:
                    move(fl, dest_path)

        else:
            print('file cannot moved')


catagorize(source_path(), destination_path())
print('files moved')
