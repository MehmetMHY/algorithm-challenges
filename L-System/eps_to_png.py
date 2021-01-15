from PIL import Image
import sys

augs = list(sys.argv)

if(len(augs) != 3):
    print("Invalid Arugments!")
    print(" *EX: python3 eps_to_png.py sqaures.eps sqaures.png")
else:
    eps_file = str(augs[1])
    png_name = str(augs[2])

    image = Image.open(eps_file)
    new_image = image.convert('RGBA')
    new_image.save(png_name, lossless = True)
    
    print("The " + eps_file + " file has been converted and saved to " + png_name + ".")


