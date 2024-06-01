
# Import 
import json
import jsonpath_ng as jp #actuellement pb avec le path
import numpy as np
with open("trajectory.jason", "r") as f: #on ouvre le fichier json et on place les données dans data
    data= json.load(f)

t=0.5
query1=jp.parse("pose.position")
coord_x=[] 
coord_y=[]
vitesse_l=[] #Vitesse linéaire
vitesse_a=[] #Vitesse angulaire 

# Extraction des données
for i in range(800):#on selectionne uniquement x et y 
    coord_x.append(data[i]["pose"]['position']['x'])
    coord_y.append(data[i]["pose"]['position']['y'])

# Calcul des vitesses linéiare et angulaire
for i in range(799):
    vitesse_l.append((((coord_x[i+1]-coord_x[i])/t)+((coord_y[i+1]-coord_y[i])/t))/2)
    

    if (coord_x[i+1]-coord_x[i])==0:
        vitesse_a.append(0)
    else:
        vitesse_a.append(np.arctan(((coord_y[i+1]-coord_y[i])/(coord_x[i+1]-coord_x[i])))/t)

print(vitesse_l)
