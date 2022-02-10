
import streamlit as st

import sys

from pandas.api.types import is_float_dtype


def import_utils():
    sys.path.append('../src')
    from src. format_color_util_plotly.colors import (
        plotly_qualitative_colors, plotly_continuous_colors)

    return (plotly_qualitative_colors, plotly_continuous_colors)


(plotly_qualitative_colors, plotly_continuous_colors) = import_utils()


def guided_select_color_scale_cat(plotly_qualitative_colors, discrete_axis, data_x, data_y):
    if discrete_axis == "x":
        data_colored = data_x

    elif discrete_axis == "y":
        data_colored = data_y

    color_options = plotly_qualitative_colors

    plot_color_scale = st.sidebar.selectbox(
        label="plot color scale:", options=color_options)

    return data_colored, plot_color_scale


def unguided_select_color_scale_cat(df, plotly_qualitative_colors):

    data_colored = st.sidebar.selectbox(
        label="data color key:", options=df.columns)

    plot_color_scale = st.sidebar.selectbox(
        label="plot color scale:", options=plotly_qualitative_colors)

    return data_colored, plot_color_scale


def select_color_scale_based_on_dtype(df):
    color_col, plot_color_scale_col = st.columns(2)
    with color_col:
        data_colored = st.selectbox(
            label="data colored:", options=df.columns)

    with plot_color_scale_col:
        if is_float_dtype(df[data_colored]):
            color_options = plotly_continuous_colors
        else:
            color_options = plotly_qualitative_colors

        plot_color_scale = st.sidebar.selectbox(
            label="plot color scale:", options=color_options)

    return data_colored, plot_color_scale
