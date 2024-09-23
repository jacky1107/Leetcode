import os
import usb.core
import usb.util

path1 = "F:\\Photos\\AllPhotosFromi12_04062023"
path2 = "本機\Apple iPhone\Internal Storage\DCIM"

dev = usb.core.find(idProduct="12A8") #, idProduct="12A8")
if dev is None:
    raise ValueError("iPhone not found")

file_path = dev[0][(0,0)][0].filename
print("iPhone file path:", file_path)

for file_path in os.listdir(path2):
    print(len(os.listdir(os.path.join(path1, file_path))))
    