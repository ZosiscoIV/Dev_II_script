# Dev_II_script

Le projet **Dev_II_script** permet de gérer et d'analyser des données de stock à partir de fichiers CSV. Il offre des fonctionnalités telles que la fusion de fichiers CSV, le tri et le filtrage des données, ainsi que la génération de rapports d'analyse des stocks. Toutes les fonctionnalités sont accessibles via une interface en ligne de commande, permettant de manipuler facilement les données sans avoir à recoder des processus complexes.

## Fonctionnalités

1. **Fusion de fichiers CSV**
   - Fusionne plusieurs fichiers CSV situés dans un dossier donné en un seul fichier de sortie.
   - Gère les en-têtes pour ne les écrire qu'une seule fois.

2. **Tri des données d'un fichier CSV**
   - Permet de trier un fichier CSV sur des critères tels que le nom, la quantité, le prix ou le type.
   - Le tri peut être effectué dans l'ordre croissant ou décroissant.

3. **Filtrage des données CSV**
   - Permet de filtrer un fichier CSV selon des critères comme le nom, la quantité, le prix ou le type.
   - Seules les lignes correspondant aux critères spécifiés sont exportées.

4. **Rapport d'analyse des stocks**
   - Génère un rapport détaillant les stocks avec des totaux pour chaque article, ainsi que des informations additionnelles (quantité totale, prix total, valeur totale).

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python 3 et les dépendances nécessaires.

Le fichier CSV doivent comporter les colonnes "nom", "quantite", "prix" et "type"

### Dépendances

Le programme nécessite la bibliothèque `argparse`, qui est incluse dans la bibliothèque standard de Python, donc il n'y a pas besoin d'installer de dépendances externes à moins que vous n'ayez une version Python trop ancienne.

Si vous souhaitez installer manuellement les dépendances, utilisez la commande suivante :

pip install -r requirements.txt

## Installation

1. Clonez ce dépôt sur votre machine locale :

git clone https://github.com/votre-utilisateur/Dev_II_script.git

2. Accédez au répertoire du projet :

cd Dev_II_script

3. Si nécessaire, installez les dépendances :

pip install -r requirements.txt

## Utilisation

Le programme se lance via la ligne de commande et offre plusieurs sous-commandes pour effectuer différentes actions.

### Fusion de fichiers CSV

python csv_manager.py merge --input_folder <dossier_source> --output_file <fichier_sortie.csv>

### Tri des données

python csv_manager.py sort --input_file <fichier.csv> --output_file <fichier_sortie.csv> --sort_by <colonne> [--descending]

### Filtrage des données

python csv_manager.py filter --input_file <fichier.csv> --output_file <fichier_sortie.csv> [--type <valeur>] [--nom <valeur>] [--prix <valeur>] [--quantite <valeur>]

### Génération d'un rapport des stocks

python csv_manager.py report --input_file <fichier.csv> --output_file <rapport.csv>

## Contribution

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, ouvrez une issue ou soumettez une pull request.

#
