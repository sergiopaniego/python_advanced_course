from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client(project='gcp-course-example', database='gcpcourseexample')


# Retrieve the document
user_ref = db.collection('users').document('user_0')
user_data = user_ref.get()

if user_data.exists:
    print(f'User data: {user_data.to_dict()}')
else:
    print('No such user found.')
