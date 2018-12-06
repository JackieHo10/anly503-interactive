import pandas as pd
import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool

tc_merged = pd.read_csv('mergedDF.csv')

output_file("SalesVolume_GDP.html", title = "SalesVolume vs GDP")

z = tc_merged['salesVolume']
x2 = tc_merged['GDP in billion current U.S. dollars']
y2 = z/10**2
regression = np.polyfit(x2, y2, 1)
r_x, r_y = zip(*((i, i*regression[0] + regression[1]) for i in list(x2)))

source2 = ColumnDataSource(data=dict(gdp=x2,
                                    salesDivby100=y2,
                                    states=tc_merged['State'],
                                    salesVolume = z,
                                    rx = r_x,
                                    ry = r_y
                                   ))

TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,save,"
p2 = figure(plot_width=600, plot_height=500, tools=TOOLS, 
            title="Used Car Sales Volume vs State GDP")

p2.line(x = 'rx', y = 'ry', color="#2858a8", source = source2)
p2.scatter(x = 'gdp', y = 'salesDivby100', marker="circle", 
           fill_color = '#70a6ff', line_color=None, size = 6, fill_alpha=0.6,
           source = source2)

p2.xaxis.axis_label = "GDP in Billion Current U.S. Dollars"
p2.yaxis.axis_label = "Used Car Sales Volume in Hundred"

p2.title.text_font = "arial"
p2.title.text_font_size = '14pt'
p2.title.align = 'center'

p2.add_tools(HoverTool(
    tooltips=[
        ( 'State',   '@states'            ),
        ( 'GDP',  '@gdp{0,0}' ),
        ( 'Sales Volume', '@salesVolume'      )
    ]
))

show(p2)
