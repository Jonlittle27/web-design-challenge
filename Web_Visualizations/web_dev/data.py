import pandas as pd

#changing a csv file to a dataframe and then into html 

path = "assets/cities.csv"
data = pd.read_csv(path)

table_html = data.to_html()

print(table_html)