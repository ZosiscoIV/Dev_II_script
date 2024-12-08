import csv
import argparse
import os


def generate_report(input_file, output_file):
    """
    Génère un rapport à partir d'un fichier CSV d'inventaire.

    PRE :
        input_file (str): Chemin du fichier CSV source.
        output_file (str): Chemin du fichier rapport de sortie.
    POST :
        Un fichier CSV de rapport est généré, incluant des statistiques sur les stocks.
    RAISES :
        FileNotFoundError : Si le fichier source n'est pas trouvé.
        ValueError : Si le fichier CSV ne contient pas les colonnes requises.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Fichier source non trouvé : {input_file}")

    total_value = 0
    total_items = 0
    categories = set()
    data = []

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file)
        required_columns = ["nom", "quantite", "prix", "type"]

        # Vérification des colonnes requises
        missing_columns = [col for col in required_columns if col not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"Colonnes manquantes dans le fichier CSV : {', '.join(missing_columns)}")

        for row in reader:
            try:
                nom = row["nom"]
                quantite = int(row["quantite"])
                prix = float(row["prix"])
                type_ = row["type"]
                total_article = quantite * prix

                total_value += total_article
                total_items += quantite
                categories.add(type_)
                data.append((nom, quantite, prix, type_, total_article))
            except ValueError:
                print(f"Erreur lors du traitement de la ligne : {row}")
                continue

    # Écriture du rapport
    with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Statistique", "Valeur"])
        writer.writerow(["Valeur totale des stocks (€)", f"{total_value:.2f}"])
        writer.writerow(["Nombre total d'articles", total_items])
        writer.writerow(["Nombre de catégories uniques", len(categories)])
        writer.writerow(["Catégories", ", ".join(categories)])
        writer.writerow([])  # Ligne vide
        writer.writerow(["Détails des stocks"])
        writer.writerow(["Nom", "Quantité", "Prix Unitaire (€)", "Type", "Total (€)"])
        writer.writerows(data)

    print(f"Rapport généré dans : {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Génère un rapport à partir d'un fichier CSV d'inventaire.")
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Chemin du fichier CSV source."
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="Chemin du fichier CSV du rapport de sortie."
    )

    args = parser.parse_args()

    generate_report(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
