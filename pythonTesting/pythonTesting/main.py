# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys
from os import rename

import requests


name = input("Your name? ")
print("Hello ", name)
print(sys.version)
print(sys.executable)


def print_hi(name):
    test = "test"
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to runkori
#  the script.
if __name__ == "__main__":
    print_hi("PyCharm")
r = requests.get("https://coreyms.com")
print(r.status_code)
