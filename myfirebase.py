import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#before running install: pip install firebase_admin

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#will look up for the user's information and upload his info
user = auth.get_user_by_email(email)
print('Successfully fetched user data: {0}'.format(user.uid))

#set documents with known IDs
data = {'food': 'Butter', 'expiration date': 23}
db.collection('person').document('Jenny').set(data) #document reference

#merging
db.collection('person').document('Jenny').set({'food': 'Cheese'}, merge=True)

#adds new collection to the file
db.collection('person').document('Jenny').collection('Meat').add({'food': 'Beaf', 'expiration date': 22})
db.collection('person').document('Jenny').collection('Fruits').add({'food': 'Apple', 'expiration date': 5})

#deletes a document with known IDs
db.collection('person').document("food").delete()

#deletes a field with known IDs
db.collection('person').document("food").update("food_item", firestore.DELETE_FIELD)

#deletes a document with a known IDs
docs = db.collection('person').where("expiration date", 25).get()
for doc in docs:
    key = doc.id
    db.collection('person').document(key).delete()

#deletes a field with unknown ID
docs = db.collection('person').where("expiration date", 33).get()
for doc in docs:
    key = doc.id
    db.collection('person').document(key).update("expiration date", firestore.DELETE_FIELD)

#seletes all documents in a collection
docs = db.collection('person').get()
for doc in docs:
    db.collection('person').document(key).delete()

#adding documents with auto IDs
#db.collection('person').add({'food': 'Butter', 'expiration date': 23})

'''
data = {'food': 'Butter', 'expiration date': 23}
db.collection('person').add(data)
    .then(function(){
    console.log("Successfully displayed an info!");         # adding a named document
})
    .catch(function(error){
        console.error("Error writing document: ", error);
    })

db.collection('person').get()
    .then(function(querySnapshot){
        querySnapshot.forEach(function(doc){            # supposed to retrieve the document
            sendForVerification(doc.data())
        })
    })
'''

#set documents with auto IDs
#db.collection('person').document().set(data) #document reference
