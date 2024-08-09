import pandas as pd
import plotly.express as px
import os
from utils import read_and_parse_dat_automation

# Load the data
data_path = os.path.join('..', 'data', 'export-2024-08-09T08_59_30.984Z.csv')
df = read_and_parse_dat_automation(data_path)


# Example of generating an interactive plotly graph
def plot_automation_impact(df):
    fig = px.scatter(df, x='Country', y='Risk of Automation',
                     hover_name='Country', title='Risk of automation')

    # Save the graph as an HTML file
    output_path = os.path.join('..', 'graphs', 'automation_impact.html')
    fig.write_html(output_path)
    print(f'Graph saved to {output_path}')


if __name__ == "__main__":
    plot_automation_impact(df)
