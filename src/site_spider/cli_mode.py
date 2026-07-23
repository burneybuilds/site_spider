def banner_info():
    banner = fr""" __       _     _           
/ _\_ __ (_) __| | ___ _ __ 
\ \| '_ \| |/ _` |/ _ \ '__|
_\ \ |_) | | (_| |  __/ |   
\__/ .__/|_|\__,_|\___|_|   
   |_|                      
            @Autho : Albert.
   """
    print(banner)

def take_input():
    options = ["1. [+] Img to Loc ",
                "2. [+] Crawler",
                "3. [+] WebScrapper"]
    for op in options:
        print(op)
    
    try:
        user_input = input("Enter your Choice: ")
        user_input = int(user_input)
        
        if user_input not in (1, 2, 3):
            return "Options are 1, 2, 3."
        return user_input
    
    except ValueError:
        return "Invalid input 1 / 2 / 3."

def main():
    banner_info()
    output = take_input()
    print(output)

if __name__ == "__main__":
    main()