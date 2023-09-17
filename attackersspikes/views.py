"""
Program: attackersspikes\views.py
Author: River Deters
Last date modified: 07/28/2023

"""

from django.shortcuts import render

# Create your views here.

# in your Django app's views.py
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
    df = pd.read_sql_query("SELECT * FROM Attackers", conn)

    # Close the connection
    conn.close()

    # Handle missing values by filling with zeros
    df["spikes"].fillna("0", inplace=True)

    # Convert "spikes" column to integers
    df["spikes"] = df["spikes"].astype(int)

    # Group the data by team and sum up the 'spikes' for each team
    grouped = df.groupby('team')['spikes'].sum()

    # Define a function to show actual values
    def absolute_val(val):
        a = np.round(val/100.*grouped.sum(), 0)
        return int(a)

    # Plot a pie chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(grouped, labels=grouped.index, autopct=absolute_val, textprops={'fontsize': 10})

    # To rotate the labels to 45 degrees and bold them
    for text in ax.texts:
        text.set_rotation(45)
        text.set_weight('bold')

    ax.set_title('Total Number of Spikes Per Team')

    # Convert plot to PNG image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8').replace('\n', '')
    buf.close()

    return image_base64


def attackersspikes_view(request):
    plot = create_plot()
    return render(request, 'attackersspikes/index.html', {'plot': plot})
