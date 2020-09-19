from PIL import Image
import os

def main():
    """
    Creates noise in our dataset to train the de-noising model
    """
    out_dir = ""
    images_dir = ""
    for image in os.listdir(images_dir):
        if(image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg")):
            img = Image.open(os.path.join(images_dir, image))
            dims = img.size
            hgt = dims[0]*0.5
            wit = dims[1]*0.5
            CompressResult = img.resize((hgt,wit),Image.ANTIALIAS)
            DecompressResult = "REPLACE - DO NOT USE LIKE THIS"
            DecompressResult.save(out_dir, quality=95)


if __name__ == '__main__':
    main()
