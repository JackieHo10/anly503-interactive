import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
pd.options.display.max_rows = 20

def data2_ge(ylist,df_g1):
    datalist=[]
    for i in ylist:
        datalist=datalist+[df_g1[df_g1["year"]==i].mileage]
    return datalist
df_g2=df[["mileage","year"]]

ylist=[2017,2012,2007,2002,1997]


hist_data = data2_ge(ylist,df_g2)
group_labels = ylist

fig = ff.create_distplot(hist_data, group_labels,bin_size=5000)


layout = {
  "title": "2016 Summer Olympic Medal Count", 
  "updatemenus": [
    {
      "x": -0.05, 
      "y": 1, 
      "buttons": [
        {
          "args": ["visible", [True, True, True, True]], 
          "label": "All", 
          "method": "restyle"
        }, 
        {
          "args": ["visible", [False, True, False, False]], 
          "label": "Gold", 
          "method": "restyle"
        } 
      ], 
      "yanchor": "top"
    }
  ]
}

layout ={'barmode': 'overlay',
'hovermode': 'closest',
'legend': {'traceorder': 'reversed'},
'xaxis': {'anchor': 'y2', 'domain': [0.0, 1.0], 'zeroline': False},
'yaxis': {'anchor': 'free', 'domain': [0.35, 1], 'position': 0.0},
'yaxis2': {'anchor': 'x', 'domain': [0, 0.25], 'dtick': 1, 'showticklabels': False},
 "updatemenus": [
    {
      "x": 0, 
      "y": 1, 
      "buttons": [
        {
          "args": ["visible", [True, False, True, False]], 
          "label": "All", 
          "method": "restyle"
        }, 
        {
          "args": ["visible", [False, True, False, True]], 
          "label": "Gold", 
          "method": "restyle"
        } 
      ], 
      "yanchor": "top"
    }
  ]
}

fig.layout["updatemenus"]=updatemenus_ge(ylist)
fig.layout["title"]="Mileage distribution by year"
fig.layout["xaxis"]=dict(
        title='Mileage(mile)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        ))
fig.layout["yaxis"]=dict(
    title='probability',
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color='#7f7f7f'
    ))
print(fig)

py.iplot(fig)
