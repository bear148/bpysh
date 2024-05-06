from sys import exit

try:
    from colors import bcolors
    from util import cross_clear
except ImportError:
    exit("Critical bpysh dependencies not found")

# Bear-Shell rewrite because I don't know what else to work on...
# May 6 2024
def main():
    cross_clear() # clear screen without needing ugly system() command and allows for use on both CMD and PS
    print(f"""
    bpysh a1.0.0
    """)

    print(f"{bcolors.OKBLUE}Welcome, michael")
    print(f"""{bcolors.OKBLUE}
    [1] To Configure and Open BioS
    [2] Show Recent Updates
    [3] To restart the system
    [4] To Close Shell Safely
    [5] Check for Updates
    """)
    select = input(f"[?]:{bcolors.OKGREEN} ")
    print(f"{bcolors.OKBLUE}")
    
    # So much cleaner: new match statement!
    match select:
        case "1":
            print("bios")
        case "2":
            print("updates")
        case "3":
            print("restart")
        case "4":
            print("close")
        case "5":
            print("check")
    
if __name__ == "__main__":
    main()