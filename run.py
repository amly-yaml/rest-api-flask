from app import app
from db import db

db.init_app(app)

@app.before_first_request   #effect the method below it, run the method before the first request into this app
def create_tables():
    db.create_all()