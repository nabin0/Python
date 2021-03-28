import os
def soldier(path, file, format):
    '''This Function Takes Three Parameters:\n
    path of folder: This is the path where files are located.
    file path:Path of file which contains name of files not to be affected by program
    extension of file: Given extensions files will be renamed with numerical value name as eg: 1.png
    '''
    os.chdir(path)
    i = 1
    with open(file) as txtFile:
        files = txtFile.read().split('\n')

    filesInPath = os.listdir(path)
    for file in filesInPath:
        if file not in files:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1

if __name__ == '__main__':
    print(soldier.__doc__)
    path = input("Enter the path where files are located: ")
    file = input("Enter the file in which names of file are given which should not be changed: ")
    ext = input("Enter the extension whose name you want to change in asccending order nums: ")
    soldier(path, file, ext)
