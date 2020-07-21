"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Mon Jul 20 13:48:27 2020

@author: simplon
"""

import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://simplon:simplon@localhost:3306/simplon')
data = pd.read_sql_query('SELECT * FROM jeux_video', engine)
print(data)



engine = create_engine('mysql+pymysql://simplon:simplon@localhost:3306/assurauto')
data2 = pd.read_sql_query('SELECT * FROM CLIENTS', engine)
print(data2)





#TABLES CLIENTS
import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://simplon:simplon@localhost:3306/assurauto')
CL_ID = pd.read_sql_query("SELECT max(CL_ID) as max FROM CLIENTS;", engine)['max'].values
CL_ID = CL_ID[0]+1
CO_CL_FK = CL_ID
CL_NOM = ''
CL_PRENOM = ''
CL_VILLE = ''
CL_ADRESSE = ''
CL_CODE_POSTAL =''
CL_COORDONNEE = ''



while len(CL_NOM) == 0 or len(CL_PRENOM) == 0 or len(CL_VILLE) == 0 or len(CL_ADRESSE) == 0 or len(CL_CODE_POSTAL) == 0 or len(CL_COORDONNEE) == 0 :

    if len(CL_NOM) == 0:
       CL_NOM = input('veuillez entrer un nom :')
       
    elif CL_NOM != CL_NOM.upper() :
         CL_NOM = CL_NOM.upper()
              
    elif len(CL_PRENOM) == 0:
        CL_PRENOM = input('veuillez entrer un prenom :')

    elif len(CL_VILLE) == 0:
        CL_VILLE = input('veuillez entrer la ville du client :')

    elif len(CL_ADRESSE) == 0: 
        CL_ADRESSE = input("veuillez entrer l'adresse :")

    elif len(CL_CODE_POSTAL) == 0:
        CL_CODE_POSTAL = input('veuillez entrer le code postal :')
        if CL_CODE_POSTAL.isdigit() :
           CL_CODE_POSTAL = CL_CODE_POSTAL
        else:
            print('veuillez ne rentrer que des nombres')
            CL_CODE_POSTAL = ''

    elif len(CL_COORDONNEE) == 0 :
        CL_COORDONNEE = input('veuillez entrer un numéro de tel :')




engine.execute('INSERT INTO CLIENTS (CL_ID, CL_NOM, CL_PRENOM, CL_VILLE, CL_ADRESSE, CL_CODEPOSTAL, CL_COORDONNEE) VALUES (%s, "%s", "%s", "%s", "%s", %s, %s);' %(CL_ID ,CL_NOM ,CL_PRENOM, CL_VILLE, CL_ADRESSE, CL_CODE_POSTAL, CL_COORDONNEE))


#TABLES CONTRAT
import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://simplon:simplon@localhost:3306/assurauto')
CO_ID = pd.read_sql_query("SELECT max(CO_ID) as max FROM CONTRAT;", engine)['max'].values
CO_ID = CO_ID[0]+1
CO_DATE = ''
CO_BONUS = ''
CO_MALUS = ''
CO_CATEGORIE_FK =''



while len(CO_DATE) == 0 or len(CO_BONUS) == 0 or len(CO_MALUS) == 0 or len(CO_CATEGORIE_FK) == 0:

    if len(CO_DATE) == 0:
        CO_DATE = input('Veuillez entrez la date du contrat :')
        
    elif len(CO_BONUS) == 0:
        CO_BONUS = input('Veuillez entrez la valeur du taux de bonus du client :')
        
    elif len(CO_MALUS) == 0:
        CO_MALUS = input('Veuillez entrez la valeur du taux de malus du client :')
        
    elif len(CO_CATEGORIE_FK) == 0:
        CO_CATEGORIE_FK = input('Veuillez entrez la catégorie du contrat de véhicule :')
        
        
engine.execute('INSERT INTO CONTRAT (CO_ID, CO_DATE, CO_BONUS, CO_MALUS, CO_CATEGORIE_FK, CO_CL_FK) VALUES(%s, "%s", %s, %s, "%s", %s);' %(CO_ID, CO_DATE, CO_BONUS, CO_MALUS, CO_CATEGORIE_FK, CO_CL_FK))
#CL_ID = max(ID) +1 from clients 
#CL_NOM = "Sergio"
#CL_PRENOM = "Rodriguez"
#CL_ADRESSE = 'Avenue Jean-medecin'
#CL_VILLE = "NICE"
#CL_CODE_POSTAL = '06100'
#CL_COORDONNEE = "07 89 23 43 55"

#CO_ID = '44'
#CO_DATE = '23/02/2019'
#CO_BONUS = '345'
#CO_MALUS = '455'
#CO_CATEGORIE_FK = 'véhicule utilitaire'
#engine.execute('INSERT INTO CLIENT (CL_ID, CL_NOM, CL_PRENOM, CL_ADRESSE, CL_VILLE, CL_COORDONNEE) VALUES (%s, 's%');' %(CL_ID, CL_NOM, CL_PRENOM, CL_ADRESSE, CL_VILLE, CL_COORDONNEE))