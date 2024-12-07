import os
import csv
import argparse


def merge_csv_files(input_folder, output_file):
    """
    Fusionne tous les fichiers CSV d'un dossier dans un seul fichier CSV.

    PRE :
        input_folder (str): Chemin vers le dossier contenant les fichiers CSV.
        output_file (str): Chemin vers le fichier de sortie.
    POST :
        tout les fichiers CSV du dossier input_folder sont rassemblés en 1 seul fichier (qui est output_file).
    RAISES :
        FileNotFoundError : Si il n'y a pas de fichier CSV dans le dossier spécifié ou que le fichier de sortie n'est pas trouvé.


    """
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    if not csv_files:
        print("Aucun fichier CSV trouvé dans le dossier spécifié.")
        return

    print(f"Fichiers trouvés : {csv_files}")

    header_written = False

    with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
        writer = None

        for file in csv_files:
            file_path = os.path.join(input_folder, file)
            with open(file_path, mode='r', newline='', encoding='utf-8') as in_file:
                reader = csv.reader(in_file)
                header = next(reader)  # Lire l'en-tête

                if not header_written:
                    writer = csv.writer(out_file)
                    writer.writerow(header)  # Écrire l'en-tête une seule fois
                    header_written = True

                for row in reader:
                    writer.writerow(row)
                print(f"Ajout des données depuis : {file_path}")

    print(f"Fichier fusionné créé : {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Fusionne plusieurs fichiers CSV en un seul fichier.")
    parser.add_argument(
        "--input_folder",
        type=str,
        required=True,
        help="Chemin vers le dossier contenant les fichiers CSV à fusionner."
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="Chemin vers le fichier CSV de sortie."
    )

    args = parser.parse_args()
    merge_csv_files(args.input_folder, args.output_file)


if __name__ == "__main__":
    main()
