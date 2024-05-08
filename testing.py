import cv2
import urllib.request
import numpy as np

def display_image_from_url(image_url):
    try:
        # Mengunduh gambar dari URL
        resp = urllib.request.urlopen(image_url)
        # Membaca gambar dari byte
        image = bytearray(resp.read())
        # Menampilkan gambar
        nparr = np.asarray(image, dtype=np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)

# Contoh penggunaan
image_url = "https://i.pinimg.com/736x/ee/76/6b/ee766b355267a5d0e38d0b5d6f9c951b.jpg"
display_image_from_url(image_url)

# import os

# def display_files_in_disk_d():
#     root_dir = 'D:\\'
#     for root, dirs, files in os.walk(root_dir):
#         for filename in files:
#             file_path = os.path.join(root, filename)
#             print(file_path)

# display_files_in_disk_d()


