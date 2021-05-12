from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devmysql:mY$Ql@d3v2o21!!10.20.19.205/seo'

db = SQLAlchemy(app)


from app.apis import urls