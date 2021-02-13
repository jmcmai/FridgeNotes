import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#before running install: pip install firebase_admin

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {'food': 'Butter', 'expiration date': 23}
db.collection('person').add(data)

#db.collection('person').add({'food': 'Butter', 'expiration date': 23})