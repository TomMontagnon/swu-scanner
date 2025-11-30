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

## 📦 Installation

### 0. Ouvrir un git bash (spécifique windows)


### 1. Cloner le dépôt

```bash
git clone https://github.com/TomMontagnon/swu-scanner.git
cd swu-scanner
```

---

### 2. Environnement virtuel (spécifique linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*(Sous Windows, cette étape n'est pas nécessaire selon ta procédure.)*

---

### 3. Installation des dépendances

```bash
pip install .
```

---

### 4. Lancement de l’application

- Linux

```bash
launch-swu-scanner
```

- Windows

```bash
launch-swu-scanner.exe
```

## ▶️ Utilisation

