#Write a Python program to read each row from a given csv file and print a list of strings.
import pandas as pd


csv_f = pd.read_csv("users.csv")
#print(csv_f)
print()
#print(csv_f.head())
id=csv_f[["name","batch"]]
print(id)
