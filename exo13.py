#Bienvenue a notre progrmme de l'exo 13"
import datetime
date_string = '31-12-2010'
date_format = '%d-%m-%Y'
try:
    date_obj = datetime.datetime.strptime(date_string,date_format)
    print(date_obj)
except ValueError:
    print("incorrect data format, should be DD-MM-YYY")

