import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

with conn.begin() as c:
	c.execute(
		sa.text(
			"CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT,"
			" damages FLOAT)"
		)
	)



# original book example, pg 325
#	AttributeError: 'Engine' object has no attribute 'execute'
#
# Google says sqlalchemy no longer has an execute method. Corrected 
# version above.

ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
with conn.begin() as c:
	c.execute(
		sa.text('INSERT INTO zoo (critter, count, damages) VALUES (:critter, :count, :damages)'),
		[
			{"critter": "duck", "count": 10, "damages": 0.0},
			{"critter": "bear", "count": 2, "damages": 1000.0},
			{"critter": "weasel", "count": 1, "damages": 2000.0},
		]
	)

with conn.connect() as c:
	rows = c.execute(sa.text("SELECT * FROM zoo"))

for row in rows:
	print(row)


