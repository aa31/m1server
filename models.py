from flask_sqlalchemy import  SQLAlchemy
from app import app
import pymysql,json

pymysql.install_as_MySQLdb()

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mm123465@localhost/m1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
class User(db.Model):
    __tablename__ = 'user2'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.name



test_role1 = User(id=1,name= 'name')
# db.session.add(test_role1)
# db.session.commit()
# print( type( User.query.all()))
# print( json.dumps( User.query.all()))
# db.session.query(User).first()