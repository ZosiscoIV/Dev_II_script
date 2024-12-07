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
        FileNotFoundError : Si aucun fichier CSV n'est trouvé dans le dossier spécifié.
        ValueError : Si les en-têtes des fichiers ne correspondent pas.
        IOError : Si une erreur d'écriture ou de lecture survient.
    """
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError(f"Aucun fichier CSV trouvé dans le dossier : {input_folder}")

    print(f"Fichiers trouvés : {csv_files}")

    header_written = False
    global_header = None

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as out_file:
            writer = None

            for file in csv_files:
                file_path = os.path.join(input_folder, file)
                with open(file_path, mode='r', newline='', encoding='utf-8') as in_file:
                    reader = csv.reader(in_file)
                    header = next(reader)

                    # Valider l'en-tête des fichiers
                    if not header_written:
                        global_header = header
                        writer = csv.writer(out_file)
                        writer.writerow(header)  # Écrire l'en-tête une seule fois
                        header_written = True
                    elif header != global_header:
                        raise ValueError(f"En-tête non correspondant dans le fichier : {file}")

                    for row in reader:
                        writer.writerow(row)
                    print(f"Ajout des données depuis : {file_path}")
        print(f"Fichier fusionné créé : {output_file}")

    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(f"Erreur : {fnf_error}")
    except IOError as io_error:
        raise IOError(f"Erreur d'accès au fichier : {io_error}")


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

    try:
        merge_csv_files(args.input_folder, args.output_file)
    except (FileNotFoundError, ValueError, IOError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
