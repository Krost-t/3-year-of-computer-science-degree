from flask import Flask, render_template, request, redirect, url_for
from .models import *

app = Flask(__name__)
# il faut ouvrir le port du parfeu au préalable



@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route('/formulaire/')
def formu():
    return render_template("form.html")


@app.route('/info/')
def info():
    return render_template("info.html")


@app.route('/enregistrer/',methods=["GET","POST"])
def enregistrer():
    if request.method == "POST":
        if mdp_correct():
            register.users.insert_one(create_user())
        else:
            return render_template("form.html")
        return render_template("form.html")
    else:
        return "error"
    
    
@app.route('/connexion/',methods=["GET","POST"])
def connexion():
   
    id = request.form['mail-connect']
    mdp = request.form['pwd-connect']

    return render_template("account.html",
                           nom = connect_user(id,mdp)['nom'],
                           prenom = connect_user(id,mdp)['prenom'],
                           age = connect_user(id,mdp)['age'],
                           dateOfB = connect_user(id,mdp)['date_de_naissance'],
                           mail = connect_user(id,mdp)['mail'],
                           adresse = connect_user(id,mdp)['adresse'],
                           codeP = connect_user(id,mdp)['code_postal'],
                           ville = connect_user(id,mdp)['ville'],
                           password = connect_user(id,mdp)['password'])

