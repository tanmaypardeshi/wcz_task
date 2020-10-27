from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = '5a8829076c843bf7474885f1a5d88c31'
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

from apis import routes
