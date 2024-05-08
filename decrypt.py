import os 
from cryptography.fernet import Fernet

files = []

# if you encrypt in disk :)
# root_dir = 'D:\\'
# for root, dirs, files in os.walk(root_dir):
#     for filename in files:
#             file_path = os.path.join(root, filename)
#             files.append(file_path)

for file in os.listdir():
    if file == 'animesom.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)

password = 'anjaymabar' # is password for key encrypt


with open('thekey.key', 'rb') as thekey:
    iskey = thekey.read()

lock = str(input('What password bro??: '))
if lock == password:
    for file in files:
        with open(file, 'rb') as thefile:
            content = thefile.read()
        content_decrypt = Fernet(iskey).decrypt(content)
        with open(file, 'wb') as thisfile:
            thisfile.write(content_decrypt)
