# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests

r = requests.get("https://coreyms.com")

print(r.status_code)
print(r.ok)
