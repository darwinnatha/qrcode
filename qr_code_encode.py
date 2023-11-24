import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class GenerateQRCodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Générateur de Code QR")

        # Créer les composants de l'interface
        self.label = Label(master, text="Entrez le texte pour le code QR:")
        self.label.pack()

        self.entry = Entry(master, width=40)
        self.entry.pack()

        self.button_generate = Button(master, text="Générer le code QR", command=self.generate_qr)
        self.button_generate.pack()

        self.image_label = Label(master)
        self.image_label.pack()

        self.button_save = Button(master, text="Enregistrer le code QR", command=self.save_qr)
        self.button_save.pack()

    def generate_qr(self):
        # Récupérer le texte de l'entrée
        chaine_a_encoder = self.entry.get()

        # Générer le code QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(chaine_a_encoder)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Afficher l'image générée dans l'interface
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

        # Sauvegarder l'image générée pour pouvoir l'enregistrer ultérieurement
        self.generated_image = img

    def save_qr(self):
        # Vérifier si une image a été générée
        if hasattr(self, 'generated_image'):
            # Demander à l'utilisateur où enregistrer le fichier
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            
            # Si l'utilisateur a choisi un fichier, enregistrer l'image
            if file_path:
                self.generated_image.save(file_path)
                print(f"Le code QR a été enregistré sous {file_path}")
        else:
            print("Veuillez d'abord générer un code QR.")

# Créer et lancer l'application Tkinter
root = Tk()
app = GenerateQRCodeApp(root)
root.mainloop()
