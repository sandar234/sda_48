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

# import csv
#
# coloane = ['C1','C2']
# data = [{'C1':1,'C2':2},{'C1':3,'C2':4}]
#
# with open('out_dict.csv', 'w') as c:
#     write = csv.DictWriter(c, fieldnames=coloane)
#     write.writeheader()
#     write.writerows(data)

date_json = {
"studenti":[
{"nume":"Ion",
'prenume':"Ionescu",
"adresa":{
"oras":"Bucuresti",
"strda":"Calea Victoriei",
"numar":123
},
"nr tel":"4078541112"
},
{"nume":"Vasile",
'prenume':"Vasilescu",
"adresa":{
"oras":"Iasi","strda":"Calea Liberatii","numar":1234
},"nr tel":"407854143563"
}
]
}

import json
fisier_json = "datele_mele.json"

# #reprezentarea "frumoasa"/usor de citit a unui dictionar json
# pretty_json_string = json.dumps(date_json, indent= 2)
# print(pretty_json_string)
#
# #scrierea unui json intr-un fisier cu extensia .json

# with open(fisier_json,"w") as file:
#     json.dump(date_json, file)

with open(fisier_json, "r") as file:
    date_citite = json.load(file)

print(date_citite)
print(type(date_citite))
print('\n')
print(json.dumps(date_citite, indent=2))

