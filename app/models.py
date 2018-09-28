from app.exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    user_account = db.Column(db.String(64), unique=True)
    user_pwd = db.Column(db.String(255), nullable=False)
    user_salt = db.Column(db.Integer(), nullable=False)
    user_name = db.Column(db.String(64), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.name


    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class User2(db.Model):
    __tablename__ = 'user2'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<User2 %r>' % self.name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

