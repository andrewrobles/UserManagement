import subprocess
import random
import string

from library import System

def run_menu():
    system = System()

    while True:
        options = [
            "create",
            "remove",
            "modify",
        ]
        print("MENU".center(70, "-"))
        for option in options:
            print(f">> {option}")

        choice = ''
        while choice not in options:
            choice = input("Choose a functionality: ").lower()
            if choice in options:
                break

        username = input("Enter username: ")
        if choice == options[0]:
            fullname = input("Enter full name: ")
            first_name, last_name = fullname.split()
            system.create_user(first_name, last_name, username)
        elif choice == options[1]:
            system.remove_user(username)
        elif choice == options[2]:
            fullname = input("Enter full name: ")
            first_name, last_name = fullname.split()
            system.change_name(first_name, last_name, username)

run_menu()