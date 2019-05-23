import os
import face_recognition
import time
from operator import itemgetter

def detect_faces_in_image():

     # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)

                #picture_of_vizcarra = face_recognition.load_image_file("fotos_bd/vizcarra.png")
                #known_face_encoding = face_recognition.face_encodings(picture_of_vizcarra)[0]
    global dbEncodnigs
    global distances

    file_stream = "/home/xrok/Documents/Tarea2_BD/script/bd/test/test.jpg"

    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    #is_vizcarra = False

    if len(unknown_face_encodings) > 0:
        face_found = True
        # See if the first face in the uploaded image matches the known face of Obama
                #match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        # Your can use the distance to return a ranking of faces <face, dist>.
        
        

        for person in dbEncodings:
            
            distance=[]
            dist_prom=0
            cant=0
            #distance.append(person[0])
            #print(person[0],"cant imagenes",len(person)-1)
                
            for img in range(1,len(person)):
                
                #print("imagen numero: ",img)
                dist= face_recognition.face_distance(person[img], unknown_face_encodings[0])

                #print(dist)
                
                if len(dist):
                    cant+=1
                    dist_prom+= dist[0]

            dist_prom= dist_prom/cant
            #distance.append(dist_prom)
            distances.append([person[0],dist_prom])


        #print(distances[0][1])
        #distances.sort(key= lamba x: x[1])
        distances.sort(key=itemgetter(1))

        for x in range(len(distances)):
            print(distances[x][:])
        


dir = os.getcwd() + "/bd/"
dbEncodings = []# indice 0-> nombre | 1:-> encodings
distances=[]

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

detect_faces_in_image()



        
    