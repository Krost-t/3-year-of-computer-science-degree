from pymongo import MongoClient

ADMIN_LOGIN = '51236497465'
ADMIN_KEY = "01lj!d-ma14CC-Dmr5?"
# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
#  permet de générer toutes les données chiffrées. Par exemple, elle permet de générer les cookies.
SECRET_KEY = "BU+Ngo9Bov#O;5P.Yw|dHW!"


client = MongoClient('Localhost', 27017)
register = client.a_verifier
db = client.client_app
