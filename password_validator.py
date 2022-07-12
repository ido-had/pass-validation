import sys
from colorama import Fore


def main():
    if len(sys.argv)==2:
        validate(sys.argv[1])
    else: #missing or too many arguments in command line
        output("Please enter one password for validation  ",False)

def validate(password):
    """
    validating password and assuring its standards
    :param password: the password to be validated
    """
    if len(password)>=10: #verifying length
        has_num=False
        has_upper=False
        has_lower=False
        for c in sys.argv[1]:
            if c.isnumeric():  #verifying it contains at least one digit
                has_num=True
            if c.islower():     # verifying it contains at least one lower case char
                has_lower=True
            if c.isupper():      #verifying it contains at least one upper case char
                has_upper=True
            if has_lower and has_num and has_upper:    #All ok, no need to check the rest
                 output("Password meets all requirements  ",True)
        if not has_num:
            output("password must contain a digit",False)
        if not has_upper:
            output("password must contain upper case letter",False)
        if not has_lower:
            output("password must contain lower case letter",False)

    else:
        output("password length must be at least 10 characters",False)


def output(text,status):
    """
    printing password status after validating
    :param text: message to the user regarding password acceptance
    :param status: False for non legit password.true for valid and accepted password
    False will lead to Red foreground color true for green
    """
    if status:
        print(Fore.GREEN +text)
        sys.exit(0)
    else:
        print(Fore.RED +text)
        sys.exit(1)


main()
