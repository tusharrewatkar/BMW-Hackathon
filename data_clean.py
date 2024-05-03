#%%
import pandas as pd

try: 
    df = pd.read_csv(r'C:\Users\s.stroka\Desktop\BMW Inno Hub\data\SAP Data 2.4 10K.csv', encoding='ISO-8859-1', sep=None, engine='python')
except Exception as e:
    print('Failed to read with automatic delimiter detection: ', str(e))

df = df.fillna('Unknown')

erfasser_list = []
email_list = []
location_list = []
solution_list = []
notif_creatDate = []
mal_startStamp = []
mal_endStamp = []

len(solution_list) == len(email_list) == len(erfasser_list)
# len(max(solution_list, key=len))

for line in range(df.shape[0]):

    try:
    
        # line = 0
        df_longtext = df.notificationlongtext[line]
        if 'Erfasser' not in df_longtext or df_longtext == 'Unknown':
            continue

        df_one = df_longtext.split(' ')
        # erfasser, email = df_one[1].split(',;')

        if len(df_one[1].split(',;'))==1:
            temp = df_one[1].split(',;')
            temp = temp[0].split(',')
            erfasser = temp[0]

            temp = df_one[1].split(',;')
            temp = temp[0].split(';')
            email = temp[2]
        else:
            erfasser, email = df_one[1].split(',;')

        erfasser_list.append(erfasser); email_list.append(email)
        del erfasser; del email

        # if 'Lokation' in [entry for entry in df_one if 'Lokation' in entry][0]:
        #     location = df_one[df_one.index([entry for entry in df_one if 'Lokation' in entry][0])+1][:-1]
        # else:
        #     location = df_one[df_one.index('Lokation:')+1]

        location_list.append(df.maintenancefunctionallocationdescription[line])
        notif_creatDate.append(df.notificationcreationdate[line])
        mal_startStamp.append(df.malfunctionstarttimestamp[line])
        mal_endStamp.append(df.malfunctionendtimestamp[line])

        df_one = df_longtext.split(',')
        solution = df_one[-1]
        solution_list.append(solution)
        del solution

        if len(email_list) != len(solution_list):
            print(email_list[-1])
            print(solution_list[-1])
            print('test')

    except (ValueError, IndexError):
        continue
# %%

len(email_list)
len(location_list)
len(erfasser_list)
len(solution_list)
len(mal_startStamp)


table = pd.DataFrame({'Melder':erfasser_list, 'Email':email_list, 'Lokation':location_list, 'Solution':solution_list, 
                      'notif_creatDate':notif_creatDate, 'mal_startStamp':mal_startStamp, 'mal_endStamp':mal_endStamp})
table.to_csv(r'C:\Users\s.stroka\Desktop\BMW Inno Hub\data\res_table.csv')
# %%
