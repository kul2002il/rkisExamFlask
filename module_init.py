import sqlite3


def connect_db(app):
	return sqlite3.connect(app.config['DATABASE'])


def init_db(app):
	script = '''
CREATE TABLE IF NOT EXISTS servise (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title STRING NOT NULL,
	description STRING NOT NULL,
	datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	image STRING
)
'''
	db = connect_db(app)
	db.cursor().execute(script)
	db.commit()
	db.close()
