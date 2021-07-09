"""Flask app for Cupcakes"""
from logging import NullHandler
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'abc124'

connect_db(app)

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    try:
        new_cupcake = Cupcake(
            flavor = request.json['flavor'],
            rating = request.json['rating'],
            size = request.json['size'],
            image = request.json['image'] 
        )
    except: 
        new_cupcake = Cupcake(
            flavor = request.json['flavor'],
            rating = request.json['rating'],
            size = request.json['size']
        )
    db.session.add(new_cupcake)
    db.session.commit()
    resp_json = jsonify(cupcake = new_cupcake.serialize())
    return(resp_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')









