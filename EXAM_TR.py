import datetime as datetime
import time as time

#exemple [temps execution, periode,comportement tank, prio, nom]
PUMP_1 = [2,5,10,0,"PUMP_1"]
PUMP_2 = [3,15,20,0,"PUMP_2"]
MACHINE_1 = [5,5,-25,0,"MACHINE_1"]
MACHINE_2 = [3,5,-5,0,"MACHINE_2"]

LIST_TACHE = [PUMP_1,PUMP_2,MACHINE_1,MACHINE_2]
Tank = 0
Stock_Roues = 0
Stock_Moteurs = 0
iteration = 0

def RUN_TASK (TACHE) :
    global Tank
    global Stock_Moteurs
    global Stock_Roues
    time.sleep(TACHE[1])
    Tank = Tank + TACHE[2]
    print("Il y a acctuellement",Tank,"huile dans le reservoir,",Stock_Roues,"Roues et ",Stock_Moteurs,"Moteurs \n")
    if Stock_Roues == 4 & Stock_Moteurs == 1 :
        print("1 voiture est prête")
        Stock_Roues = 0
        Stock_Moteurs = 0
        iteration == 1



def Prio_Tache (LIST_TACHE) :

    global iteration
    global Stock_Roues
    global Stock_Moteurs
    global Tank
    Tache_prioritaire = [0,0,0,0,"TACHE"]

    if Tank <= 5 :
        Tache_prioritaire = LIST_TACHE[0]

    if Stock_Roues / 4 > Stock_Moteurs & Tank > 25 :
        Tache_prioritaire = LIST_TACHE[2]
        Tank += LIST_TACHE[2][2]
        Stock_Moteurs += 1

    if Stock_Roues / 4 < Stock_Moteurs & Tank > 10 :
        Tache_prioritaire = LIST_TACHE[3]
        Tank += LIST_TACHE[3][2]
        Stock_Moteurs += 1



    RUN_TASK(Tache_prioritaire)

while iteration < 1 :
    Prio_Tache(LIST_TACHE)






