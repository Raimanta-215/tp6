import subprocess
import sys

def get_route(nomHote, output_file=None):
    try:
        process = subprocess.Popen(['tracert', nomHote], stdout=subprocess.PIPE, text=True)
        if output_file:
            with open(output_file, 'w') as file:
                for line in process.stdout:
                    file.write(line)
                    print(line, end='')
        else:
            for line in process.stdout:
                print(line, end='')

        process.communicate()

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL or IP address> [-p] [-o <output-file>]")
        sys.exit(1)

    target = sys.argv[1]
    progressive = '-p' in sys.argv
    output_file = None

    if '-o' in sys.argv:
        output_file_index = sys.argv.index('-o') + 1
        if output_file_index < len(sys.argv):
            output_file = sys.argv[output_file_index]
        else:
            print("Erreur : Le paramètre '-o' doit être suivi du nom du fichier.")
            sys.exit(1)

    get_route(target, output_file)
