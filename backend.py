from sentence_transformers import SentenceTransformer, util
from PIL import Image

list = [
"IMG_0008.jpg", 
"IMG_0271.jpg",
"IMG_0335.jpg",
"IMG_0618.jpg",
"IMG_0678.jpg",
"IMG_0968.jpg",
"IMG_2331.jpg",
"IMG_3102.jpg",
"IMG_3137.jpg",
"IMG_3213.jpg"
]

model = SentenceTransformer('clip-ViT-B-32')

image_list = []
for image in list:
    image_list.append(Image.open(image))


