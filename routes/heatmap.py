from flask import Blueprint, request, send_from_directory, render_template

# heatmap = Blueprint('heatmap', __name__, static_folder="../static")
heatmap = Blueprint('heatmap', __name__)

@heatmap.route("/map", methods=["GET"])
def get_heatmap():
    if request.method == "GET":
        return render_template("index.html")
        # return send_from_directory(heatmap.static_folder, "index.html")