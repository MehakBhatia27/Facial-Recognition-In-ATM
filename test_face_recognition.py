import face_recognition
import pandas as pd

# Load the database CSV file into a DataFrame
database_filename = 'D:\\college 5th sem\\Research Methodology\\customer_dataset - Sheet1.csv'  # Replace with your actual database file
database = pd.read_csv(database_filename)

# Function to find a match in the database
def find_match(user_image_path, database):
    # Load the user image
    user_image = face_recognition.load_image_file('C:\\Users\\hp\\Downloads\\Happy-46.jpg')
    user_face_encodings = face_recognition.face_encodings(user_image)

    if len(user_face_encodings) == 0:
        return "No face found in the user image"

    # Loop through each face in the database
    for index, row in database.iterrows():
        known_image = face_recognition.load_image_file(row['Image Url'])
        known_face_encodings = face_recognition.face_encodings(known_image)

        if len(known_face_encodings) == 0:
            continue  # Skip if no face found in the known image

        # Compare the user face with each face in the database
        results = face_recognition.compare_faces(known_face_encodings, user_face_encodings[0])
        
        if True in results:
            return "Match Found"  # A match was found in the database

    return "Nothing Found"  # No match found in the database

# Get the user's image path from the user
user_image_path = input('C:\\Users\\hp\\Downloads\\Happy-46.jpg')

# Find a match in the database
result = find_match(user_image_path, database)

# Print the result
print(result)
