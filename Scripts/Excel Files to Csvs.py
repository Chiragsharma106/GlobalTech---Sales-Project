# Use this Script to Convert Excel files into CSVs for a smooth Data model in Power BI

# In[1]:


import pandas as pd
import os
from sqlalchemy import create_engine
import pyodbc


# In[2]:


folder = r"C:\Users\chira\Documents\All Files\#TrickyDashboards\SalesDashboard\AllData\ReData"
Ongoing = r"C:\Users\chira\Documents\All Files\#TrickyDashboards\SalesDashboard\AllData\PythonData"


# # Excel to CSVs Conversions for Power BI Dashboard

# In[3]:


for files in os.listdir(folder):
    if files.endswith("xlsx"):
        Excel_Path = os.path.join(folder, files)
        Excel_File = pd.read_excel(Excel_Path, sheet_name= None)
        for names, df in Excel_File.items():
            Csv_Names = files.replace(".xlsx", "") + " - " + names + ".csv"
            Csv_Path = os.path.join(Ongoing, Csv_Names)
            df.to_csv(Csv_Path, index = False)

print("AllDone🙌")

