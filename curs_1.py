def impartire(a,b):
    try:
        rez = round(a/b,2)
        return  rez
    except:
        print("A fost o eroare")
    return None



def impartire(a,b):
    try:
        rez = round(a/b,2)
        return  rez
    except Exception as e:
        print(f"Eroarea este = {e}")


def impartire(a,b):
    return round(a/b,2)

print(impartire(7,0))

#https://github.com/constantinus345/sda_48