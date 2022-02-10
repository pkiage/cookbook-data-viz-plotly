import streamlit as st


import sys


def import_utils():
    sys.path.append('../src')

    from src.data_util_streamlit.selection import (
        filter_row_values_of_discrete_column,
        guided_setup_axes_and_hover_data)

    from src.  format_color_util_streamlit.color_scale import (
        guided_select_color_scale_cat)

    from src.plot_util_plotly.boxplot import (
        basic_boxplot)

    return (basic_boxplot,
            filter_row_values_of_discrete_column,
            guided_setup_axes_and_hover_data,
            guided_select_color_scale_cat)


(basic_boxplot,
 filter_row_values_of_discrete_column,
 guided_setup_axes_and_hover_data,
 guided_select_color_scale_cat) = import_utils()


def st_basic_boxplot(df, discrete_columns, continous_columns, plotly_qualitative_colors):
    discrete_axis = st.sidebar.radio(
        "axes with discrete data:",
        ('x', 'y'), key='discrete_axesdiscrete_axisb')

    (data_x, data_y, data_on_hover) = guided_setup_axes_and_hover_data(
        df, discrete_columns, continous_columns, discrete_axis)

    (data_colored, plot_color_scale) = guided_select_color_scale_cat(
        plotly_qualitative_colors, discrete_axis, data_x, data_y)

    filtered_df = filter_row_values_of_discrete_column(
        discrete_axis, df, data_x, data_y)

    return basic_boxplot(dataframe=filtered_df,
                         data_x=data_x,
                         data_y=data_y,
                         data_colored=data_colored,
                         data_on_hover=data_on_hover,
                         plot_color_scale=plot_color_scale)
