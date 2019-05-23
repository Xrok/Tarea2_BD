import face_recognition
import os
import numpy
from flask import Flask, jsonify, request, redirect
from operator import itemgetter


# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



app = Flask(__name__)
#---------DB Encodings --------
#
dir = os.getcwd() + "/bd/"
dbEncodings = []# indice 0-> nombre | 1:-> encodings
distances = []

for i,name in enumerate(os.listdir(dir)):

    person=[]
    person.append(name)

    for img in os.listdir(dir+name):

        img_path = dir+name+"/"+img
        picture = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(picture)

        

        person.append(encoding)

    print("Loading DB: ",100*i/len(os.listdir(dir)) ,"%")

    dbEncodings.append(person)
        
    



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])

def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Top 5 !</title>
    <h1>Cargar una foto descubre el top5 !</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Cargar">
    </form>
    '''


def detect_faces_in_image(file_stream):



     # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    global dbEncodnigs
    global distances


    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    

    if len(unknown_face_encodings) > 0:
        face_found = True
        # See if the first face in the uploaded image matches the known face of Obama

        for person in dbEncodings:
            
            distance=[]
            dist_prom=0
            cant=0
                
            for img in range(1,len(person)):
                
                dist= face_recognition.face_distance(person[img], unknown_face_encodings[0])

                if len(dist):
                    cant+=1
                    dist_prom+= dist[0]

            dist_prom= dist_prom/cant

            distances.append([person[0],dist_prom])


        distances.sort(key=itemgetter(1))


        result = {
        "Top1": [ distances[0][0],distances[0][1]],
        "Top2": [ distances[1][0],distances[1][1]],
        "Top3": [ distances[2][0],distances[2][1]],
        "Top4": [ distances[3][0],distances[3][1]],
        "Top5": [ distances[4][0],distances[4][1]]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)