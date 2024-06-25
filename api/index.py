from flask import Flask
from gbx import Gbx, GbxType
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/testgbx")
def test_gbx():
    g = Gbx('test.Gbx')
    ghost = g.get_class_by_id(GbxType.CTN_GHOST)
    if not ghost:
        quit()

    return "<p>Ghost: " + ghost.name + "</p>"