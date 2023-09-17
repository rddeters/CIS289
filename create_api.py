"""
Program: create_api.py
Author: River Deters
Last date modified: 07/28/2023

The purpose of this program is to create the API and search criteria for my Python II final project.
"""

import flask
from flask import request, jsonify
import sqlite3
import create_database as cd

database = "2020_mens_vnl.db"
conn = cd.create_connection(database)
cur = conn.cursor()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>2020 Men's Volleyball Nations League</h1>
    <p>An API that returns a list of the 255 best players from the 2020 Men's Volleyball Nations League ranked based on
     6 attributes: serving, attacking, setting, blocking, digging, and receiving. Please feel free to search the 
     following tables: Blockers, Servers, Setters, Attackers, Receivers, and Diggers.</p>'''


@app.route('/api/v1/resources/2020vnl/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory  # function that returns dictionaries instead of lists to better output json
    cur = conn.cursor()

    all_attackers = cur.execute('SELECT * FROM Attackers;').fetchall()
    all_blockers = cur.execute('SELECT * FROM Blockers;').fetchall()
    all_diggers = cur.execute('SELECT * FROM Diggers;').fetchall()
    all_receivers = cur.execute('SELECT * FROM Receivers;').fetchall()
    all_servers = cur.execute('SELECT * FROM Servers;').fetchall()
    all_setters = cur.execute('SELECT * FROM Setters;').fetchall()

    return jsonify(all_attackers, all_blockers, all_diggers, all_receivers, all_servers, all_setters)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# API Search for Attackers Table
@app.route('/api/v1/resources/2020vnl/attackers', methods=['GET'])
def api_filter_attackers():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    spikes = query_parameters.get('spikes')
    faults = query_parameters.get('faults')
    shots = query_parameters.get('shots')
    total_attempts = query_parameters.get('total_attempts')
    success_percentage = query_parameters.get('success_percentage')

    query = "SELECT * FROM Attackers WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if spikes:
        query += ' spikes=? AND'
        to_filter.append(spikes)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if shots:
        query += ' shots=? AND'
        to_filter.append(shots)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if success_percentage:
        query += ' success_percentage=? AND'
        to_filter.append(success_percentage)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Attackers"
    description = "This API provides data about attackers in the 2020 Men's Volleyball Nations League. You can " \
                  "search for attackers using the following parameters: rank, shirt_number, name, team, spikes, " \
                  "faults, shorts, total_attempts, and success_percentage"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


# API Search for Blockers Table
@app.route('/api/v1/resources/2020vnl/blockers', methods=['GET'])
def api_filter_blockers():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    stuff_blocks = query_parameters.get('stuff_blocks')
    faults = query_parameters.get('faults')
    rebounds = query_parameters.get('rebounds')
    total_attempts = query_parameters.get('total_attempts')
    average_per_set = query_parameters.get('average_per_set')

    query = "SELECT * FROM Blockers WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if stuff_blocks:
        query += ' stuff_blocks=? AND'
        to_filter.append(stuff_blocks)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if rebounds:
        query += ' rebounds=? AND'
        to_filter.append(rebounds)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if average_per_set:
        query += ' average_per_set=? AND'
        to_filter.append(average_per_set)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Blockers"
    description = "This API provides data about blockers in the 2020 Men's Volleyball Nations League. You can " \
                  "search for blockers using the following parameters: rank, shirt_number, name, team, stuff_blocks," \
                  " faults, rebounds, total_attempts, and success_percentage!"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


# API Search for Diggers Table
@app.route('/api/v1/resources/2020vnl/diggers', methods=['GET'])
def api_filter_diggers():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    digs = query_parameters.get('digs')
    faults = query_parameters.get('faults')
    reception = query_parameters.get('reception')
    total_attempts = query_parameters.get('total_attempts')
    average_per_set = query_parameters.get('average_per_set')

    query = "SELECT * FROM Diggers WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if digs:
        query += ' digs=? AND'
        to_filter.append(digs)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if reception:
        query += ' reception=? AND'
        to_filter.append(reception)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if average_per_set:
        query += ' average_per_set=? AND'
        to_filter.append(average_per_set)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Diggers"
    description = "This API provides data about diggers in the 2020 Men's Volleyball Nations League. You can " \
                  "search for diggers using the following parameters: rank, shirt_number, name, team, digs, " \
                  "faults, reception, total_attempts, and success_percentage!"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


# API Search for Receivers Table
@app.route('/api/v1/resources/2020vnl/receivers', methods=['GET'])
def api_filter_receivers():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    excellents = query_parameters.get('excellents')
    faults = query_parameters.get('faults')
    serve_reception = query_parameters.get('serve_reception')
    total_attempts = query_parameters.get('total_attempts')
    efficiency_percentage = query_parameters.get('efficiency_percentage')

    query = "SELECT * FROM Receivers WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if excellents:
        query += ' excellents=? AND'
        to_filter.append(excellents)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if serve_reception:
        query += ' serve_reception=? AND'
        to_filter.append(serve_reception)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if efficiency_percentage:
        query += ' efficiency_percentage=? AND'
        to_filter.append(efficiency_percentage)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Receivers"
    description = "This API provides data about receivers in the 2020 Men's Volleyball Nations League. You can " \
                  "search for receivers using the following parameters: rank, shirt_number, name, team, excellents, " \
                  "faults, serve_reception, total_attempts, and efficiency_percentage!"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


# API Search for Servers Table
@app.route('/api/v1/resources/2020vnl/servers', methods=['GET'])
def api_filter_servers():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    aces = query_parameters.get('aces')
    faults = query_parameters.get('faults')
    hits = query_parameters.get('hits')
    total_attempts = query_parameters.get('total_attempts')
    average_per_set = query_parameters.get('average_per_set')

    query = "SELECT * FROM Servers WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if aces:
        query += ' aces=? AND'
        to_filter.append(aces)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if hits:
        query += ' hits=? AND'
        to_filter.append(hits)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if average_per_set:
        query += ' average_per_set=? AND'
        to_filter.append(average_per_set)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Servers"
    description = "This API provides data about servers in the 2020 Men's Volleyball Nations League. You can " \
                  "search for servers using the following parameters: rank, shirt_number, name, team, aces, " \
                  "faults, hits, total_attempts, and average_per_set!"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


# API Search for Setters Table
@app.route('/api/v1/resources/2020vnl/setters', methods=['GET'])
def api_filter_setters():
    query_parameters = request.args

    rank = query_parameters.get('rank')
    shirt_number = query_parameters.get('shirt_number')
    name = query_parameters.get('name')
    team = query_parameters.get('team')
    running_sets = query_parameters.get('running_sets')
    faults = query_parameters.get('faults')
    still_sets = query_parameters.get('still_sets')
    total_attempts = query_parameters.get('total_attempts')
    average_per_set = query_parameters.get('average_per_set')

    query = "SELECT * FROM Setters WHERE"
    to_filter = []

    if rank:
        query += ' rank=? AND'
        to_filter.append(rank)
    if shirt_number:
        query += ' shirt_number=? AND'
        to_filter.append(shirt_number)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if team:
        query += ' team=? AND'
        to_filter.append(team)
    if running_sets:
        query += ' running_sets=? AND'
        to_filter.append(running_sets)
    if faults:
        query += ' faults=? AND'
        to_filter.append(faults)
    if still_sets:
        query += ' still_sets=? AND'
        to_filter.append(still_sets)
    if total_attempts:
        query += ' total_attempts=? AND'
        to_filter.append(total_attempts)
    if average_per_set:
        query += ' average_per_set=? AND'
        to_filter.append(average_per_set)
    if not (id or rank or name or team):
        return page_not_found(404)

    query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

    conn = sqlite3.connect('../finalvolleyball/2020_mens_vnl.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    # Create an HTML string for the header and description
    header = "2020 Men's VNL Setters"
    description = "This API provides data about setters in the 2020 Men's Volleyball Nations League. You can " \
                  "search for setters using the following parameters: rank, shirt_number, name, team, running_sets, " \
                  "faults, still_sets, total_attempts, and average_per_set!"

    response_data = {
        'header': header,
        'description': description,
        'results': results
    }

    return jsonify(response_data)


app.run(debug=True, use_reloader=False)
