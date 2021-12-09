import os
from UnityPy import AssetsManager
from collections import Counter
import zipfile
import re
import UnityPy

def mesh():
    mesh : Mesh
    asset_path = 'files/'
    destination_folder = 'Mesh/'
    os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir('files'):
    filename = "files/" + filename
    env = UnityPy.load(filename)
    for obj in env.objects:
        tpe = str(obj.type).split('.')[1]
        if tpe == "Mesh":
            data = obj.read()
            dest = os.path.join("Mesh", data.name)
            dest, ext = os.path.splitext(dest)
            dest = dest + '.obj'
            print("Extracting... " + data.name)
            export = data.export().encode("utf8")
            file = open(dest, 'wb')
            file.write(export)
