spisok=["potato","cucumber","milk"]
def append_product(name_product):
    spisok.append(name_product)

def delete_tovar(name_tovar):
    spisok.remove(name_tovar)
append_product("milk")
delete_tovar("cucumber")
print(spisok)