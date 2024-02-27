import os
import rawpy
from PIL import Image

# Path to the directory containing the RAW images
input_dir = "../img"

# Path to the directory where processed images will be saved
output_dir = "../img_processed"


# Input quality by the user
quality = int(input("What quality do you want, from 0 to 100?"))

if quality >= 0 and quality <= 100:
    print("Valid quality:", quality)
else:
    print("Please choose a number between 0 and 100.") 


#Input of the extension by the user
extension = input("What extension do you want, .png or .jpg?: ")

if extension.lower() == ".png" or extension.lower() == ".jpg":
    print("Valid extension:", extension)
else:
    print("Please choose between '.png' or '.jpg'.")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get the list of files in the input directory
files = os.listdir(input_dir)

# Iterate over each file
for file in files:
    # Check if the file is a RAW file (CR2)
    if file.endswith(".CR2"):
        # Build the full path of the input file
        input_file_path = os.path.join(input_dir, file)
        
        # Build the full path of the output file
        output_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + extension)
        
        # Open the CR2 file and save as PNG
        with rawpy.imread(input_file_path) as raw:
            # Convert to RGB and save as PNG
            rgb = raw.postprocess()
            image = Image.fromarray(rgb)
            image.save(output_file_path, quality=quality) 

print("Process completed.")