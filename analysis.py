import pandas as pd
import numpy as np
from modules.analyzer import analyze
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

program_url_id = '1454279'

dfe = pd.read_csv(f'storage/wr-listens.csv')
dfe = dfe[['title','escuchas','time','likes','comments']]
dfe = dfe.dropna() # remove rows with NaN values

total = dfe.count()[0]

#df.index = abs(df.index - total)

#episode_index = np.linspace(1,total,total)

df_sorted_by_escuchas = dfe[['title','escuchas','time','likes','comments']].sort_values(by='escuchas', ascending=False)
df_sorted_by_escuchas = df_sorted_by_escuchas.reset_index(drop=True)

df_executive_sorted_by_escuchas = df_sorted_by_escuchas[['title','escuchas']]
print(df_executive_sorted_by_escuchas.head(10))

df_sorted_by_escuchas = dfe[['title','escuchas','time','likes','comments']].sort_values(by='escuchas')
df_sorted_by_escuchas = df_sorted_by_escuchas.reset_index(drop=True)

episodes_cds = ColumnDataSource(df_sorted_by_escuchas)

fig = figure(
    title='Web Reactiva: Episodes plotted by Escuchas',
    plot_height=400, plot_width=700,
    x_axis_label='Episodes',
    x_minor_ticks=3,
    y_range=(0, 1000),
    toolbar_location=None
)

fig.circle(
    x='index',
    y='escuchas',
    source=episodes_cds,
    color='green',
    size=10,
    alpha=0.5
)

tooltips = [
    ('Title', '@title'),
    ('Escuchas', '@escuchas')
    ('Likes', '@likes'),
    ('Duration', '@time'),
    ('Comments', '@comments')
]

fig.add_tools(HoverTool(tooltips=tooltips))

output_file('viz.html', title='Web Reactiva: Episodes plotted by Likes')

show(fig)
