from flask import Flask
from routes.upload import upload
from routes.home import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(upload)

if __name__ == "__main__":
    app.run(debug=True)