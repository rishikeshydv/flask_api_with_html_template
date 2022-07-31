from sqlalchemy import create_engine
from os import path

ROOT = path.dirname(path.relpath(__file__))

def conn():
    hostname = 'localhost'
    database = 'trials'
    username = 'postgres'
    pwd = 'rishiBLOOMED!321'
    port_id = '5432'

    engine = create_engine('postgresql+psycopg2://postgres:rishiBLOOMED!321@localhost:5432/trials')
    connect_1 = engine.connect(path.join(ROOT, 'database.db'))
    return connect_1

def create_post(name, content):
    con = conn()
    con.execute('insert into posts (name,content) values (%s,%s)', (name, content))

def get_posts():
    con = conn()
    return con.execute('select * from posts').fetchall()


    