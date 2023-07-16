import os
import cv2
import face_recognition



# Get the list of files in the folder
file_list = os.listdir("./images")

l_img = []

# Print the names of the files
for file_name in file_list:
    l_img.append("./images/" + file_name)

for i in l_img:
    img = cv2.imread(i)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    for j in l_img:
        if i == j:
            continue

        img2 = cv2.imread(j)
        rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

        result = face_recognition.compare_faces([img_encoding], img_encoding2)
        print("[ ", i ," == " , j , " ] ", result)


