import streamlit as st


import sys
from pandas.api.types import is_float_dtype


def import_utils():
    sys.path.append('../src')

    from src.data_util_streamlit.selection import (
        filter_row_values_of_selected_column,
        semiguided_setup_axes_hover_and_size_data)

    from src.  format_color_util_streamlit.color_scale import (
        select_color_scale_based_on_dtype)

    from src.plot_util_plotly.scatterplot import (
        basic_scatterplot_color_cat,
        basic_scatterplot_color_seq)

    return (
        filter_row_values_of_selected_column,
        semiguided_setup_axes_hover_and_size_data,
        select_color_scale_based_on_dtype, basic_scatterplot_color_cat,
        basic_scatterplot_color_seq)


(
    filter_row_values_of_selected_column,
    semiguided_setup_axes_hover_and_size_data,
    select_color_scale_based_on_dtype, basic_scatterplot_color_cat,
    basic_scatterplot_color_seq) = import_utils()


def st_basic_scatterplot(df, discrete_columns, continous_columns):
    discrete_axis = st.sidebar.radio(
        "axes with discrete data:",
        ('x', 'y', 'either/neither'), key='discrete_axesdiscrete_axisb')

    (data_x, data_y, data_on_hover, data_sized) = semiguided_setup_axes_hover_and_size_data(
        df, discrete_columns, continous_columns, discrete_axis)

    (data_colored, plot_color_scale) = select_color_scale_based_on_dtype(df)

    filtered_df = filter_row_values_of_selected_column(df)

    if is_float_dtype(df[data_colored]):
        return basic_scatterplot_color_seq(df=filtered_df, data_x=data_x,
                                           data_y=data_y, data_sized=data_sized,
                                           data_colored=data_colored,
                                           data_on_hover=data_on_hover,
                                           plot_color_scale=plot_color_scale)
    else:
        return basic_scatterplot_color_cat(df=filtered_df, data_x=data_x,
                                           data_y=data_y, data_sized=data_sized,
                                           data_colored=data_colored,
                                           data_on_hover=data_on_hover,
                                           plot_color_scale=plot_color_scale)
