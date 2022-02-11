import streamlit as st


import sys


def import_utils():
    sys.path.append('../src')

    from src.plot_util_plotly.boxplot import (
        adv_boxplot,
        adv_animated_boxplot)

    from src.data_util.data import (
        convert_to_bool
    )

    from src.data_util_streamlit.selection import (
        animated_data_setup, filter_row_values_of_selected_column, unguided_setup_axes_and_hover_data
    )

    from src.  format_color_util_streamlit.color_scale import (
        unguided_select_color_scale_cat
    )

    return (convert_to_bool,
            adv_boxplot,
            animated_data_setup,
            adv_animated_boxplot,
            unguided_select_color_scale_cat,
            unguided_setup_axes_and_hover_data,
            filter_row_values_of_selected_column,
            unguided_setup_axes_and_hover_data)


(
    convert_to_bool,
    adv_boxplot,
    animated_data_setup,
    adv_animated_boxplot,
    unguided_select_color_scale_cat,
    unguided_setup_axes_and_hover_data,
    filter_row_values_of_selected_column,
    unguided_setup_axes_and_hover_data
) = import_utils()


def adv_boxplot_settings():

    points_options = ['all', 'suspectedoutliers', 'outliers']

    points_settings = st.sidebar.selectbox(
        label="points:", options=points_options)

    notch_settings = st.sidebar.radio(
        "notched:",
        ('false', 'true'), key='notch_settings')

    orientation_settings = st.sidebar.radio(
        "orientation:",
        ('v', 'h'), key='orientation')

    boxmode_settings = st.sidebar.radio(
        "boxmode:",
        ('overlay', 'group'), key='boxmode_settings')

    logx_settings = st.sidebar.radio(
        "log_x:",
        ('false', 'true'), key='logx_settings')

    logy_settings = st.sidebar.radio(
        "log_y:",
        ('false', 'true'), key='logy_settings')

    bool_settings = [
        convert_to_bool(i)
        for i in [notch_settings, logx_settings, logy_settings]
    ]

    return (points_settings,
            orientation_settings,
            boxmode_settings,
            bool_settings[0],
            bool_settings[1],
            bool_settings[2])


def st_adv_data_and_settings_boxplot(df, plotly_qualitative_colors):

    (data_x, data_y, data_on_hover) = unguided_setup_axes_and_hover_data(df)

    (points_settings, orientation_settings, boxmode_settings,
     notch_settings, logx_settings, logy_settings) = adv_boxplot_settings()

    (data_colored, plot_color_scale) = unguided_select_color_scale_cat(
        df, plotly_qualitative_colors)

    filtered_df = filter_row_values_of_selected_column(df)

    return (filtered_df,  data_x,  data_y,
            data_colored, data_on_hover, plot_color_scale, points_settings,
            notch_settings, orientation_settings, boxmode_settings,
            logx_settings, logy_settings)
