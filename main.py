import argparse
import sys
import subprocess

def get_route(adresse, progressive=False, output_file=None):
    try:
        with subprocess.Popen(['tracert', adresse], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,encoding='cp850') as process:
            if progressive:
                # Afficher la sortie en temps réel
                for line in process.stdout:
                    print(line.strip())
            else:
                # Lire toute la sortie après l'exécution
                output, errors = process.communicate()
                print(output)

            # Enregistrer dans un fichier si spécifié
            if output_file:
                with open(output_file, "w") as file:
                    file.writelines(process.stdout)

    except FileNotFoundError:
        print("Erreur : La commande 'tracert' est introuvable. Assurez-vous qu'elle est disponible sur votre système.")
    except Exception as e:
        print(f"Erreur : Une erreur est survenue lors de l'exécution de la commande tracert : {e}")


def main():
    parser = argparse.ArgumentParser(description="traceroute")
    parser.add_argument("adresse",  help="adresse")
    parser.add_argument(  "-p", "--progressive", nargs="?", const=True, help="utilisation -p ou --progressive")
    parser.add_argument("-o","--output-file", help="utilisation -o ou --output-file")

    args = parser.parse_args()
    get_route(adresse=args.adresse, progressive=args.progressive, output_file=args.output_file)




if __name__ == "__main__":
    main()
