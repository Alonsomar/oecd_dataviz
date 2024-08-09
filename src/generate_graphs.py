import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
from utils import read_and_parse_dat_automation

# Set the default theme to dark mode and specify the color palette
pio.templates.default = "plotly_dark"

# Define a custom color palette
custom_palette = px.colors.qualitative.Dark24

# Load the data
data_path = os.path.join('..', 'data', 'export-2024-08-09T08_59_30.984Z.csv')
df = read_and_parse_dat_automation(data_path)


# Generate an interactive Plotly graph
def plot_automation_impact(df):
    fig = px.scatter(df, x='Country', y='Risk of Automation',
                     hover_name='Country', title='Risk of Automation by Country',
                     color='Risk of Automation',
                     size='Risk of Automation',  # Assuming you want the size to reflect the risk
                     color_continuous_scale=custom_palette)

    # Customize the layout for a more professional look
    fig.update_layout(
        font=dict(family="Arial, sans-serif", size=14, color="white"),
        title=dict(font=dict(size=24, color="white")),
        paper_bgcolor='#1f1f1f',  # Dark background
        plot_bgcolor='#1f1f1f',    # Dark grid background
        xaxis=dict(title='Country', showgrid=False),
        yaxis=dict(title='Risk of Automation (%)', showgrid=False),
        margin=dict(l=40, r=40, t=80, b=40),
    )

    # Save the graph as an HTML file
    output_path = os.path.join('..', 'graphs', 'automation_impact.html')
    fig.write_html(output_path, include_plotlyjs='cdn', full_html=False)  # Save without the full HTML wrapper
    print(f'Graph saved to {output_path}')


if __name__ == "__main__":
    plot_automation_impact(df)
