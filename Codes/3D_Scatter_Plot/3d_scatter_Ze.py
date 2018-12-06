import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='zz186', api_key='g7hnRhD8XruvpT3eKj1C')


df=pd.read_csv("cleaned_carscom.csv")
df2=df[["year","mileage","price","bodyStyle"]]
df2=df2[df2["year"]>=1990]
df2["counts"]=1
df2=df2.groupby(['year','bodyStyle']).sum()
df2=df2[df2["counts"]>=5]
df2["ave_mile"]=df2["mileage"]/df2["counts"]
df2["ave_price"]=df2["price"]/df2["counts"]
df2=df2.reset_index()
df2.to_csv("3d_average.csv")
df2[:5]


aaa=pd.read_csv("3d_average.csv")
bbb=aaa[aaa['counts']>5].reset_index()
z=bbb["ave_price"]
y=bbb["ave_mile"]
x=bbb["bodyStyle"]
zz=bbb["year"]
trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=zz,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    )
)

data = [trace1]
layout = {
  "hovermode": "closest", 
  "legend": {
    "y": 0.5, 
    "yanchor": "top"
  }, 
  "margin": {
    "r": 10, 
    "t": 25, 
    "b": 40, 
    "l": 60
  }, 
  "scene": {
    "xaxis": {"title": "BodyStyple"}, 
    "yaxis": {"title": "Average Mileage(miles)"}, 
    "zaxis": {"title": "Average Price(US dollars)"}
  }, 
  "showlegend": False, 
  "title": " Cars' average price vs Average mileage & BodyStyle in a 3d surface plot"
}

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='3d-scatter-colorscale')