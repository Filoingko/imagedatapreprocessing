# import the necessary packages
from PIL import Image
import argparse
from imutils import paths

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# original data directory
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
# after resizing save in this directory
ap.add_argument("-s", "--savepath", type=str, required=True,
	help="path to output dataset")
args = vars(ap.parse_args())

print("[INFO] resizing images...")
imagePaths = list(paths.list_images(args["dataset"]))
savePath = args["savepath"]

i = 0
# loop over our image paths
for imagePath in imagePaths:
    i = i+1
    # load the input image and resizing
    image = Image.open(imagePath)
    new_image = image.resize((225, 225))
    # save images in new directory
    new_image.save(savePath+str(i)+'.jpeg')




