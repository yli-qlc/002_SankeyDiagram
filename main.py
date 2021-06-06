import pandas as pd
import holoviews as hv
hv.extension('bokeh')
from bokeh.plotting import show



df = pd.read_csv(r"C:\Users\YingLi\PycharmProjects\vaccines\vaccines_data_formated.csv")
value_list = ["EU","COVAX","USA","UK","Brazil","China","India","Canada","Japan","Latam (w/o Brazil)","African Union","Rest"]
boolean_series = df.Country.isin(value_list)
df = df[boolean_series]
df['Doses'] = df['Doses'].div(1000000000).round(3)
print (df.head)



sankey1 = hv.Sankey(df,kdims=["Manufacturer", "Country"], vdims=["Doses"])
show (hv.render(sankey1))

sankey2 = hv.Sankey(df,kdims=["Manufacturer", "Country"], vdims=["Doses"])
sankey2.opts(cmap="PuBuGn_r",label_position='outer',
                                 edge_color='Manufacturer', edge_line_width=0,
                                 node_alpha=1.0, node_width=40, node_sort=False,
                                 width=800, height=1200, bgcolor="snow",
                                 title="How many covid-19 vaccines has each manufacturer sold")

show (hv.render(sankey2))