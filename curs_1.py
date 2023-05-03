# def impartire(a,b):
#     try:
#         rez = round(a/b,2)
#         return  rez
#     except:
#         print("A fost o eroare")
#     return None
#
#
#
# def impartire(a,b):
#     try:
#         rez = round(a/b,2)
#         return  rez
#     except Exception as e:
#         print(f"Eroarea este = {e}")
#
#
# def impartire(a,b):
#     return round(a/b,2)
#
# print(impartire(7,0))

#https://github.com/constantinus345/sda_48

a = 18
b = [1,2,3,7,0,"sf",6]

# def impartire(a,b):
#     try:
#         rez = round(a/b,2)
#         return rez
#     except ZeroDivisionError:
#         raise "Eroarea este ZeroDivisionError"
#     except TypeError:
#         print("Eroarea este TypeError")
#     except Exception as e:
#         print(f"Eroarea este = {e}")
#     # except:
#     #     print("A fost o oarecare exceptie")
#     #CODE SMELL!
#     # finally:
#     #     print("Operatiunea a avut loc")
#     #finally executa cod indiferent ca precedentele instructiuni au intrat in try sau except
#     #= no matter what

def impartire(a,b):
    if b == 0:
        raise ZeroDivisionError("Eroarea este divizarea la zero")
        #raise ne ofera posibililitatea sa facem un mesaj special al erorii, nu sa o gestionam in sine

    try:
        rez = round(a/b,2)
        return rez
    except TypeError:
        print("Eroarea este TypeError")
    except Exception as e:
        print(f"Eroarea este = {e}")



for el in b:
    rezultatul = impartire(a,el)
    print(rezultatul)

# print(b[7])