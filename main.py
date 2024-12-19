import argparse
import sys
import subprocess

def get_route(adresse,arg=None):
    if arg:
        try:
            with subprocess.Popen(['tracert', adresse], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
                for line in process.stdout:
                    print(line.strip())
        except FileNotFoundError:
            print("tracert not found")
    else:
        process = subprocess.Popen(['tracert', adresse], stdout=subprocess.PIPE, text=True)
        print(process.communicate()[0])

    if arg is not None and arg.isalpha():
        process = subprocess.Popen(['tracert', adresse], stdout=subprocess.PIPE, text=True)
        with open(arg,"w") as file:
            for line in process.stdout:
                file.write(line)



def main():
    parser = argparse.ArgumentParser(description="traceroute")
    parser.add_argument("adresse",  help="adresse")
    parser.add_argument(  "-p", "--progressive", nargs="?", const=True, help="utilisation -p ou --progressive")
    parser.add_argument("-o","--output-file", help="utilisation -o ou --output-file")

    args = parser.parse_args()
    print(args)



    if  sys.argv[2] in [ "-p","--progressive"]:
        get_route(args.adresse, args.progressive)
    elif sys.argv[2] in [ "-o","--output-file"]:
        get_route(args.adresse, args.output_file)
    else:
        get_route(args.adresse)




if __name__ == "__main__":
    main()
