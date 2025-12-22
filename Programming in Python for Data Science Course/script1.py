"""
Created on Thurs March 13 11:02:29 2025

@author: Marina Galvao

"""
import pandas as pd


def group_and_sum(dataframe, group_by_column, sum_column):
    """
    Given a dataframe, return a dataframe that has been grouped
    by a specified column, and summed the values of another specified column

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    group_by_column : str
        The column of choice where the grouping will occur
    sum_column : str
        The column that will be summed within the specified groups

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe with the column that has been grouped and the resulting sum of each group

    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    Raise Exception
        If the input argument group_by_column is not in the dataframe
    Raise Exception
        If the input argument sum_column is not in the dataframe

    Examples
    --------
    >>> group_and_sum(vinyl_sales, 'vinyl_artist', 'album_price')

    """

    # Checks if the data variable is of type pd.dataframe
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # If the group_by_column is not in the dataframe
    if group_by_column not in dataframe.columns:
        raise Exception(
            "The grouping column you are specifiying cannot be found in the dataframe given"
        )

    # If the sum_column is not in the dataframe
    if sum_column not in dataframe.columns:
        raise Exception(
            "The summing column you are specifiying cannot be found in the dataframe given"
        )

    # Group by the group_by_column and sum the sum_column
    grouped_totals = dataframe.groupby(group_by_column)[sum_column].sum().reset_index()

    # Set the group_by_column as the index; by doing this, we can access these values as row indices
    grouped_totals = grouped_totals.set_index(group_by_column)

    # Sort by the sum_column
    grouped_totals = grouped_totals.sort_values(by=sum_column, ascending=False)

    # Renaming columns; we don't need to mention the group_by_column here as it is the index
    grouped_totals.columns = [sum_column]

    # Return the grouped group_by_column and summed sum_column
    return grouped_totals
