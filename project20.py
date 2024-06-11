assert 0<1,"Problem"
try:
    5/0
except:
    print("Problem")
class Error(Exception):
    pass
raise Error("Problem")
