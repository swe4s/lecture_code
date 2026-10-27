"""Combine forest fire emissions and GDP data by country and year.

Reference solution for Assignment 5 (Test Driven Development).
"""


def get_data(file_name, query_column=None, query_value=None,
             return_header=False):
    """Return rows from a CSV file, optionally only those matching a query.

    Parameters
    ----------
    file_name : str
        Path to a comma-separated file with a header line.
    query_column : int, optional
        Index of the column to match against.
    query_value : str, optional
        Keep only rows whose query_column equals this string.
    return_header : bool
        If True, return (header, rows) instead of rows.

    Returns
    -------
    list of list of str, or (list of str, list of list of str)
    """
    header = None
    rows = []
    with open(file_name) as f:
        for line in f:
            A = line.rstrip('\n').split(',')
            if header is None:
                header = A
                continue
            if query_column is None or A[query_column] == query_value:
                rows.append(A)
    if return_header:
        return header, rows
    return rows


def get_column_index(header, column_name):
    """Return the position of column_name in header, or None if absent."""
    try:
        return header.index(column_name)
    except ValueError:
        return None


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    """Return [year, forest_fires, gdp] for each year with both values.

    Parameters
    ----------
    co2_file : str
        Agrofood CO2 emission CSV (one row per country per year).
    gdp_file : str
        IMF GDP CSV (one row per country, one column per year).
    country : str
        Country name as written in both files.

    Returns
    -------
    list of [int, float, float]
    """
    co2_header, co2_rows = get_data(co2_file, query_column=0,
                                    query_value=country, return_header=True)
    gdp_header, gdp_rows = get_data(gdp_file, query_column=0,
                                    query_value=country, return_header=True)
    if len(gdp_rows) == 0:
        return []
    gdp_row = gdp_rows[0]

    fire_i = get_column_index(co2_header, 'Forest fires')
    year_i = get_column_index(co2_header, 'Year')

    data = []
    for row in co2_rows:
        year = row[year_i]
        gdp_i = get_column_index(gdp_header, year)
        if gdp_i is None:
            continue
        fire = row[fire_i]
        gdp = gdp_row[gdp_i]
        if fire == '' or gdp == '':
            continue
        data.append([int(year), float(fire), float(gdp)])
    return data
