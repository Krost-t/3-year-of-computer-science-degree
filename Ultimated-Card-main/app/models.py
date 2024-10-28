

import random
from flask import request

from config import *


def create_user():
    nombre = random.randint(1000000000, 9999999999)
    return {
        "nom": request.form['name'],
        "prenom" : request.form['prenom'],
        "password" : request.form['pwd'],
        "adresse" : request.form['adresse'],
        "age" : request.form['age'],
        "numid" : nombre,
        "code_postal" : request.form['code_postal'],
        "ville" : request.form['ville'],
        "mail" : request.form['mail'],
        "date_de_naissance" : request.form['date-naissance']                     
        }
    
def mdp_correct():
    boolean = False
    if request.form['pwd'] == request.form['pwd2']:
        boolean = True
    return boolean

def admin_login():
    boolean = False
    if request.form['pwd-connect'] == ADMIN_KEY:
        if request.form['num-connect'] == ADMIN_LOGIN:
            boolean = True
    return  boolean

def connect_user(id,password):
   return register.users.find_one({"mail":id},{"password":password})