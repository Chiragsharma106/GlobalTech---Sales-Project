# Use this Script to load data into SQL.

# # Ingesting Products Data into PostgreSQL

# In[1]:


import pandas as pd
import os
from sqlalchemy import create_engine
import pyodbc


# In[2]:


Folder = r"C:\Users\chira\Documents\All Files\PortFolio Dashboards💸\#1 SalesDashboard\AllData\DimTables"


# In[3]:


pg_user = 'postgres'
pg_password = 'SQUAL#QUE'
pg_host = 'localhost'
pg_port = '5432'
pg_db = 'SalesDashboard'


# In[4]:


PostgresCar = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')


# In[5]:


for files in os.listdir(Folder):
    if files.startswith("Dim"):
        names = files.replace('.csv', '').lower()
        Csvpath = os.path.join(Folder, files)
        df = pd.read_csv(Csvpath)

        # Clean and standardize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)

        print('Table Loading:', names)
        df.to_sql(names, con=PostgresCar, if_exists='replace', index=False)

print("✅ Done😉")





