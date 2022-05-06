def create():
    file = open("team.txt","x")
    file= open("team.txt","w")
    file.write(f"sr.no name age address \n")
    print("file is created")


def addrec(sr,name,age,address):
    newdata = (sr,name,age,address)
    file = open("team.txt","r")
    cont = file.readlines()
    file.close()

    data= []

    for sent in cont:
        t = tuple(sent.strip().split())
        data.append(t)

    data.append(newdata)

    file = open("team.txt","w")
    for nt in data:
        file.write(f"{nt[0]:^9} {nt[1]:^8} {nt[2]:^3} {nt[3]:^10} \n")
    file.close()


def update(sr,name,age,address):
    newdata = (sr,name,age,address)
    file = open("team.txt","r")
    cont = file.readlines()
    file.close()

    data =[]

    for sent in cont:
        t = tuple(sent.strip().split())
        data.append(t)

    data.pop(sr)
    data.insert(sr,newdata)

    file = open("team.txt","w")
    for nt in data:
        file.write(f"{nt[0]:^9} {nt[1]:^8} {nt[2]:^3} {nt[3]:^10} \n")
    file.close()


def read():
    file = open("team.txt","r")
    print(file.read())
    file.close()

    
def delrec(sr):
    file = open("team.txt","r")
    cont = file.readlines()
    file.close()

    data = []

    for sent in cont:
        t = tuple(sent.strip().split())
        data.append(t)

    data.pop(sr)

    file = open("team.txt","w")
    for nt in data:
        file.write(f"{nt[0]:^9} {nt[1]:^8} {nt[2]:^3} {nt[3]:^8} \n")
    file.close()
