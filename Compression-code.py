from PIL import Image
import tkinter as tk
from tkinter import filedialog
import io

def image_to_binary_string(image_path, threshold=128):
    try:
        # Opens the image file
        with Image.open(image_path) as img:
            # Conversion au niveaux de gris
            img_gray = img.convert('L')
            
            # Conversion a une image binaire
            img_binary = img_gray.point(lambda p: 0 if p < threshold else 1, mode='1')
            
            # Conversion d'image binaire a string binaire
            binary_string = ''.join(str(pixel) for pixel in img_binary.getdata())
            
            return binary_string
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None




def rle_encode(binary_string):
    encoded_string = "" #Initialisation d'un string vide ou on va enregistrer le string binaire compresse
    count = 1 #Compteur des repetitions
    prev_char = binary_string[0] #Init du compteur du charactere actuel
    #Loop
    for char in binary_string[1:]:
        if char == prev_char:
            count += 1
        else:
            #Arret de Loop, Enregistrement des valeurs et initialisation a nouveau
            encoded_string += f"{count},{prev_char} "
            count = 1
            prev_char = char

    encoded_string += f"{count},{prev_char}"
    return encoded_string


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.bmp")])
    if file_path:
        binary_string = image_to_binary_string(file_path)
        if binary_string:
            print("Binary string representation of the image:")
            print(binary_string)
            encoded_string = rle_encode(binary_string)
            print("RLE encoded string:")
            print(encoded_string)

        data = encoded_string
        file_path = "rlestring2.txt"
        with open(file_path, 'w') as f:
                f.write(data)
        return file_path

image_path = select_image()
root = tk.Tk()
root.withdraw()
button = tk.Button(root, text="Select Image", command=select_image)
button.pack()
root.mainloop()







    
