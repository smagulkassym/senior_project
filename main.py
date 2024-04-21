from flask import Flask
from routes.upload import upload
from routes.home import home_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(home_bp)
app.register_blueprint(upload)

if __name__ == "__main__":
    app.run()