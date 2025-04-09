# Consignes Projet API - Utilisation de l’API Deezer 🎵

## Projet par groupe (3 ou 4)

---

## 📚 Lexique

- **API** (*Application Programming Interface*) : Interface de programmation permettant d'accéder à des données ou services via des points d’accès appelés *endpoints*.
- **Endpoints** : URLs fournies par l’API permettant de faire des requêtes précises (par exemple : récupérer des albums, artistes ou playlists).

---

## 🎯 Objectif

Créer une application complète en Python avec le framework **Django**, en utilisant les données fournies par **l'API publique de Deezer**.  
L’application devra également stocker certaines informations utilisateur dans une **base de données interne**.

Vous devez mener un projet **from scratch** en équipe, avec une **répartition claire des tâches**, un **travail collaboratif**, et une **communication constante**.  
Le projet combinera une source de données externe (**l’API Deezer**) avec une base de données locale pour offrir une interface **utile, cohérente et agréable** à l’utilisateur.

---

## 🧠 Exemple adapté (non exhaustif)

L’application permet de :

- Rechercher des **artistes**, **albums** ou **morceaux** via l’API Deezer.
- Voir des **informations détaillées** (top titres d’un artiste, albums, durée des morceaux, etc.).
- Pour les **utilisateurs connectés** :
  - Ajouter des morceaux ou albums à une **liste de favoris**.
  - Créer des **playlists personnelles**.
  - Voir leur **profil musical**, leurs favoris et playlists.
  - Éventuellement noter ou commenter des morceaux (fonctionnalité avancée).

---

## 👣 Déroulé

### Étapes recommandées

1. Comprendre les **endpoints** disponibles via l’API Deezer.
2. Imaginer et lister les **fonctionnalités** de l’application.
3. Concevoir la **base de données interne** (profil utilisateur, playlists, favoris, etc.).
4. Établir un **planning clair** et une **répartition des tâches**.
5. Développer l’application Django :
   - Appels API (via `requests` ou autre)
   - Backend (gestion utilisateur, base de données, logique métier)
   - Frontend (templates, affichage, design)

---

## 📁 Livrables attendus

**En plus du code**, les documents suivants sont attendus :

- **Planning**
- **Cahier des charges**
  - Fonctionnalités prévues
  - Rôles utilisateurs : non connecté / connecté / admin
  - Diagramme de **base de données**
  - Outils utilisés pour le développement **ET** l’organisation du projet
- **Charte graphique**
  - Choix esthétiques, couleurs, logo, etc.
  - Expérience utilisateur (**UX**)
- **README.md** complet
  - Installation et lancement de l’application
  - Fonctionnalités disponibles
  - Explication des appels **API Deezer** utilisés

📌 **Tous les livrables** doivent être centralisés dans un dépôt **GitHub** d’équipe, auquel le formateur devra avoir accès.

---

## 📅 Planning

Projet sur **6 séances (35h)** :

- **02/09** journée
- **17/09** journée ▶️ Planning, Cahier des charges, Charte graphique
- **25/11** journée
- **10/12** journée
- **16/12** demi-journée
- **18/12** demi-journée ▶️ Code finalisé + README

---

## 💡 Conseils & pièges à éviter

- Écrire un code **propre et lisible** :
  - Noms de variables explicites
  - Indentation correcte
  - Suppression du code inutile
- Tous les membres doivent pouvoir **expliquer** toutes les parties du projet.
- Utiliser les outils de **debug** :
  - Frontend : Devtools navigateur
  - Backend : `print()` ou `pdb`
- Lire la **documentation Django** (authentification notamment).
- Mettre en place **Git** dès le début avec des **commits réguliers**.
- Travail **en binôme** recommandé pour les tâches complexes (**pair programming**).
- Commencer par les éléments les plus complexes : **API**, puis **backend**, puis **front**.
- Utiliser des **données mockées** si besoin.
- Suivre une logique de développement : **Données → Fonctionnalités → Style**.

---

## 🔗 Liens utiles

- **Documentation API Deezer** : https://developers.deezer.com/api
- **Appel API en Python** :  
  https://pythonds.linogaliana.fr/content/manipulation/04c_API_TP.html  
- **Débuter avec Django** :  
  https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django  
- **Authentification avec Django** :  
  https://docs.djangoproject.com/fr/4.2/topics/auth/default/
