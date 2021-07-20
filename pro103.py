import pandas as pd 
import plotly.express as px

ex = pd.read_csv('CovidData.csv')
fig = px.scatter(ex, x = 'date',y = 'cases', color = 'country')
fig.show()