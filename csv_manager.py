import argparse
from src import csv_filtrer, csv_merger, csv_reporter, csv_sorter


def main():
    parser = argparse.ArgumentParser(description="Gérer les fichiers CSV : fusion, tri, filtrage, génération de rapports.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Commandes disponibles")

    # Sous-commande pour fusionner
    merge_parser = subparsers.add_parser("merge", help="Fusionner plusieurs fichiers CSV en un seul fichier")
    merge_parser.add_argument("--input_folder", type=str, required=True, help="Dossier contenant les fichiers CSV à fusionner.")
    merge_parser.add_argument("--output_file", type=str, required=True, help="Chemin vers le fichier CSV de sortie.")

    # Sous-commande pour trier
    sort_parser = subparsers.add_parser("sort", help="Trier un fichier CSV")
    sort_parser.add_argument("--input_file", type=str, required=True, help="Chemin vers le fichier CSV d'entrée.")
    sort_parser.add_argument("--output_file", type=str, required=True, help="Chemin vers le fichier CSV de sortie.")
    sort_parser.add_argument("--sort_by", type=str, choices=["nom", "quantite", "prix", "type"],
                             required=True, help="Colonne sur laquelle trier.")
    sort_parser.add_argument("--descending", action="store_true", help="Trier par ordre décroissant.")

    # Sous-commande pour filtrer
    filter_parser = subparsers.add_parser("filter", help="Filtrer un fichier CSV")
    filter_parser.add_argument("--input_file", type=str, required=True, help="Chemin vers le fichier CSV d'entrée.")
    filter_parser.add_argument("--output_file", type=str, required=True, help="Chemin vers le fichier CSV de sortie.")
    filter_parser.add_argument("--type", type=str, help="Filtrer par type de produit.")
    filter_parser.add_argument("--nom", type=str, help="Filtrer par nom de produit.")
    filter_parser.add_argument("--prix", type=float, help="Filtrer par prix de produit.")
    filter_parser.add_argument("--quantite", type=int, help="Filtrer par quantité de produit.")

    # Sous-commande pour le rapport
    report_parser = subparsers.add_parser("report", help="Générer un rapport à partir d'un fichier CSV")
    report_parser.add_argument("--input_file", type=str, required=True, help="Chemin vers le fichier CSV d'entrée.")
    report_parser.add_argument("--output_file", type=str, required=True, help="Chemin vers le fichier rapport.")

    args = parser.parse_args()

    # Dispatcher les commandes
    if args.command == "merge":
        csv_merger.merge_csv_files(args.input_folder, args.output_file)
    elif args.command == "sort":
        csv_sorter.sort_csv(args.input_file, args.output_file, args.sort_by, args.descending)
    elif args.command == "filter":
        filters = {
            "nom": args.nom,
            "quantite": args.quantite,
            "prix": args.prix,
            "type": args.type,
        }
        # Filtrer les éléments qui sont définis (non-None)
        filters = {key: value for key, value in filters.items() if value is not None}

        # Passer le dictionnaire des filtres à la fonction filter_csv
        csv_filtrer.filter_csv(args.input_file, args.output_file, filters)

    elif args.command == "report":
        csv_reporter.generate_report(args.input_file, args.output_file)
    else:
        parser.error("Commande inconnue.")

if __name__ == "__main__":
    main()
