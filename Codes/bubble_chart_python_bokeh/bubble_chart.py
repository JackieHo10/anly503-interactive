import pandas as pd
import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

tc_merged = pd.read_csv('mergedDF.csv')

output_file("SalesVolume_Population_n_NonAutoTrans.html", title="SalesVolume vs Populationn & NonAutoTrans")

x_pre = tc_merged["Population estimate July 1, 2016"]
x = x_pre/10**7
tc_merged['non_auto_trans_means'] = 100 - tc_merged['Car, truck or van drove alone %'] - tc_merged['Car, truck or van carpooled %']
y = tc_merged['non_auto_trans_means']
z = tc_merged['salesVolume']
radii = (z - np.mean(z))/np.std(z)/20

source = ColumnDataSource(data=dict(pop=x,
                                    commute=y,
                                    states=tc_merged['State'],
                                    radius = radii,
                                    salesVolume = z
                                   ))
TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,save,"

p1 = figure(plot_width=600, plot_height=500, tools = TOOLS,
            title = "Used Car Sales Volume vs Population and Non Auto Commute Percentage")

p1.scatter(x = 'pop', y = 'commute', radius='radius',
           fill_color = '#70a6ff',
          fill_alpha=0.6,
          line_color=None, source = source)
p1.xaxis.axis_label = "Population Estimate in 10 Million by July-1-2016"
p1.yaxis.axis_label = "Non Auto Commute Percentage"

p1.title.text_font = "arial"
p1.title.text_font_size = '9pt'
p1.title.align = 'center'

p1.add_tools(HoverTool(
    tooltips=[
        ( 'State',   '@states'            ),
        ( 'Population',  '@pop*10m' ),
        ( 'Non Auto Commute Percentage', '@commute%'      ),
        ( 'Sales Volume', '@salesVolume'      )
    ]
))

show(p1)  # open a browser
