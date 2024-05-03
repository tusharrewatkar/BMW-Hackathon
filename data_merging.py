#%%
import pandas as pd

event_tech_df = pd.read_excel(r'C:\Users\s.stroka\Desktop\BMW Inno Hub\data\Events_Technology_E__10K.xlsx')[['notificationNumber','valuetext','valueeventtype']]
sap_df = pd.read_csv(r'C:\Users\s.stroka\Desktop\BMW Inno Hub\data\res_table.csv')  # Update the path as necessary

num_sap_rows = len(sap_df)

random_notifications = event_tech_df['notificationNumber'].sample(n=num_sap_rows, replace=True, random_state=1)

sap_df['NotificationNumber_new'] = random_notifications.values

result_df = pd.merge(event_tech_df, sap_df, left_on='notificationNumber', right_on='NotificationNumber_new', how='right')

cols = result_df.columns.drop(['Unnamed: 0','NotificationNumber_new'])

result_df = result_df[cols]
result_df.to_csv(r'C:\Users\s.stroka\Desktop\BMW Inno Hub\data\plc_merge_data.csv', index=False)  # Saves the result of the join

