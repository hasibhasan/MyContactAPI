from app import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body


    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
    def update(self):
        return db.session.commit()
    def delete(self,resource):
        db.session.delete(resource)
        return db.session.commit()

    def __repr__(self):
        return  '<title %r>' % (self.title)