# 📚 Book Scraper

Script Python permettant de scraper automatiquement les informations des livres du site [Books to Scrape](http://books.toscrape.com), un site fictif conçu à des fins pédagogiques.

---

## 🚀 Fonctionnalités

- Scrape les **50 pages** du site.
- Récupère pour chaque livre :
  - Titre
  - Prix en livres sterling (£)
  - Disponibilité
  - Évaluation (1 à 5 étoiles)
- Enregistre les données dans un fichier **CSV** horodaté (`books_YYYY-MM-DD.csv`).
- Structure de projet propre avec bonnes pratiques : `venv`, `.gitignore`, `requirements.txt`.

---

## 🛠️ Technologies utilisées

- Python 3
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- csv, os, datetime (modules standard)

---

## 📦 Installation

### 1. Cloner le projet :
```bash
git clone https://github.com/SebastienMichel57/books-scraper.git
cd books-scraper
```

### 2, Créer un environnement virtuel (optionnel mais recommandé) :
```bash 
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
```

### 3, Installer les dépendances:
```bash
    pip install -r requirements.txt
```

▶️ Utilisation
```bash 
    python scraper.py
```

### Le fichier CSV sera généré dans le dossier data/ :
    data/books_2025-07-30.csv

📂 Structure du projet
```
    books-scraper/
├── data/
│   └── books_YYYY-MM-DD.csv
├── scraper.py
├── requirements.txt
├── .gitignore
└── README.md
```

🛡️ Conformité éthique et légale
✅ Ce projet utilise un site web fictif (books.toscrape.com) conçu pour la formation au scraping.
Aucun scraping réel de site commercial ou protégé n’est effectué.

✍️ Auteur
Développé par Sébastien Michel — Développeur Fullstack JS.

- [📫 LinkedIn](https://www.linkedin.com/in/smichel5789)
- [Portfolio](https://www.sebmichel-dev.fr)

📌 Licence
Projet libre pour usage pédagogique. Reproduction partielle autorisée avec mention de l’auteur.

