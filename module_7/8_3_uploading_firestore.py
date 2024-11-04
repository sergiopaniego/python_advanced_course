from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Create a new document in the "users" collection
doc_ref = db.collection('users').document('user_1')
doc_ref.set({
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
})

print('User data written to Firestore.')
