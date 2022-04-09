from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


# Instanciando o Flask
app = Flask(__name__)

# Conectando a aplicação ao banco de dados.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seuUsuário:suaSenha@localhost:5432/nomeDoSeuBanco'

# A opção TRACK_MODIFICATIONS é depreciated, ela envia um aviso antes e 
# depois de uma alteração ser confirmada no banco de dados.
# Por isso, iremos desativá-la.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuramos o SQLAlchemy com o flask, agora precisamos instanciá-lo.
db = SQLAlchemy(app)