# ------------ 

import sqlalchemy as sa
conn = sa.create_engine('sqlite://')

meta = sa.MetaData()

zoo = sa.Table('zoo', meta,
	sa.Column('critter', sa.String, primary_key=True),
	sa.Column('count', sa.Integer),
	sa.Column('damages', sa.Float)
	)
meta.create_all(conn)

# again the book's example conn.execute is no longer valid
# using google's example

with conn.begin() as c:
	stmt = sa.insert(zoo).values(critter="bear", count=2, damages=0.0)
	c.execute(stmt)

with conn.begin() as c:
	stmt = sa.insert(zoo)
	c.execute(
		stmt,
		[
			{"critter": "weasel", "count": 1, "damages": 2000.0},
			{"critter": "duck", "count": 10, "damages": 0.0},
			{"critter": "jabberwocky", "count": 50, "damages": 2.5},
		],
	)

with conn.connect() as c:
	result = c.execute(sa.select(zoo))

rows = result.fetchall()

for row in rows:
	print(row)
