from flask import Flask
from routes.upload import upload
from routes.home import home_bp
from routes.heatmap import heatmap
from routes.new import new

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(home_bp)
app.register_blueprint(upload)
app.register_blueprint(heatmap)
app.register_blueprint(new)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
    # app.run(debug=True)