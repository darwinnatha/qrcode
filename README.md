# Générateur et Décodage de Code QR

## Générateur de Code QR

Ce script Python utilise la bibliothèque `qrcode` pour générer un code QR à partir d'une chaîne de caractères et l'enregistrer dans un dossier spécifié. Il utilise également Tkinter pour créer une interface graphique conviviale.

### Instructions d'utilisation

1. Installez les dépendances en utilisant la commande suivante :
   ```bash
   pip install qrcode```
   
2. Exécutez le script generate_qr_tkinter.py.

3. Entrez le texte pour le code QR dans la zone de texte.

4. Cliquez sur le bouton "Générer le code QR" pour générer et afficher le code QR.

Vous pouvez également cliquer sur le bouton "Enregistrer le code QR" pour enregistrer le code QR généré dans un fichier PNG.

## Décodage de Code QR

Ce script Python utilise les bibliothèques zxing et Tkinter pour créer une interface graphique permettant de décoder un code QR à partir d'une image.

## Instructions d'utilisation
1. Installez les dépendances en utilisant la commande suivante :

```bash
pip install zxing
```
2. Exécutez le script decode_qr_tkinter.py.

3. Cliquez sur le bouton "Parcourir" pour sélectionner un fichier QRCode à décoder.

4. Cliquez sur le bouton "Décoder le QRCode" pour afficher le contenu du QRCode dans l'interface.

# Remarques
Assurez-vous d'avoir les droits nécessaires pour écrire dans le dossier où vous souhaitez enregistrer le code QR généré.
Pour le décodage, assurez-vous d'avoir Java installé sur votre système, car la bibliothèque zxing est basée sur Java.
