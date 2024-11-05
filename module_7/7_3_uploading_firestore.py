from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client(project='gcp-course-example', database='gcpcourseexample')

# Prueba un código simple para escribir en Firestore
doc_ref = db.collection('test').document('test_doc')
doc_ref.set({'test_field': 'test_value'})
print('Test document written to Firestore.')


# Create a new document in the "users" collection
doc_ref = db.collection('users').document('user_1')
doc_ref.set({
    'name': 'Alice'
})

print('User data written to Firestore.')
