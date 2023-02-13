from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)

# FIXME: Include User model to a file or folder called models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(200))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "id":self.id,
            "username":self.username, 
            "email":self.email
        }

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(User('admin', 'admin@garatzailea.com'))
    db.session.add(User('guest', 'guest@garatzailea.com'))
    db.session.commit()

    users = User.query.all()
    print(users)

@app.route('/')
def index():
    # GET status
    return jsonify({ "message":"pong"})

@app.route('/users', methods=['GET'])
def allusers():
    # GET all data from database & sort by id
    data = User.query.order_by(User.id).all()
    return jsonify({"users":[auser.serialize() for auser in data]})

@app.route('/users/<string:id>', methods=['GET'])
def oneuser(id):
    auser = User.query.get(id)
    return jsonify(auser.serialize())

@app.route('/users', methods=['POST'])
def createusers():
    # POST a data to database
    body = request.json
    if not( 'username' in body):
        return jsonify({"error": "username not found"})
    if not( 'email' in body):
        return jsonify({"error": "email not found"})
        
    name = body['username']
    email = body['email']
    auser = User(name, email)
    db.session.add(auser)
    db.session.commit()

    return jsonify({"message": "sucess!", "data":auser.serialize()})

@app.route('/users/<string:id>', methods=['PUT'])
def updateuser(id):
    auser = User.query.get(id)
    body = request.json
    if not(auser):
        return jsonify({"error": f"User {id} not found"})
    if not( 'username' in body):
        return jsonify({"error": "username not found"})
    if not( 'email' in body):
        return jsonify({"error": "email not found"})

    auser.username = body['username']
    auser.email = body['email']
    db.session.add(auser)
    db.session.commit()
    return jsonify({"message": "sucess!", "data":auser.serialize()})

@app.route('/users/<string:id>', methods=['DELETE'])
def deleteuser(id):
    auser = User.query.filter_by(id=id).first()
    db.session.delete(auser)
    db.session.commit()
    db.session.commit()
    return jsonify({'status': 'user '+id+' has been deleted'})

if __name__ == '__main__':
    app.run()