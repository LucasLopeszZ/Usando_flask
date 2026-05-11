from flask import Flask
app = Flask (__name__)

from app.routes import homepage
from app.routes import sobre
from app.routes import contato
from app.routes import servico