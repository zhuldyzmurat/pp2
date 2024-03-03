#ex1
import os

def dirfile(path):
    print()
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
            
    if __name__ == "__main__":
      path = input()
      dirfile(path) 
#ex2
import os

def dirfile(path):
    if os.path.exists(path):
        print(path,"exists.")
        if os.access(path, os.R_OK):
            print(path , "is readable.")
        else:
            print(path, " is not readable.")

        if os.access(path, os.W_OK):
            print(path, "is writable.")
        else:
            print(path, "is not writable.")

        if os.access(path, os.X_OK):
            print(path, "is executable.")
        else:
            print(path, "is not executable.")
    else:
         print(path,"does not exist.")
if __name__ == "__main__":
    path = input()
    dirfile(path)
#ex3
    import os

def dirfile(path):
    if os.path.exists(path):
        print(path , " exists.")

        dirname, dirname1 = os.path.split(path)
        print(dirname)
        print(dirname1)
    else:
        print(path, "does not exist.")

if __name__ == "__main__":
    path = input()
    dirfile(path)
#ex4
def dirfile(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                count += 1
        print(count)
    except FileNotFoundError:
        print("file was not found")

if __name__ == "__main__":
    filename = input()
    dirfile(filename)
#ex5
def dirfile(filename, data):
    try:
        with open(filename, 'w') as file:
            file.writelines([item + '\n' for item in data])
        print(filename)
    except FileNotFoundError:
        print("an error occured")

if __name__ == "__main__":
    filename = input()
    data = input("the list of strings: ").split(',')
    dirfile(filename, data)
#ex6
import string
def dirfile():
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            with open(filename, 'w') as file:
             file.write(filename)
            print(filename)
if __name__ == "__main__":
    dirfile()
#ex7
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except IOError:
        print(f"Error copying contents from '{source_file}' to '{destination_file}'.")

if __name__ == "__main__":
    source_file = input("the source filename: ")
    destination_file = input("the destination filename: ")

    copy_file(source_file, destination_file)
#ex8
import os

def delete_file(path):
    try:
        if os.path.exists(path):
            if os.access(path, os.F_OK | os.R_OK | os.W_OK | os.X_OK):
                os.remove(path)
                print(path , "has been deleted.")
            else:
                print(f"No access to delete file '{path}'.")

            print(path, "does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    path = input()
    delete_file(path)   