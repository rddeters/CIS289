"""
Program: serversaces\views.py
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
import numpy as np
from io import BytesIO
import base64


def create_plot():
    # Establish a connection to the database
    conn = sqlite3.connect("2020_mens_vnl.db")

    # Write a SQL query to fetch data from database
    df = pd.read_sql_query("SELECT * FROM Servers", conn)

    # Close the connection
    conn.close()

    # Handle missing values by filling with zeros
    df["aces"].fillna("0", inplace=True)

    # Convert "spikes" column to integers
    df["aces"] = df["aces"].astype(int)

    # Group the data by team and sum up the 'spikes' for each team
    grouped = df.groupby('team')['aces'].sum()

    # Show actual values
    def absolute_val(val):
        a = np.round(val / 100. * grouped.sum(), 0)
        return int(a)

    # Plot a pie chart
    plt.figure(figsize=(10, 6))
    patches, texts, autotexts = plt.pie(grouped, labels=grouped.index, autopct=absolute_val, textprops={'fontsize': 10})

    # To rotate the labels to 45 degrees and bold them
    for text in texts:
        text.set_rotation(45)
    for autotext in autotexts:
        autotext.set_weight('bold')

    plt.title('Total Number of Aces Per Team')

    # Convert the plot figure to a PNG image string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return image_base64


def serversaces_view(request):
    plot = create_plot()
    return render(request, 'serversaces/index.html', {'plot': plot})
