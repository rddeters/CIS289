"""
Program: attackersfaults\views.py
Author: River Deters
Last date modified: 07/28/2023

"""
# Create your views here.

from django.shortcuts import render
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def create_plot():
    # Establish a connection to the database
    conn = sqlite3.connect("2020_mens_vnl.db")

    # Write a SQL query to fetch data from database
    df = pd.read_sql_query("SELECT * FROM Attackers", conn)

    # Close the connection
    conn.close()

    # Handle missing values by filling with zeros
    df["faults"].fillna("0", inplace=True)

    # Convert "faults" column to integers
    df["faults"] = df["faults"].astype(int)

    # Group the data by team and sum up the 'faults' for each team
    grouped = df.groupby('team')['faults'].sum()

    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate the bar graph
    ax.bar(grouped.index, grouped.values)

    # Add labels for x-axis, y-axis, and chart title
    ax.set_xlabel('Team')
    ax.set_ylabel('Total Number of Attack Faults')
    ax.set_title('Total Attack Faults by Team')

    # Rotate x-axis labels by 45 degrees
    ax.set_xticklabels(grouped.index, rotation=45)

    # Add a dotted line for y-axis points to improve readability.
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Convert plot to PNG image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8').replace('\n', '')
    buf.close()

    return image_base64


def attackersfaults_views(request):
    plot = create_plot()
    return render(request, 'attackersfaults/index.html', {'plot': plot})
