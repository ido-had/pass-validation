import sys
from colorama import Fore


def main():

    if len(sys.argv)==2:
        validate(sys.argv[1])
    else:
        output("Please enter one password for validation ",False)

def validate(password):
    if len(password)>=10:
        hasnum=False
        hasUpper=False
        haslower=False
        for c in sys.argv[1]:
            if c.isnumeric():
                hasnum=True
    else:
        output("password length must be at least 10 characters",False)


def output(text,status):
    if status:
        print(Fore.GREEN +text)
    else:
        print(Fore.RED +text)


main()
