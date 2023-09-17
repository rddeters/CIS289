"""
Program: receiverstotalattempts\views.py
Author: River Deters
Last date modified: 07/28/2023

"""

from django.shortcuts import render

# Create your views here.

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
from io import BytesIO
import base64


def create_plot():
    # Establish a connection to the database
    conn = sqlite3.connect("2020_mens_vnl.db")

    # Write a SQL query to fetch data from database
    df = pd.read_sql_query("SELECT * FROM Receivers", conn)

    # Close the connection
    conn.close()

    # Handle missing values by filling with zeros
    df["total_attempts"].fillna("0", inplace=True)

    # Convert "faults" column to integers
    df["total_attempts"] = df["total_attempts"].astype(int)

    # Group the data by team and sum up the 'faults' for each team
    grouped = df.groupby('team')['total_attempts'].sum()

    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate the bar graph
    ax.bar(grouped.index, grouped.values)

    # Add labels for x-axis, y-axis, and chart title
    ax.set_xlabel('Team')
    ax.set_ylabel('Total Number of Receive Attempts')
    ax.set_title('Total Receive Attempts by Team')

    # Rotate x-axis labels by 45 degrees
    ax.set_xticklabels(grouped.index, rotation=45)

    # Add a dotted line for y-axis points to improve readability.
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Convert the plot figure to a PNG image string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return image_base64


def receiverstotalattempts_view(request):
    plot = create_plot()
    return render(request, 'receiverstotalattempts/index.html', {'plot': plot})
