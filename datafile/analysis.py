from datafile.dataSet import *
def generateReport(data_set):
    customerId = []
    recency = []
    frequency = []
    monetary =[]
    for p in data_set:
        customerId.append(p.customer_id)
        recency.append(p.recency)
        frequency.append(p.frequency)
        monetary.append(p.monetary)
    """
    print(customerId)
    print(recency)
    print(frequency)
    print(monetary)"""


    """
    customer_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    recency = [8,5,4,3,1,2,6,9,7,9,6,5,1,2,4,2,3,6,1,9,7,4,5,8,6,5]
    frequency = [3,8,1,9,6,6,3,1,2,5,6,9,8,5,4,1,2,3,6,5,4,8,9,8,5,8]
    monetary = [100,1500,200,6560,500,200,300,600,800,900,1000,2500,1500,3000,4000,500,600,700,800,400,1500,2000,900,200,100,500]"""

    recency_id = []
    frequency_id = []
    monetary_id = []

    for i in range(len(recency)):
        x = [i+1]
        x.append(recency[i])
        recency_id.append(x)
    for i in range(len(frequency)):
        x = [i+1]
        x.append(frequency[i])
        frequency_id.append(x)
    for i in range(len(monetary)):
        x = [i+1]
        x.append(monetary[i])
        monetary_id.append(x)


    recency_id.sort(key= lambda x: x[1])
    frequency_id.sort(key= lambda x: x[1],reverse=True)
    monetary_id.sort(key= lambda x: x[1],reverse=True)

    """print(recency_id)#cutomer_id , rfm_value
    print(frequency_id)
    print(monetary_id)"""

    len_var = len(recency_id)
    mod_val = int(len_var/5)
    mod_rem = int(len_var%5)

    rfm_score_values = [5,4,3,2,1]
    if mod_rem == 0:
        val = 0
        for i in range(0,len(recency_id),mod_val):
            for j in range(mod_val):
                recency_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
        val = 0
        for i in range(0,len(frequency_id),mod_val):
            for j in range(mod_val):
                frequency_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
        val = 0
        for i in range(0,len(monetary_id),mod_val):
            for j in range(mod_val):
                monetary_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
    else:
        val = 0
        for i in range(0, len(recency_id)-mod_rem, mod_val):
            for j in range(mod_val):
                recency_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
        for i in range(len(recency_id)-mod_rem,len(recency_id)):
            recency_id[i].append(0)
        val = 0
        for i in range(0, len(frequency_id)-mod_rem, mod_val):
            for j in range(mod_val):
                frequency_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
        for i in range(len(frequency_id)-mod_rem,len(frequency_id)):
            frequency_id[i].append(0)
        val = 0
        for i in range(0, len(monetary_id)-mod_rem, mod_val):
            for j in range(mod_val):
                monetary_id[i].append(rfm_score_values[val])
                i += 1
            val += 1
        for i in range(len(monetary_id)-mod_rem,len(monetary_id)):
            monetary_id[i].append(0)

    """
    print(recency_id)#customer_id , rfm_value , rfm_score
    print(frequency_id)
    print(monetary_id)"""

    recency_id.sort()
    frequency_id.sort()
    monetary_id.sort()

    #average of frequency and moentary score values

    for i in range(0,len(frequency_id)):
        value = round((frequency_id[i][2] + recency_id[i][2] )/2)
        frequency_id[i][2] = value

    recency_score = []
    freq_mon_score = []

    for i in range(0,len(recency_id)):
        r_score = []
        r_score.append(recency_id[i][0])
        r_score.append(recency_id[i][2])
        recency_score.append(r_score)
        fm_score = []
        fm_score.append(frequency_id[i][0])
        fm_score.append(frequency_id[i][2])
        freq_mon_score.append(fm_score)

    """
    print(recency_score) #customer_id , rfm_Score in 2-D plot
    print(freq_mon_score)
    """

    Champions = []
    Loyal_Customers = []
    Potential_Loyalist = []
    Recent_Customers = []
    Promising = []
    Customers_Needing_Attention = []
    About_to_Sleep = []
    At_Risk = []
    Cant_Lose_Them = []
    Hibernating = []
    Lost = []


    for i in range(0,len(recency_score)):
        if recency_score[i][1] in range(4,6) and freq_mon_score[i][1] in range(4,6):
            Champions.append(recency_score[i][0])
        elif recency_score[i][1] in range(2,6) and freq_mon_score[i][1] in range(3,6):
            Loyal_Customers.append(recency_score[i][0])
        elif recency_score[i][1] in range(3,6) and freq_mon_score[i][1] in range(1,4):
            Potential_Loyalist.append(recency_score[i][0])
        elif recency_score[i][1] in range(4,6) and freq_mon_score[i][1] in range(0,2):
            Recent_Customers.append(recency_score[i][0])
        elif recency_score[i][1] in range(3,5) and freq_mon_score[i][1] in range(0,2):
            Promising.append(recency_score[i][0])
        elif recency_score[i][1] in range(2,4) and freq_mon_score[i][1] in range(2,4):
            Customers_Needing_Attention.append(recency_score[i][0])
        elif recency_score[i][1] in range(2,4) and freq_mon_score[i][1] in range(0,3):
            About_to_Sleep.append(recency_score[i][0])
        elif recency_score[i][1] in range(0,3) and freq_mon_score[i][1] in range(2,6):
            At_Risk.append(recency_score[i][0])
        elif recency_score[i][1] in range(0,2) and freq_mon_score[i][1] in range(4,6):
            Cant_Lose_Them.append(recency_score[i][0])
        elif recency_score[i][1] in range(1,3) and freq_mon_score[i][1] in range(1,3):
            Hibernating.append(recency_score[i][0])
        else:
            Lost.append(recency_score[i][0])

    """
    print(Champions)
    print(Loyal_Customers)
    print(Potential_Loyalist)
    print(Recent_Customers)
    print(Promising)
    print(Customers_Needing_Attention)
    print(About_to_Sleep)
    print(At_Risk)
    print(Cant_Lose_Them)
    print(Hibernating)
    print(Lost)
   """

    rfm_values(Champions,Loyal_Customers,Potential_Loyalist,Recent_Customers,Promising,Customers_Needing_Attention,About_to_Sleep,At_Risk,Cant_Lose_Them,Hibernating,Lost)







