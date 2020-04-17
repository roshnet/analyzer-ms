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
        return "", err
