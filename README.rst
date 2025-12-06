# SWU Scanner

Ce projet combine PaddleOCR et PySide6 (Qt) pour créer une application graphique capable de scanner et reconnaître automatiquement les cartes du jeu Star Wars Unlimited. L’application détecte et lit le numéro de carte présent en bas à droite grâce à des modèles OCR optimisés. L’objectif est de fournir un outil rapide, précis et ergonomique pour le catalogage, le référencement ou la collection de cartes SWU.

---

## 📥 Pré-requis

### Git
- Windows  
   https://git-scm.com/install/windows

- Linux
```bash
sudo apt install git -y
```

### Python
- Windows  
   https://www.python.org/downloads/release/python-3140/

- Linux
```bash
sudo apt install python3 python3-pip -y
```
---



## ▶️ Utilisation

# 📘 Guide d’utilisation – SWU Scanner

L’interface se compose de trois zones principales :

- **Menu du haut**
- **Panneau de gauche**
- **Visualisation du flux caméra au centre**

![image-de-l-application](images/global.png)

---

## 1) Menu du haut

### a) **Start**
Permet de **lancer le flux vidéo** depuis la source sélectionnée.

![image-start](images/start.png)

---

### b) **Stop**
Permet d’**arrêter entièrement le flux vidéo**.

![image-stop](images/stop.png)

---

### c) **Source**
Permet de choisir la source du flux vidéo.

![image-source](images/source.png)

Options disponibles :

- **Camera**  
  Toute caméra branchée à l’ordinateur sera automatiquement détectée.  
  *Conseil : privilégier une caméra 1080p minimum, avec focus réglable.*

- **RTSP / MJPEG**  
  Recommandé si vous utilisez une **caméra virtuelle depuis un smartphone**.  
  Meilleure qualité d’image.  
  *Conseil : l’application mobile « CamON Live » fonctionne très bien.*

- **Fichier vidéo**  
  Import d’un fichier local via l’explorateur.

---

### d) **Export**

![image-source](images/export.png)

Permet de choisir la base de données vers laquelle exporter les résultats.  
Actuellement disponible : **SWUDB** uniquement.

---

### e) **Offline Database**
*(Coming soon)*  
Cette fonctionnalité permettra de gérer une base locale sans connexion internet.

---

## 2) Panneau de droite

### a) Zone zoomée (OCR)

![image-source](images/ocr.png)

Affiche la **partie agrandie de la carte détectée**, transmise au moteur OCR.  
Permet de vérifier que :

- la carte est bien détectée,
- l’OCR lit correctement les informations.

---

### b) Auto‑detect / sélection manuelle

![image-source](images/autodetect.png)

Possibilité d’activer :

- **Détection automatique**
- **Sélection manuelle** de la zone ou de la carte si la détection automatique ne convient pas.

---

### c) Artwork et variantes

![image-source](images/variantes.png)

Affichage de l’**artwork de la carte reconnue**, avec navigation entre les variantes si nécessaire.

Exemple :  
Pour les extensions **Set 1, 2 et 3**, les **cartes fold** peuvent avoir le même ID que les cartes standard.  
L’utilisateur doit donc :

- naviguer entre les différentes possibilités,
- choisir la bonne,
- puis **verrouiller** la sélection.

---

### d) Auto‑add ou ajout manuel

![image-source](images/add.png)

Deux modes :

- **Auto‑add** : ajoute automatiquement chaque carte détectée à la liste.
- **Ajout manuel** : l’utilisateur décide quand ajouter la carte.

La liste des cartes ajoutées est ensuite **exportée** via le menu *Export*, pour être importée dans SWUDB.
