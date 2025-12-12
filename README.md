# 🏆 AFCON 2025 Dashboard – Streamlit App

Ce projet est une application **Streamlit** interactive qui présente un tableau de bord complet pour la **Coupe d’Afrique des Nations 2025 (AFCON)** organisée au Maroc.

---

## 🚀 Fonctionnalités

- **Affichage des groupes (A–F)** avec drapeaux et design personnalisé  
- **Liste des joueurs les plus valorisés** avec graphiques interactifs (Plotly)  
- **Calendrier des matchs** filtrable par groupe  
- **Analytics avancées** :
  - Valeur maximale par pays  
  - Force des groupes (Top 3 joueurs par groupe)  
  - Timeline Gantt des matchs  
- **Interface moderne** avec thèmes CSS personnalisés

---

## 📁 Fichiers requis

Le dashboard utilise trois fichiers CSV (ou charge des données par défaut en cas d’absence) :

- `groups.csv`
- `players.csv`
- `matches.csv`

---

## ▶️ Lancer l'application

```bash
streamlit run dashboard.py
