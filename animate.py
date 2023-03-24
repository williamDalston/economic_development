import pandas as pd
import plotly.express as px

# Load the Gapminder dataset
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(url)

# Create the bubble chart
fig = px.scatter(df,
                 x='gdpPercap',
                 y='lifeExp',
                 size='pop',
                 color='continent',
                 hover_name='country',
                 log_x=True,
                 range_y=[20, 90],
                 range_x=[100, 100000],
                 animation_frame='year',
                 title='Life Expectancy vs. GDP per Capita (1952-2007)',
                 labels={'gdpPercap': 'GDP per Capita (log scale)',
                         'lifeExp': 'Life Expectancy (years)',
                         'pop': 'Population',
                         'year': 'Year'})

# Update the layout
fig.update_layout(autosize=False, width=800, height=600)

# Show the plot
fig.show()

# fig.write_html("gapminder_animation.html")
# <iframe src="gapminder_animation.html" width="800" height="600" frameborder="0" scrolling="no"></iframe>


