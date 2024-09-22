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
    
    #let's find hash
    # 6e93b81e0c4ae59a181c3678f16dde050a5232ba   <----hash
    print("commit number 2")
    print("chtoto zacomitili nomer1")
    print("chtoto zacomitili nomer2")

