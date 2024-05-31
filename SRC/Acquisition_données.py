import json
import jsonpath_ng as jp #actuellement pb avec le path
import numpy as np
with open("trajectory.jason", "r") as f: #on ouvre le fichier json et on place les données dans data
    data= json.load(f)

t=0.5
query1=jp.parse("pose.position")
coord_x=[]
coord_y=[]
vitesse_l=[]
vitesse_a=[]

for i in range(800):#on selectionne uniquement x et y 
    coord_x.append(0)
    coord_y.append(0)
    coord_x[i]=data[i]["pose"]['position']['x']
    coord_y[i]=data[i]["pose"]['position']['y']

for i in range(799):
    vitesse_l.append()
    vitesse_a.append()
    vitesse_l[i]=(((coord_x[i+1]-coord_x[i])/t)+((coord_y[i+1]-coord_y[i])/t))/2#calcul de la vitesse avec les coordonnées récupérées
    if (coord_x[i+1]-coord_x[i])==0:
        vitesse_a[i]=0
    else:
        vitesse_a[i]=np.arctan(((coord_y[i+1]-coord_y[i])/(coord_x[i+1]-cord_x[i])))/t

print(vitesse_l)
