from sys import exit

try:
    from colors import bcolors
    from util import cross_clear
except ImportError:
    exit("(CRITICAL) shipped bpysh dependencies not found")

# Bear-Shell rewrite because I don't know what else to work on...
# May 6 2024
class BPySh:
    def __init__(self, user = "user") -> None:
        super().__init__()
        self.user = user
        
        self.ver = "a1.0.0"
        
        # Run after init of everything
        # Makes it so I don't have to call bpysh.main() in __name__ if statement at bottom of the file
        self.main()
    
    def set_user(self, name: str) -> None:
        self.user = name
    
    def set_ver(self, ver: str) -> None:
        self.ver = ver
    
    def main(self) -> None:
        cross_clear() # clear screen without needing ugly system() command and allows for use on both CMD and PS
        print(f"""
        bpysh {self.ver}
        """)

        print(f"{bcolors.OKBLUE}Welcome, {self.user}")
        print(f"""{bcolors.OKBLUE}
        [1] To Configure and Open BioS
        [2] Show Recent Updates
        [3] To restart the system
        [4] To Close Shell Safely
        [5] Check for Updates
        """)
        select = input(f"[?]:{bcolors.OKGREEN} ")
        print(bcolors.OKBLUE)
        
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
            case _:
                print("nothing")
        
        print(f"{bcolors.DEFAULT}")
    
if __name__ == "__main__":
    bpysh = BPySh()