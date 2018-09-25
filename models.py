from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<user %r>' % self.name