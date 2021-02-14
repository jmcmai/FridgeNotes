import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from kivymd.app import App
import requests
import json

#before running install: pip install firebase_admin

cred = credentials.Certificate("fridgenotes-f5c47-firebase-adminsdk-djtrj-f230380d99.json")
firebase_admin.initialize_app(cred)


class MyFirebase():
    wak = 'AIzaSyBL6nY4funOgC_Yiw0no4zOdixr0kWAOlM'
    db = firestore.client() 
    def sign_up(self, email, password):
        #send email to firebase
        #firebase will return localid(userid), authtoken(idtoken), refreshtoken
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {"email": email, "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        print(sign_up_request.ok)
        print(sign_up_request.content.decode())

        sign_up_data = json.loads(sign_up_request.content.decode())
        if sign_up_request.ok == True:
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            # Save refreshToken to a file
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            # save local id to a variable in main app class
            App.get_running_app().local_id = localId
            App.get_running_app().id_token = idToken

            #create new key and add initial info:
            initial_data = {'avatar': 'fridge.png'}
            self.db.collection(localId).document(u'initial').set(initial_data)

            #send back to login screen
            App.get_running_app().root.current = 'login_screen'

        if sign_up_request.ok == False:
                error_data = json.loads(sign_up_request.content.decode())
                error_message = error_data["error"]['message']
                App.get_running_app().root.ids['sign_up_screen'].ids['invalid_sign_up'].text = error_message
        pass
    
    def sign_in(self, email, password):
        """Called if a user tried to sign up and their email already existed."""
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.wak
        signin_payload = {"email": email, "password": password, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        sign_up_data = json.loads(signin_request.content.decode())
        app = App.get_running_app()

        if signin_request.ok == True:
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            print(localId)
            idToken = sign_up_data['idToken']

            # Save localId to a variable in main app class
            # Save idToken to a variable in main app class
            app.local_id = localId
            app.id_token = idToken

            app.signed_in()
            App.get_running_app().root.current = 'list_screen'
            print('true!')
        elif signin_request.ok == False:
            error_data = json.loads(signin_request.content.decode())
            error_message = error_data["error"]['message']
            app.root.ids['login_screen'].ids['wrong_login'].text = error_message.replace("_", " ")

    def get_database_data(self, loginId):
        grocery_items = {}
        item_number = 0
        docs = self.db.collection(loginId).stream()
        for doc in docs:
            if doc.id != 'initial':
                d = doc.to_dict()
                temp = {item_number:d}
                grocery_items.update(temp)
                item_number += 1
        return grocery_items

                




#person could be local id
#stream gets every food item out of their fridge
#each document is a food item

# doc_ref = db.collection(u'person').stream()
# ordered_docs = db.collection(u'person').order_by(u'').stream()


# for doc in ordered_docs:
#     d = doc.to_dict()
#     for key, value in d.items():
#         if key == 'name':
#             print(d[key])
    #print(d['name'])
    # print(f'{doc.id} => {doc.to_dict()}')

# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

#set documents with known IDs
# data = {'name': 'Pear', 'expiration date': "2021-03-12", 'quantity': 4}
# db.collection('person').add(data) #document reference

# #will look up for the user's information and upload his info
# user = auth.get_user_by_email(email)
# print('Successfully fetched user data: {0}'.format(user.uid))


# #merging
# db.collection('person').document('Jenny').set({'food': 'Cheese'}, merge=True)

# #adds new collection to the file
# db.collection('person').document('Jenny').collection('Meat').add({'food': 'Beaf', 'expiration date': 22})
# db.collection('person').document('Jenny').collection('Fruits').add({'food': 'Apple', 'expiration date': 5})

# #deletes a document with known IDs
# db.collection('person').document("food").delete()

# #deletes a field with known IDs
# db.collection('person').document("food").update("food_item", firestore.DELETE_FIELD)

# #deletes a document with a known IDs
# docs = db.collection('person').where("expiration date", 25).get()
# for doc in docs:
#     key = doc.id
#     db.collection('person').document(key).delete()

# #deletes a field with unknown ID
# docs = db.collection('person').where("expiration date", 33).get()
# for doc in docs:
#     key = doc.id
#     db.collection('person').document(key).update("expiration date", firestore.DELETE_FIELD)

# #seletes all documents in a collection
# docs = db.collection('person').get()
# for doc in docs:
#     db.collection('person').document(key).delete()

# #adding documents with auto IDs
# #db.collection('person').add({'food': 'Butter', 'expiration date': 23})

# '''
# data = {'food': 'Butter', 'expiration date': 23}
# db.collection('person').add(data)
#     .then(function(){
#     console.log("Successfully displayed an info!");         # adding a named document
# })
#     .catch(function(error){
#         console.error("Error writing document: ", error);
#     })

# db.collection('person').get()
#     .then(function(querySnapshot){
#         querySnapshot.forEach(function(doc){            # supposed to retrieve the document
#             sendForVerification(doc.data())
#         })
#     })
# '''

# #set documents with auto IDs
# #db.collection('person').document().set(data) #document reference
