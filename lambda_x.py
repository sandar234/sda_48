# def square_of_number(x):
#     return x**2
#
# varx = 50
# print(square_of_number(varx))
#
# square_of_number_v2 = lambda x: x**2
# print(square_of_number_v2(varx))

# def capitalize_string(strx):
#     return strx.upper()
# strx_ex = 'studentii învață Python'
# print(capitalize_string(strx_ex))
#
# capitalize_string_v2 = lambda strx: strx.upper()
# print(capitalize_string_v2(strx_ex))

items = list(range(1,10))
# print(items)
#
# patrate = list(map(lambda x: x**3, items))
# print(patrate)
#
# filtru = list(filter(lambda x: x%3, items))
# print(filtru)

print(sum(items))
suma = 0
for el in items:
    suma += el
print(suma)
