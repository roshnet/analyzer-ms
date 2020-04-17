import pandas as pd


def get_columns_from_excel():
    '''
    Returns a list of columns in the temporary excel.
    Returns an error if one occurred.
    '''
    try:
        df = pd.read_excel('src/static/records.xlsx')
        return list(df.columns), None
    except Exception as err:
        return '', err


def prepare_pivot_payload(column):
    '''
    Generates a JSON <dict> payload to be used by the REST client.

    :param column:      (str)  Name of column to pivot about
    :return:            (dict) The JSON payload for client
                        (str)  Error message, if one occurred.
    '''
    payload = {}
    try:
        df = pd.read_excel('src/static/records.xlsx')
        payload['x_axis'] = {
            'column': column,
            'values': list(df[column]),
        }
        payload['y_axis'] = []
        for sub_col in df.drop(columns=column).columns:
            payload['y_axis'].append({
                'column': sub_col,
                'values': list(df[sub_col]),
            })
        return payload, None
    except Exception as err:
        return '', err
