f = open("C:/Users/shigoyal/Python/PythonPrac/File Handling/oulipo.txt", "r")

lines = f.readlines()

for line in lines:
    first_char = line[0]
    print("<b>"+first_char+"</b>"+line.strip(first_char))