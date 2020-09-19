import PIL
import os

def main():
"""
Creates noise in our dataset to train the denoising model
"""
    out_dir = ""
    images_dir = ""
    for image in os.listdir(images_dir):
        if(image.endswith(".jpg")):
            im = PIL.Image.open(os.path.join(images_dir, image))
            dims = im.size
            hgt = dims[0]*0.5
            wit = dims[1]*0.5
            im = im.resize((hgt,wit),PIL.Image.ANTIALIAS)
            im.save(out_dir, quality=95)
if __name__ == '__main__':
    main()
