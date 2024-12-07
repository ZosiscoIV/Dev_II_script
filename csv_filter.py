import csv
import argparse
import os

def filter_csv(input_file, output_file, filters):
    """
    Filtre un fichier CSV selon des colonnes et des valeurs spécifiques.

    PRE :
        input_file (str): Chemin du fichier CSV source.
        output_file (str): Chemin du fichier CSV filtré.
        filters (dict): Dictionnaire de filtres où clé=colonne et valeur=valeur à filtrer.
    POST :
        Le fichier filtré est écrit dans output_file.
    RAISES :
        FileNotFoundError : Si le fichier source n'est pas trouvé.
        ValueError : Si une colonne spécifiée pour le filtre n'existe pas.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Fichier source non trouvé : {input_file}")

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file)
        rows = list(reader)

        for column, value in filters.items():
            if column not in reader.fieldnames:
                raise ValueError(f"Colonne spécifiée introuvable : {column}")
            rows = [row for row in rows if row[column] == value]

        with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"Fichier filtré créé : {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Filtre un fichier CSV.")
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
        help="Chemin du fichier CSV de sortie."
    )
    parser.add_argument(
        "--nom",
        type=str,
        help="Filtrer sur la colonne 'nom' avec une valeur spécifique."
    )
    parser.add_argument(
        "--quantite",
        type=str,
        help="Filtrer sur la colonne 'quantite' avec une valeur spécifique."
    )
    parser.add_argument(
        "--prix",
        type=str,
        help="Filtrer sur la colonne 'prix' avec une valeur spécifique."
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Filtrer sur la colonne 'type' avec une valeur spécifique."
    )

    args = parser.parse_args()

    filters = {
        "nom": args.nom,
        "quantite": args.quantite,
        "prix": args.prix,
        "type": args.type,
    }
    filters = {key: value for key, value in filters.items() if value is not None}

    if not filters:
        print("Erreur : Vous devez spécifier au moins un filtre.")
        return

    filter_csv(args.input_file, args.output_file, filters)


if __name__ == "__main__":
    main()
