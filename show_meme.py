from PIL import Image
import matplotlib.pyplot as plt
import random 


if __name__ == '__main__':
    a=random.randint(1,3)
    image_path=str('memes1/meme')+str(a)+str('.jpg')
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


