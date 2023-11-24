import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import zxing

class DecodeQRCodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Décodage de Code QR")

        # Créer les composants de l'interface
        self.label = Label(master, text="Sélectionnez un fichier QRCode à décoder:")
        self.label.pack()

        self.button_browse = Button(master, text="Parcourir", command=self.browse_file)
        self.button_browse.pack()

        self.image_label = Label(master)
        self.image_label.pack()

        self.button_decode = Button(master, text="Décoder le QRCode", command=self.decode_qr)
        self.button_decode.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def browse_file(self):
        # Demander à l'utilisateur de choisir un fichier QRCode
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        # Afficher l'image choisie dans l'interface
        if file_path:
            img = Image.open(file_path)
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            self.selected_image_path = file_path

    def decode_qr(self):
        # Vérifier si une image a été sélectionnée
        if hasattr(self, 'selected_image_path'):
            # Utiliser la bibliothèque zxing pour décoder le QRCode
            reader = zxing.BarCodeReader()
            barcode = reader.decode(self.selected_image_path)

            # Afficher le résultat dans l'interface
            if barcode:
                result_text = f"Contenu du QRCode : {barcode.raw}"
            else:
                result_text = "Aucun QRCode trouvé dans l'image."

            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Veuillez d'abord sélectionner un fichier QRCode.")

# Créer et lancer l'application Tkinter
root = Tk()
app = DecodeQRCodeApp(root)
root.mainloop()
