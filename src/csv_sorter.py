import csv
import argparse
import os

def sort_csv(input_file, output_file, sort_by, descending=False):
    """
    Trie un fichier CSV sur une colonne spécifique.

    PRE :
        input_file (str): Chemin du fichier CSV source.
        output_file (str): Chemin du fichier CSV trié.
        sort_by (str): Nom de la colonne sur laquelle effectuer le tri ("nom", "quantite", "prix", "type").
        descending (bool): Indique si le tri doit être décroissant.
    POST :
        Le fichier trié est écrit dans output_file.
    RAISES :
        FileNotFoundError : Si le fichier source n'est pas trouvé.
        ValueError : Si la colonne spécifiée pour le tri n'existe pas.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Fichier source non trouvé : {input_file}")

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        reader = csv.DictReader(in_file)
        rows = list(reader)

        # Vérification si la colonne existe en ignorant la casse
        columns = [col.lower() for col in reader.fieldnames]
        if sort_by.lower() not in columns:
            raise ValueError(f"Colonne spécifiée introuvable : {sort_by}")

        # Tri des lignes
        rows.sort(key=lambda x: x[sort_by], reverse=descending)

        with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"Fichier trié créé : {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Trie un fichier CSV.")
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
        "--sort_by",
        type=str,
        choices=["nom", "quantite", "prix", "type"],
        required=True,
        help="Nom de la colonne pour le tri (nom, quantite, prix, type)."
    )
    parser.add_argument(
        "--descending",
        action="store_true",
        help="Tri décroissant si spécifié (par défaut, tri croissant)."
    )

    args = parser.parse_args()

    sort_csv(args.input_file, args.output_file, args.sort_by, args.descending)


if __name__ == "__main__":
    main()
