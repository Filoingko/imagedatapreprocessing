# import the necessary packages
import os
import imagehash
from PIL import Image

def get_image_hash(image_path):
    # generate hash for the image using average hashing
    img = Image.open(image_path)
    return imagehash.average_hash(img)

def remove_duplicate_images(image_folder, threshold=5):
    # remove duplicate or similar images based on their hashes
    image_hashes = {}
    duplicates = []

    # iterate through all files in the folder
    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        
        if os.path.isfile(image_path):
            try:
                # get the image hash
                image_hash = get_image_hash(image_path)

                # check if this hash is already seen
                for existing_hash, existing_files in image_hashes.items():
                    if abs(image_hash - existing_hash) < threshold:
                        # if the hash difference is small, it's a duplicate
                        print(f"Duplicate found: {filename} is similar to {existing_files[0]}")
                        duplicates.append(image_path)
                        break
                else:
                    # if it's not a duplicate, add it to the hash dictionary
                    image_hashes[image_hash] = [filename]
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # remove the duplicates
    for duplicate in duplicates:
        print(f"Removing duplicate: {duplicate}")
        os.remove(duplicate)

# data directory
image_folder = "./Data/ResizedImages/Other/"
remove_duplicate_images(image_folder)
