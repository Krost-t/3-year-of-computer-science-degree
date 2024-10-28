from flask import Flask, redirect, render_template, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
import json
# mongo db null sur des gros volume de donne 

app = Flask(__name__)

try:

    mongo = pymongo.MongoClient(
        host="db",
        port= 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.identity
    mongo.server_info()
except:
    print("Error")


@app.route("/")
def acceuil():
    return render_template("home.html")


@app.route("/formulaire/")
def forum():
    return render_template("formulaires.html")


@app.route("/traitement/",methods=["POST"])
def create_user():
    donnees = request.form
    try:
        user = {"name": donnees.get('nom'),
        "last_name":donnees.get('prenom'),
        "e-mail":donnees.get('email'),
        "age":donnees.get('age'),
        "adress": donnees.get('adresse')}
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        #for attr in dir(dbResponse):
        #print(attr)
        return Response(
            response = json.dumps(
                {"message":"user created",
                "id":f"{dbResponse.inserted_id}"}),
            status = 200,
            minetype = "application/json")
    except Exception as ex:
        print("********************************")
        print(ex)
        print("********************************")
    return "c'est fait"


@app.route("/Login/", methods=["POST","GET"])
def info_user():
    try:
        data = list(db.users.find())
        for x in data:
            x["_id"] = str(x["_id"])
        return Response(
            response= json.dumps(data),
            status = 500,
            mimetype="application/json"
        )
    except Exception as e:
        print(e)
        return Response(
            response= json.dumps({"message": "cannot read data from"}),
            status = 500,
            mimetype="application/json"
        )

        


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')