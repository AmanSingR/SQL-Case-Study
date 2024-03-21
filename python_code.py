from sqlalchemy import create_engine
import pandas as pd

Server ='server'
Database = 'database'
Drive = 'driver'
Database_con = f'add server,database,drive'

engine = create_engine(Database_con)
conn = engine.connect()

files = ['artist','canvas_size','image_link','museum_hours','museum','product_size','subject','work']

for fil in files:
    df = pd.read_csv(f'file path\\{fil}.csv')
    df.to_sql(fil,con = conn, if_exists='replace', index=False)