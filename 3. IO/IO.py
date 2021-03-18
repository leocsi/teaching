with open("C:\Code\Teaching\\3. IO\german_names.txt", "r") as file:  # specify file path(use relative paths), and opening mode
                                                                     # r -read, w- write, rw- readwrite
    data = file.readlines()  # read the data(when simply opened its just a memory address) this will be a list of lines
    file.close()  # always close!!!

for line in data:  # we can loop the data as if it was a simple array of numbers
    line = line.strip()  # remove whitespaces
    print(line)
