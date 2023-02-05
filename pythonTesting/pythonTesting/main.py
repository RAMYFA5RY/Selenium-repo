# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import pandas as pd

df = pd.read_excel(
    "C:\\Users\Ramy\\Documents\\VS Code Files\\Python Files\\2- Automating using Selenium\\pythonTesting\\pythonTesting\\mtcars.xlsx"
)

r = requests.get("https://coreyms.com")

print(r.status_code)
print(r.ok)
