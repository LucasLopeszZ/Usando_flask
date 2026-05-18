from flask import Flask
app = Flask (__name__)

app.config["SECRET_KEY"] = 'sdKLNsndkjsafbndfnd877'

from app.routes import homepage
from app.routes import sobre
from app.routes import contato
from app.routes import servico
from app.routes import listagem
from app.routes import cadastro