import openpyxl
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','finalyear.settings')
django.setup()

from rfm_model.models import *

def populate_customer_data():
    source = "datafile/datasheet.xlsx" #filename should be updates here and keep in the datafile folder
    src_workbook = openpyxl.load_workbook(source)
    for row in src_workbook.worksheets[0].iter_rows(values_only=False):
        words = []
        for cell in row:
            words.append(cell._value)
        if words[0] != 'customer_id' and words[0] != None:
            p = customerData(
                customer_id = words[0],
                customer_name = words[1],
                recency = words[2],
                frequency = words[3],
                monetary = words[4],
            )
            p.save()

def rfm_values(Champion,Loyal_Customer,Potential_Loyalis,Recent_Customer,Promisin,Customers_Needing_Attentio,About_to_Slee,At_Ris,Cant_Lose_The,Hibernatin,Los):

    for i in Champion:
        p = champions(Champions = i )
        p.save()
    for i in Loyal_Customer:
        p = loyalCustomers(Loyal_Customers=i)
        p.save()
    for i in Potential_Loyalis:
        p = potentialLoyalist(Potential_Loyalist=i)
        p.save()
    for i in Recent_Customer:
        p = recentCustomers(Recent_Customers=i)
        p.save()
    for i in Promisin:
        p = promising(Promising=i)
        p.save()
    for i in Customers_Needing_Attentio:
        p = customersNeedAttention(Customers_Needing_Attention=i)
        p.save()
    for i in About_to_Slee:
        p = aboutToSleep(About_to_Sleep=i)
        p.save()
    for i in At_Ris:
        p = atRisk(At_Risk=i)
        p.save()
    for i in Cant_Lose_The:
        p = cantLoseThem(Cant_Lose_Them=i)
        p.save()
    for i in Hibernatin:
        p = hibernating(Hibernating=i)
        p.save()
    for i in Los:
        p = lost(Lost=i)
        p.save()






#populate_customer_data()
""" drop table rfm_model_champions 
    drop table rfm_model_abouttosleep
    drop table rfm_model_atrisk
    drop table rfm_model_cantlosethem
    drop table rfm_model_customerdata
    drop table rfm_model_customersneedattention
    drop table rfm_model_hibernating
    drop table rfm_model_lost
    drop table rfm_model_loyalcustomers
    drop table rfm_model_potentialloyalist
    drop table rfm_model_promising
    """

