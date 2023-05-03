path_to_file = r'C:\Users\const\PycharmProjects\SDA_48\curs_1.txt'

# f = open(path_to_file,"w")
# f.write("SDA is cool")
# f.close()

#optiunea de mai sus implica mai multe operatiuni, inclusiv riscul de a uita sa inchidem
#fisierele deschise sau conexiuni la baze de date, = risc!

# with open(path_to_file, 'w') as f:
#     f.write("SDA are multi studenti")

with open(path_to_file, 'r') as filex:
    content = filex.read()

print(content)



