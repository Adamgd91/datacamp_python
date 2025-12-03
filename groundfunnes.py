import pandas as pd

population = pd.read_csv("datasets/US Births Python.csv", index_col= 0)

print(population)
print(population[["Year"]])
print(population[["Births", "Boy", "Girl"]])