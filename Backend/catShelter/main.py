from flask import *
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

#Checking out the available cats
@app.route("/checkCats")
def checkCats():
    con = sqlite3.connect("catBase.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from cats")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/saveCat/", methods=["POST"])
def saveCat():
    try:
        data = request.get_json(force=True)

        #Addig the needed data
        catName = data["catName"]
        catGender = data["catGender"]
        catAge = data["catAge"]
        with sqlite3.connect("catBase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into cats (catName, catGender, catAge) values (?,?,?)", (catName, catGender, catAge))
            con.commit()
    except:
        con.rollback()
    finally:
        return catName
        con.close()


@app.route("/adoptCat", methods = ["POST"])
def adopt():
    information = ""
    data = request.get_json(force=True)
    id = str(data["id"])
    with sqlite3.connect("catBase.db") as con:
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM cats WHERE id = ?", id)
            information = "Successfully adopted"
            return information
        except:
            information = "Something went wrong with adopting a cat"
            return information




@app.route("/editCatData", methods=["POST"])
def editCat():
    try:
        information = ""
        data = request.get_json(force=True)
        id = data["id"]
        catName = data["catName"]
        catGender = data["catGender"]
        catAge = data["catAge"]

        with sqlite3.connect("catBase.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE cats SET catName=?, catGender=?, catAge=? WHERE id=?", (catName, catGender, catAge, id))
            con.commit()
    except:
        con.rollback()
        information = "Something went wrong with editing a cat"
        return information
    finally:
        information = "Cat was successfully edited"
        con.close()
        return information


if __name__ == "__main__":
    app.run(debug=True)