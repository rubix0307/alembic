from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, Table
from sqlalchemy import MetaData


metadata = MetaData()
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/delivery_restaurant_site_test"
engine = create_engine(DATABASE_URL, echo=True)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(255), unique=True),
    Column('email', String(255), unique=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
)


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return 'Test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)