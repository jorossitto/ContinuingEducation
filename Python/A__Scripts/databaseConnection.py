import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///sqlalchemy_sqlite.db')
connection =engine.connect()

results = engine.execute('select * from posts limit 10')
first_result = results.fetchone()
otherResults = results.fetchall()

query = 'select * from posts'
postsDF = pd.read_sql_query(query, engine)

