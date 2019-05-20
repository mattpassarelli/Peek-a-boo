import os
import face_recognition
import cv2
import tensorflow as tf
import numpy as np

print("Starting...")

video = cv2.VideoCapture(0)

path = "images"
images_names = os.listdir(path)
known_face_encodings = []
known_face_names = []

print("Started Encoding Template Photos")
# We encode the images from our folder to get a list of
# people we can recognize. File names are the Names used 
# for people
for imgs in images_names:
    print("Encoding image: " + imgs)
    name = imgs.split(".")
    known_face_names.append(name[0])
    image_path = path + "/" + imgs
    image_file = face_recognition.load_image_file(image_path)
    image_face_encoding = face_recognition.face_encodings(image_file)[0]
    known_face_encodings.append(image_face_encoding)

print("Done Encoding Template Photos")

processFrame = True

print("Starting Video Recognition")
# Start the video and recognition
while True:
    ret, frame = video.read()

    FPS = 20.0
    FrameSize = (frame.shape[1], frame.shape[0])
    isColor = 1  # flag for color(true or 1) or gray (0)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('uselessVideo.avi', fourcc, FPS, FrameSize)

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    if processFrame:
         # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    processFrame = not processFrame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Saving the current image from the webcam for testing.
        FaceFileName = "test.jpg"
        cv2.imwrite(FaceFileName, frame)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 0), cv2.FILLED)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (left + 6, bottom - 6)
        fontScale = 0.5
        fontColor = (255, 255, 255)
        lineType = 1

        # TODO:
        # This is the text that is added to the box
        # I should add those age and gender detectors
        # when I have internet that isn't on a train
        cv2.putText(frame, "Name: " + name, bottomLeftCornerOfText,
                    font, fontScale, fontColor, lineType)

    #Show the video Feed
    out.write(frame)
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("User Quit")
        break


print("Finishing up!")
# Release my hooks
video.release()
cv2.destroyAllWindows()

# Delete the files it creates because I don't want
# that many pictures of me on Github lol
os.remove("uselessVideo.avi")
os.remove("test.jpg")

print("Done!")
