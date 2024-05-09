from sentence_transformers import SentenceTransformer, util
from PIL import Image

list = [
    "images/IMG_0008.jpg", 
    "images/IMG_0271.jpg",
    "images/IMG_0335.jpg",
    "images/IMG_0618.jpg",
    "images/IMG_0678.jpg",
    "images/IMG_0968.jpg",
    "images/IMG_2331.jpg",
    "images/IMG_3102.jpg",
    "images/IMG_3137.jpg",
    "images/IMG_3213.jpg"
]

model = SentenceTransformer('clip-ViT-B-32')

image_list = []
for image in list:
    image_list.append(Image.open(image))


image_emb = model.encode(image_list)

print("Begin Testing:\n")

while True:
    user_input = input()
    text_embedding = model.encode([user_input])
    cos_sim = util.cos_sim(text_embedding, image_emb)[0]
    print(cos_sim)

    max = cos_sim[0]
    index = 0
    for idx, element in enumerate(cos_sim):
        if element > max:
            max = element
            index = idx

    img_to_show = Image.open(list[index])
    img_to_show.show()
