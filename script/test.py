import os
import face_recognition
import time

start = time.time()
dir = os.getcwd() + "/bd/"
dbEncodigs = []# indice 0-> nombre | 1:-> encodings

for i,name in enumerate(os.listdir(dir)):

    person=[]
    person.append(name)

    for img in os.listdir(dir+name):

        img_path = dir+name+"/"+img
        picture = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(picture)

        person.append(encoding)

    dbEncodigs.append(person)
    if i%10 == 0:
    	print(i)


end =time.time()

print(end-start)


        
    