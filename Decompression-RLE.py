from PIL import Image
import tkinter as tk
from tkinter import filedialog


def rle_decode(encoded_file_path):
    try:
        with open(encoded_file_path, 'r') as file:
            encoded_string = file.read()
        #Creer un fichier string ou on va enregistrer le string binaire
        decoded_string = ""
        parts = encoded_string.split()
        for part in parts:
            count, char = part.split(',')
            decoded_string += int(count) * char
        return decoded_string
    except Exception as e:
        print("An error occurred:", e)
        return None



def binary_string_to_image(decoded_string, width, height):
    try:
        # Creation d'une nouvelle image /1 = 1bit par pixel
        img = Image.new('1', (width, height))
        
        # Conversion du string binaire a des valeurs des pixels
        pixels = [int(decoded_string[i:i+1]) * 255 for i in range(0, len(decoded_string))]
        
        # Associer les valeurs des pixels au pixels dans l'image cree
        img.putdata(pixels)
        
        return img
    except Exception as e:
        print("An error occurred:", e)
        return None


def select_encoded_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

encoded_file_path = select_encoded_file()
#encoded_file_path = "rlestring2.txt"  
decoded_string = rle_decode(encoded_file_path)

width = 64
height = 64
img = binary_string_to_image(decoded_string, width, height)
if img:
    img.show()
    img.save('Decomp.jpg')
print("Done!")
