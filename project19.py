class Users:
    def __init__(self,comuflage,username,password,money,hp,lvl):
        self.comuflage=comuflage
        self.username=username
        self.password=password
        self.money=money
        self.hp=hp
        self.lvl=lvl
    def __str__(self):
        return "ok"
a=Users(comuflage="qwerty",username="Alex",password="1234",money="9876",hp="1500",lvl=9)  
print(a)
