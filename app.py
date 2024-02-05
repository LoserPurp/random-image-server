import os
import random
from flask import Flask, send_file

app = Flask(__name__)

img_folder = 'img'

#list of all image files in the folder
img_files = [f for f in os.listdir(img_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

@app.route('/')
def serve_random_image():
    random_img = random.choice(img_files)

    img_path = os.path.join(img_folder, random_img)

    return send_file(img_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=7235)