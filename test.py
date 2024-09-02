import random
import time

from database.DAO import DAO
from model import model

mod=model.Model()

def testGrafoRic():
    def getCucine2(citta,prezzo):
        lista = []
        cucine_R={}

        resDAO = DAO.getCucineDAO(citta, prezzo, 1, 5)
        for i in resDAO:
            b = str(i)
            # cucine = b.removeprefix("[").removesuffix("]").replace("'", "").replace(" ", "").split(",")
            cucine = b.removeprefix("[").removesuffix("]").replace("'", "").split(",")

            for c in cucine:
                c = c.strip()
                if c not in lista:
                    lista.append(c)
                    cucine_R[c] = False
        return cucine_R

    allcitta=mod.getAllCitta()
    allprezzi=mod.getAllPrezzi()
    mod.listaUtente=[]

    file=open("tempiRicorsione.txt","a")
    file.write("\n\nNUOVO TEST********************************\n")

    for c in allcitta:
        print(f"\n****{c}")
        file.write(c+":\n")

        for p in allprezzi:
            print(f"- {p}")

            s=""

            cucine_R = getCucine2(c,p)
            k=list(cucine_R.keys())

            for i in range(3):
                pos=random.choice(range(0,len(k)))
                el=k[pos]
                cucine_R[el]=True

            mod.cucine_R=cucine_R

            for a in cucine_R.keys():
                if cucine_R[a]:
                    s+=f" {a}"

            print("Cucine: "+s)
            t1=time.time()
            a,b=mod.calcola(c,p,5,False,False,False)
            t2=time.time()

            file.write(f"{t2-t1} - {len(b)}\n")
    file.close()
    print("finito")

def testClassi():
    #test per suddivisione classi
    citta=DAO.getAllCittaDAO()

    for c in citta:
        res=DAO.testClassiDAO(c)
        print(f"\n{c}:")
        print(res)

# rist=DAO.getAllRistorantiDAO("$","Rome")
# for r in rist:
#     s = str(r.Reviews)
#     lRec = s.replace("[", "").replace("]", "").split("', '")
#     dizRec = {}
#     dizRec[lRec[2].replace("'", "").strip()] = lRec[0].replace("'", "").strip()
#     dizRec[lRec[3].replace("'", "").strip()] = lRec[1].replace("'", "").strip()
#     print(dizRec)


def testMigliori(i):
    #tempo per trovare i 10 migliori sql-python

    file=open("tempi.txt","w")
    file2=open("tempiPython.txt","w")
    citta=DAO.getAllCittaDAO()
    prezzi=DAO.getAllPrezziDAO()

    for c in citta:
        for p in prezzi:

            t1=time.time()
            d=mod.getTopDieci(c,p,1,5,"Qualsiasi")
            t2=time.time()

            t3=time.time()
            rist= DAO.getAllRistorantiDAOTest(p,c)
            ristOrd=sorted(rist,key=lambda x:(-x.Rating,x.Ranking))
            if len(ristOrd)<10:
                pass
            else:
                ristOrd=ristOrd[:10]
            t4=time.time()

            file.write(f"{i} {t2-t1}\n")
            file2.write(f"{i} {t4-t3}\n")
            print(i)
            i+=1

for i in range(0,3):
    testGrafoRic()