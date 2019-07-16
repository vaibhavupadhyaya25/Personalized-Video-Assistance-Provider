import pandas as pd
import numpy as np
from array import *
import numpy as np

def modelling_fetch(domain_name):
#domain = str(input("enter the domain"))
       search = domain_name + ".csv"
       my_li_model = []
       dt = pd.read_csv("C:/Users/india/AppData/Local/Programs/Python/Python37/modelling/"+search)

       #count=dt['N']
       
       receptives=dt['R']
       receptive=np.array(receptives)
       affecteds=dt['A']
       affected=np.array(affecteds)
       cureds=dt['C']
       cured=np.array(cureds)


#initialising constants

#population growth
       u=0.08

#carrying capacity 
       k=15000

#no of videos
       n=20

#recorddays-1
       d=8

#alpha is the trending rate and beta is decaying rate

       rrate=(receptive[receptive.size-1]-receptive[0])/d
       arate=(affected[affected.size-1]-affected[0])/d
       crate=(cured[cured.size-1]-cured[0])/d

       alpha = ((u*(1-(n/k))*n)-rrate)/(receptive[d]*affected[d])
       beta = ((alpha*receptive[d]*affected[d])-arate)/affected[d]
       my_li_model.append(alpha)
       my_li_model.append(beta)
       #print(alpha)
       #print(beta)
       #print(my_li_model)
       return my_li_model

