"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, jsonify, redirect
from models import db, connect_db, User

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "a-secret"

connect_db(app)

# @app.errorhandler(404)
# def page_not_found(e):
#     """ Show error 404 page """
#     return render_template('404.html'), 404

@app.route("/")
def show_home():
    """ Redirect to register page """
    return redirect('/register')

@app.route('/register')
def form_register():
    """ Display register user form """

    return render_template('form-register.html')

# @app.route('/api/cupcakes/<int:cid>')
# def single_cupcake(cid):
#     """ Respond with JSON of a single cupcake """
#     cup = Cupcake.query.get_or_404(cid)
#     cup = cup.serialize()
#     return jsonify(cupcake=cup)

# @app.route('/api/cupcakes', methods=['POST'])
# def new_cupcake():
#     """ Respond with JSON of newly created cupcake """
#     data = request.json
#     cup = Cupcake(flavor=data['flavor'], image=data['image'] or None, rating=data['rating'], size=data['size'])
#     db.session.add(cup)
#     db.session.commit()
#     return (jsonify(cupcake=cup.serialize()), 201)