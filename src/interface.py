import os
import rawpy
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def process_images():
    quality = int(quality_entry.get())
    extension = extension_var.get()

    if quality < 0 or quality > 100:
        result_label.config(text="Please choose a number between 0 and 100")
        return

    if extension.lower() not in [".png", ".jpg"]:
        result_label.config(text="Please choose either '.png' or '.jpg'.")
        return

    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()

    os.makedirs(output_dir, exist_ok=True)

    files = os.listdir(input_dir)
    for file in files:
        if file.endswith(".CR2"):
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + extension)

            with rawpy.imread(input_file_path) as raw:
                rgb = raw.postprocess()
                image = Image.fromarray(rgb)
                image.save(output_file_path, quality=quality)

    result_label.config(text="Process completed.")

def browse_input_dir():
    input_dir = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, input_dir)

def browse_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

# Create the main window
root = tk.Tk()
root.title("RAW Image Processor")

# Input directory
input_dir_label = tk.Label(root, text="Input Directory:")
input_dir_label.grid(row=0, column=0)
input_dir_entry = tk.Entry(root, width=50)
input_dir_entry.grid(row=0, column=1)
browse_input_button = tk.Button(root, text="Browse", command=browse_input_dir)
browse_input_button.grid(row=0, column=2)

# Output directory
output_dir_label = tk.Label(root, text="Output Directory:")
output_dir_label.grid(row=1, column=0)
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1)
browse_output_button = tk.Button(root, text="Browse", command=browse_output_dir)
browse_output_button.grid(row=1, column=2)

# Quality
quality_label = tk.Label(root, text="Quality (0-100):")
quality_label.grid(row=2, column=0)
quality_entry = tk.Entry(root)
quality_entry.grid(row=2, column=1)

# Extension
extension_label = tk.Label(root, text="Extension (.png/.jpg):")
extension_label.grid(row=3, column=0)
extension_var = tk.StringVar(root, ".png")
extension_dropdown = tk.OptionMenu(root, extension_var, ".png", ".jpg")
extension_dropdown.grid(row=3, column=1)

# Process Button
process_button = tk.Button(root, text="Process Images", command=process_images)
process_button.grid(row=4, column=1)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3)

root.mainloop()
