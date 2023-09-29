import subprocess
from map import Map

#Map.print_matrix(Map.populate(Map.populate(Map.create_matrix(Map))))

def choose_class():
    game_class = int(input("Choose your class by typing one of the numbers below:\n"
            "(1) Warrior\n"
            "(2) Barbarian\n"
            "(3) Mage\n"
            "(4) Bard\n"))

    if game_class == 1:
        #subprocess.run('clear', shell=True)
        answer = int(input("You are about to choose Warrior\n"
                       "ASCII ART HERE\n"
                       "(1) go back\t\t(2) confirm"))

        if answer == 1:
            return choose_class()
        elif answer == 2:
            return "Barbarian"
        else:
            print("not an option, try again.")

    elif game_class == 2:
        #subprocess.run('clear', shell=True)
        answer = int(input("You are about to choose Barbarian\n"
                       "ASCII ART HERE\n"
                       "(1) go back\t\t(2) confirm"))

        if answer == 1:
            return choose_class()
        elif answer == 2:
            return "Barbarian"
        else:
            print("not an option, try again.")

    elif game_class == 3:
        #subprocess.run('clear', shell=True)
        answer = int(input("You are about to choose Mage\n"
                       "ASCII ART HERE\n"
                       "(1) go back\t\t(2) confirm"))

        if answer == 1:
            return choose_class()
        elif answer == 2:
            return "Barbarian"
        else:
            print("not an option, try again.")

    elif game_class == 4:
        #subprocess.run('clear', shell=True)
        answer = int(input("You are about to choose Bard\n"
                       "ASCII ART HERE\n"
                       "(1) go back\t\t(2) confirm"))


        if answer == 1:
            return choose_class()
        elif answer == 2:
            return "Barbarian"
        else:
            print("not an option, try again.")

    else:
        print(f"'{game_class}' is not an option")
        #subprocess.run('clear', shell=True)
        return choose_class()


choose_class()