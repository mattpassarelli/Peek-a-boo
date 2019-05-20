# Peek-a-boo

Facial recognition software written using Python with cv2 (for webcam access) and face_recognition, an open source python library
used to do facial recognition.

# Installation and Prerequisites
Make sure you have done the installation needed for face_recognition (and it's dependency dlib), which you can find out how to do
from the [face_recognition repository](https://github.com/ageitgey/face_recognition).

Then just clone this repository by downloading the zip or running `git clone https://github.com/mattpassarelli/Peek-a-boo.git`

# Usage
Usage is easy. Put a picture of yourself you want to use in the "images" folder with your Name as the file name. Since I have git ignore my photos (so they don't stay in this repository), you'll need to create a folder called `images`. The software used the file's name to name the face it detects, so make sure it's named right. Then just run the program using your preferred method, let it encode the pictures you have, and let it detect you!

# End Notes
It doesn't really do much right now, which is fine. I hope to find an actual need for this at some point and integrate it then.
Possibly something like image recognition or into a simple AI.