import pandas as pd
import numpy as np
from modules.analyzer import analyze
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

program_url_id = '1454279'

df = pd.read_csv(f'storage/episodes-{program_url_id}.csv')
df = df[['title','time','likes','comments']]
df = df.dropna() # remove rows with NaN values

total = df.count()[0]

df.index = abs(df.index - total)

episode_index = np.linspace(1,60,60)
episodes_cds = ColumnDataSource(df)

fig = figure(
    title='Web Reactiva: Episodes plotted by Likes',
    plot_height=400, plot_width=700,
    x_axis_label='Episodes',
    x_minor_ticks=3,
    y_range=(0, 30),
    toolbar_location=None
)

fig.circle(
    x='index',
    y='likes',
    source=episodes_cds,
    color='green',
    size=10,
    alpha=0.5
)

tooltips = [
    ('Title', '@title'),
    ('Likes', '@likes'),
    ('Duration', '@time'),
    ('Comments', '@comments')
]

fig.add_tools(HoverTool(tooltips=tooltips))

output_file('viz.html', title='Web Reactiva: Episodes plotted by Likes')

show(fig)
