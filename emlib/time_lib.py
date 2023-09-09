import time 

from datetime import datetime



def format_time():
    ftime = datetime.now().strftime("%Y-%m-%d")
    print(ftime)



def main():
    format_time()



if __name__ == "__main__":
    main()
