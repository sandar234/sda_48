# import pickle
#
# var_dict = {"a":[0,1,2.4,"abc"], "b":True, "c":4.6}
#
# path_to_file = r"C:\Users\const\PycharmProjects\SDA_48\serialization_1.pickle"
#
# with open(path_to_file, "wb") as alias_1:
#     pickle.dump(var_dict,alias_1)
#
# with open(path_to_file, 'rb') as a:
#     datele = pickle.load(a)
#
# print(type(datele))
# print(datele)

import csv

coloane = ['C1','C2']
data = [{'C1':1,'C2':2},{'C1':3,'C2':4}]

with open('out_dict.csv', 'w') as c:
    write = csv.DictWriter(c, fieldnames=coloane)
    write.writeheader()
    write.writerows(data)