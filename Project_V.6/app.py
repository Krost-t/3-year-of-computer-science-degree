import json
from flask import Flask, Response, render_template, request 
import pymongo



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
def home():
    return render_template("form.html")

@app.route("/send", methods=["POST","GET"])
def create_user():
    donnees = request.form
    try:
        user = {"name": donnees.get('nom'),
        "last_name":donnees.get('prenom'),
        "e-mail":donnees.get('email'),
        "age":donnees.get('age'),
        "adress": donnees.get('adresse'),
        "doc":donnees.get('doc')}
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


@app.route("/send/sante", methods=["POST","GET"])
def create_user_sante():
    db = mongo.sante
    mongo.server_info()
    donnees = request.form
    try:
        user = {"taile": donnees.get('taille'),
        "gp_sangin":donnees.get('GPsanguin'),
        "md-traitant":donnees.get('traitant'),
        "age":donnees.get('age')}
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


@app.route("/see bdd")
def see_users():
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
        
        
@app.route("/see/sante bdd")
def see_users_sante():
    db = mongo.sante
    mongo.server_info()
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



if __name__ == "__main__":
    app.run(debug=True)