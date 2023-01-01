from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)


with app.app_context():
    from routes.main import *
    from routes.plants import *
    from routes.employees import *
    from models.models import *
    # На наступній лекції
    # db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)