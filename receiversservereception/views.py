"""
Program: receiversservereception\views.py
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
    df = pd.read_sql_query("SELECT * FROM Receivers", conn)

    # Close the connection
    conn.close()

    # Replace empty strings with NaN
    df["serve_reception"].replace("", np.nan, inplace=True)

    # Replace NaN with 0
    df["serve_reception"].fillna(0, inplace=True)

    # Convert "serve_reception" column to integers
    df["serve_reception"] = df["serve_reception"].astype(int)

    # Group the data by team and sum up the 'serve_reception' for each team
    grouped = df.groupby('team')['serve_reception'].sum()

    # Define a function to show actual values
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

    plt.title('Total Serve Receptions Per Team')

    # Convert the plot figure to a PNG image string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return image_base64


def receiversservereception_view(request):
    plot = create_plot()
    return render(request, 'receiversservereception/index.html', {'plot': plot})
