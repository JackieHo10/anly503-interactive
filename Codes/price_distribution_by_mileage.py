import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
py.sign_in('zz186', 'g7hnRhD8XruvpT3eKj1C')
pd.options.display.max_rows = 20
def data_ge(ylist,df_g1):
    datalist=[]
    for i in ylist:
        datalist=datalist+[df_g1[df_g1["mileage"]==i].price]
    return datalist
df_g3=df[["mileage","price"]]
ylist=[2017,2012,2007,2002]

ylist=[ "(902.001, 20800.8]", "(20800.8, 40600.6]", "(40600.6, 60400.4]","(60400.4, 80200.2]", "(80200.2, 100000.0]"]
#ylist=["(60400.4, 80200.2]", "(902.001, 20800.8]"]
hist_data = data_ge(ylist,df_g3)
group_labels = [("mileage range"+w) for w in ylist]

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
fig.layout["title"]="Price distribution by mileage"
fig.layout["xaxis"]=dict(
        title='Price(dollar)',
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

py.iplot(fig, auto_open=True)
