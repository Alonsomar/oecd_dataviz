import json
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
from utils import read_and_parse_dat_automation

# Set the default theme to dark mode and specify the color palette
pio.templates.default = "plotly_dark"
pio.templates["plotly_dark"].layout.font.family = "Montserrat"

# Define a custom color palette with a smoother transition
custom_palette = px.colors.sequential.Inferno

# Load the data
data_path = os.path.join('..', 'data', 'export-2024-08-09T08_59_30.984Z.csv')
df = read_and_parse_dat_automation(data_path)

# Assuming the data is loaded from a JSON file or passed as a dictionary
data_ranks = os.path.join('..', 'data', 'jobs_ranks.json')
with open(data_ranks, 'r') as file:
    data_ranks_json = json.load(file)


# Generate an interactive Plotly graph
def plot_automation_impact(df):
    fig = px.scatter(df, x='Country', y='Risk of Automation',
                     hover_name='Country', title='Risk of Automation by Country',
                     color='Risk of Automation',
                     size='Risk of Automation',
                     color_continuous_scale=custom_palette)

    # Customize the layout for a more professional look
    fig.update_layout(
        title="Fastest Growing vs. Fastest Declining Jobs (2023-2027)",
        title_font=dict(family="Montserrat, sans-serif", size=24, color="white"),
        font=dict(family="Montserrat, sans-serif", size=14, color="white"),
        xaxis_title="Rank (Positive for Growing, Negative for Declining)",
        yaxis_title="Job Title",
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent grid background
        xaxis=dict(title='Country', showgrid=False,
                   title_font=dict(family="Montserrat, sans-serif", size=16),
                   tickfont=dict(family="Montserrat, sans-serif", size=12)
                   ),
        yaxis=dict(title='Risk of Automation (%)', showgrid=False,
                   title_font=dict(family="Montserrat, sans-serif", size=16),
                   tickfont=dict(family="Montserrat, sans-serif", size=12)
                   ),
        margin=dict(l=40, r=40, t=80, b=40),
        coloraxis_colorbar=dict(
            title="Risk of Automation",
            titlefont=dict(size=14, color="white"),
            tickfont=dict(size=12, color="white"),
            lenmode="fraction",
            len=0.7,
            thickness=15,
            outlinewidth=0,
            bgcolor='#1f1f1f'
        )
    )

    # Save the graph as an HTML file
    output_path = os.path.join('..', 'graphs', 'automation_impact.html')
    fig.write_html(output_path, include_plotlyjs='cdn', full_html=False)  # Save without the full HTML wrapper
    print(f'Graph saved to {output_path}')


def plot_automation_impact_bar(df):
    # Define a custom color palette with two interpolated colors
    custom_palette = px.colors.sequential.Blues

    fig = go.Figure(
        data=[
            go.Bar(
                x=df['Country'],
                y=df['Risk of Automation'],
                marker=dict(color=df['Risk of Automation'], coloraxis="coloraxis"),
                name="Risk of Automation"
            )
        ],
        layout=dict(
            barcornerradius=5,  # Adjust the corner radius of the bars
            coloraxis=dict(colorscale=custom_palette, showscale=False)  # Hide color legend and use custom palette
        )
    )

    # Customize the layout for a more professional look
    fig.update_layout(
        title="Risk of Automation by Country",
        title_font=dict(family="Montserrat, sans-serif", size=24, color="white"),
        font=dict(family="Montserrat, sans-serif", size=14, color="white"),
        xaxis_title="Country",
        yaxis_title="Risk of Automation (%)",
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent grid background
        xaxis=dict(title='Country', showgrid=False,
                   title_font=dict(family="Montserrat, sans-serif", size=16),
                   tickfont=dict(family="Montserrat, sans-serif", size=12)
                   ),
        yaxis=dict(title='Risk of Automation (%)', showgrid=False,
                   title_font=dict(family="Montserrat, sans-serif", size=16),
                   tickfont=dict(family="Montserrat, sans-serif", size=12)
                   ),
        margin=dict(l=40, r=40, t=80, b=40),
    )

    # Save the graph as an HTML file
    output_path = os.path.join('..', 'graphs', 'automation_impact_bar.html')
    fig.write_html(output_path, include_plotlyjs='cdn', full_html=False)  # Save without the full HTML wrapper
    print(f'Bar chart saved to {output_path}')


def create_jobs_chart(data, output_dir='../graphs', output_filename='jobs_ranks.html'):
    """
    Creates a chart showing the fastest growing and declining jobs based on the provided data.

    Parameters:
    data (dict): The data containing the job ranks.
    output_dir (str): The directory where the output file will be saved.
    output_filename (str): The name of the output HTML file.

    Returns:
    None
    """
    # Convert the data into DataFrames
    df_growing = pd.DataFrame(data["Fastest Growing Jobs"])
    df_declining = pd.DataFrame(data["Fastest Declining Jobs"])

    # Adjust the rank for visual representation and ensure the correct order
    df_growing['Value'] = df_growing['Rank']
    df_declining['Value'] = -df_declining['Rank']

    # Reverse the order for display
    df_growing = df_growing.sort_values(by='Rank', ascending=False)
    df_declining = df_declining.sort_values(by='Rank', ascending=True)

    # Create the bar charts
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_growing['Value'],
        y=df_growing['Job Title'],
        orientation='h',
        marker_color='#2ecc71',  # Use a green color for growing jobs
        name="Fastest Growing Jobs"
    ))

    fig.add_trace(go.Bar(
        x=df_declining['Value'],
        y=df_declining['Job Title'],
        orientation='h',
        marker_color='#e74c3c',  # Use a red color for declining jobs
        name="Fastest Declining Jobs"
    ))

    # Update layout for better visualization
    fig.update_layout(
        title="Fastest Growing vs. Fastest Declining Jobs (2023-2027)",
        title_font=dict(family="Montserrat, sans-serif", size=24, color="white"),
        font=dict(family="Montserrat, sans-serif", size=14, color="white"),
        xaxis_title="Rank (Positive for Growing, Negative for Declining)",
        yaxis_title="Job Title",
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent grid background
        barmode='overlay',
        height=800,
        showlegend=False,
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            title_font=dict(family="Montserrat, sans-serif", size=16),
            tickfont=dict(family="Montserrat, sans-serif", size=12)
        ),
        yaxis=dict(
            autorange="reversed",
            title_font=dict(family="Montserrat, sans-serif", size=16),
            tickfont=dict(family="Montserrat, sans-serif", size=12)
        )

    )

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the output path
    output_path = os.path.join(output_dir, output_filename)

    # Save the plot as an HTML file
    fig.write_html(output_path, include_plotlyjs='cdn', full_html=False)  # Save without the full HTML wrapper
    print(f'Graph saved to {output_path}')



if __name__ == "__main__":
    plot_automation_impact(df)
    plot_automation_impact_bar(df)
    create_jobs_chart(data_ranks_json)
