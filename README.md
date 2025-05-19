# Analyse des Performances de Joueurs de Football

Ce projet analyse les statistiques des joueurs de football sur une saison complète.  
L’objectif est d’identifier les meilleurs performeurs (buteurs, passeurs, temps de jeu) à l’aide de Python, Pandas et des visualisations.

## Informations sur les données

> **Remarque :** Ce jeu de données fictif s'inspire de la saison européenne 2022/23 et contient des statistiques simulées à des fins illustratives uniquement.


## Structure du projet

```

football-performance-analysis/
│
├── data/
│   └── players.csv         # Jeu de données
│
├── main.py                 # Script principal d’analyse
├── README.md               # Description du projet
└── venv/                   # Environnement virtuel

```

## Fonctionnalités

- Chargement et nettoyage des données
- Calcul des moyennes (buts, passes, minutes)
- Classements : meilleurs buteurs / passeurs
- Visualisations avec matplotlib et seaborn

## Carnet Jupyter

Pour une version plus lisible et interactive de l’analyse, consultez le [football_analysis.ipynb](football_analysis.ipynb).


## Technologies utilisées

- Python 3
- pandas
- matplotlib
- seaborn

## Exemples de visualisations

### Top Goal Scorers
![Top Goal Scorers](images/goals.png)

### Top Assist Providers
![Top Assists](images/assist.png)

### Top Players
![Top Players](images/players.png)

## Analyse des tendances

- Les attaquants comme **Erling Haaland**, **Kylian Mbappé** et **Lionel Messi** dominent l’équipe en termes de buts et de contributions totales, montrant leurs rôles offensifs essentiels.  
- Kevin De Bruyne se distingue comme le meilleur passeur parmi les milieux de terrain, soulignant sa capacité clé de création de jeu.  
- Globalement, les données révèlent une forte corrélation entre le temps de jeu et les contributions totales, soulignant l’importance d’un temps de jeu régulier.



## Exécution

1. Cloner le repo  
2. Installer les dépendances :  
```

pip install -r requirements.txt

```
3. Lancer le script :  
```

python main.py

```

## Auteur

- [Kimia GOLBAZKHANIAN](https://github.com/KimiaGol)
- Projet personnel

---

# Football Performance Analysis

This project analyzes football player statistics over a full season.  
It aims to identify top performers (goals, assists, minutes) using Python Pandas, and data visualizations.

## Dataset Information
  
> **Note:** This mock dataset is inspired by the 2022/23 European football season and contains fictionalized statistics for illustrative purposes only.


## Project Structure

```

football-performance-analysis/
│
├── data/
│   └── players.csv         # Dataset with player stats
│
├── main.py                 # Main Python script
├── README.md               # Project documentation
└── venv/                   # Virtual environment

```

## Features

- Load and clean player data
- Compute averages: goals, assists, minutes played
- Rank top scorers and assist providers
- Create visualizations with matplotlib and seaborn

## Jupyter Notebook

For a more interactive and readable version of the analysis, see the [football_analysis.ipynb](football_analysis.ipynb) notebook.


## Tools and Libraries

- Python 3
- pandas
- matplotlib
- seaborn

## Sample Visualizations

### Top Goal Scorers
![Top Goal Scorers](images/goals.png)

### Top Assist Providers
![Top Assists](images/assist.png)

### Top Players
![Top Players](images/players.png)

## Insights

- Forwards like **Erling Haaland**, **Kylian Mbappé**, and **Lionel Messi** lead the team in both goals and total contributions, showing their vital offensive roles.  
- Kevin De Bruyne stands out as the top assist provider among midfielders, highlighting his key playmaking ability.  
- Overall, the data reveals a strong correlation between minutes played and total contributions, emphasizing the importance of consistent playtime.  


## How to Run

1. Clone the repo  
2. Install dependencies:  
```

pip install -r requirements.txt

```
3. Run the script:  
```

python main.py

```

## Author

- [Kimia Golbazkhanian](https://github.com/KimiaGol)
- Project
```

---