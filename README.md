<div align="center">

# 🎥 Video to ASCII Converter

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Transformez vos vidéos en art ASCII en temps réel avec une interface graphique intuitive*

[Installation](#-installation) •
[Fonctionnalités](#-fonctionnalités) •
[Utilisation](#-utilisation) •
[Dépannage](#-dépannage)

---

</div>

## 🚀 Installation

### Prérequis

<details>
<summary>Cliquez pour voir les prérequis</summary>

```bash
# Installation des dépendances Python
pip install opencv-python numpy tkinter

# Selon votre système d'exploitation
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS avec Homebrew
brew install python-tk
```
</details>

### Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/video-to-ascii.git

# Se déplacer dans le dossier
cd video-to-ascii

# Lancer le programme
python main.py
```

## ✨ Fonctionnalités

### 🎮 Interface interactive
- 🎯 Lecture/Pause fluide avec buffer de frames
- 📏 Contrôle de la largeur ASCII (50-300 caractères)
- 🖼️ Formats d'affichage adaptatifs
- 🎨 6 styles ASCII différents

### 🎬 Support vidéo
- 📺 Formats supportés : MP4, AVI, MKV
- 🔄 Conversion en temps réel optimisée
- ⚡ Cache des caractères pour meilleures performances
- 🎦 Préchargement des frames

### 🎨 Styles ASCII
- 🔤 Standard : "@%#*+=-:. "
- 📝 Détaillé : Set complet de caractères
- 📑 Lettres : A-Z, a-z uniquement
- 💠 Symboles : Blocs Unicode
- 💻 Binaire : Style 1/0
- 🎯 Simple : Version basique

### 🛠️ Personnalisation
- 📐 Formats multiples :
  - `Auto` : ratio original
  - `16:9` : format cinéma
  - `4:3` : format classique
- 🔍 Interface redimensionnable
- 📊 Barre de progression interactive
- 🎪 Fond noir et texte blanc pour meilleur contraste

## 📖 Utilisation

1. **Démarrage**
   ```bash
   python video_to_ascii.py
   ```

2. **Configuration**
   - Cliquez sur `Choisir une vidéo`
   - Sélectionnez le style ASCII désiré
   - Choisissez le format d'affichage
   - Ajustez la largeur avec le slider

3. **Contrôles**
   ```
   ▶️ : Lecture
   ⏸️ : Pause
   🔄 : Navigation temporelle
   🎨 : Sélection du style
   📐 : Ajustement de la taille
   ```

## 🎯 Styles ASCII disponibles

```
Standard : @%#*+=-:. 
Détaillé : $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. 
Lettres  : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
Symboles : █▓▒░+=*:-. 
Binaire  : 10 
Simple   : @#%*+=-:. 
```

## 🔧 Dépannage

<details>
<summary>💥 Problèmes courants</summary>

### 🚫 Le programme ne démarre pas
```bash
# Vérifier Python
python --version

# Vérifier les dépendances
pip list | grep -E "opencv-python|numpy"
```

### 🐌 Performances lentes
- Réduire la largeur ASCII
- Choisir un style plus simple
- Vérifier la résolution source
- Désactiver les styles complexes
</details>

## ⚠️ Limitations

- 🎥 Vidéos haute résolution : performances réduites
- 📼 Certains codecs non supportés
- 🖥️ Affichage dépendant de la police système
- 🎪 Styles complexes peuvent ralentir l'affichage

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📜 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

<div align="center">

---
Créé avec ❤️ par [Votre Nom]

</div>
