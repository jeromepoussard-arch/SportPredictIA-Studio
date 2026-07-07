# SportPredictIA Studio — DS10 Product

## Objectif
Générer automatiquement des affiches sportives premium au format 1024x1536.

## Produit MVP
Affiche Coupe du Monde 2026 basée sur le modèle DS10.

## Éléments verrouillés
- Header
- Anneaux drapeaux
- Plaques équipes
- Trophée
- Cadre circuits
- Barre info
- Footer SportPredictIA

## Éléments variables
- Équipe 1
- Équipe 2
- Phase
- Match number
- Date
- Heure France
- Heure locale
- Stade
- Ville
- Région
- Pays
- Terre / localisation
- Skyline / stade

## Architecture
Le moteur Python ne dessine pas l’affiche finale.
Il compose des assets graphiques premium et injecte les données du match.

## Règle d’or
Un composant validé ne doit plus être modifié sans créer une nouvelle version.