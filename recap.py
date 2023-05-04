# try:
#     print(5/0)
# except IndexError as e:
#     print(f'eroare: {e}')
# finally:
#     print('se executa indiferent daca try a fost cu succes sau nu')

file_path = 'B:/Dropbox/SDA/Python_48_intermed/sda_1.txt'

# f = open(file_path)
# print(f.read())
# f.close()

with open(file_path, 'r') as f:
    print(f.read())

