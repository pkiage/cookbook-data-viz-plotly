import streamlit as st

import sys


def import_utils():
    sys.path.append('../src')

    from src.  format_color_util_streamlit.scatter import (
        select_color_scale_based_on_dtype)

    from src.data_util_streamlit.selection import (
        specify_axes_value_range_plotted, filter_row_values_of_selected_column, filter_row_values_of_discrete_column)

    return (filter_row_values_of_selected_column, select_color_scale_based_on_dtype, specify_axes_value_range_plotted, filter_row_values_of_discrete_column)


(filter_row_values_of_selected_column, select_color_scale_based_on_dtype,
 specify_axes_value_range_plotted, filter_row_values_of_discrete_column) = import_utils()


def adv_scatterplot_graphed_data_setup_with_trend(df,
                                                  discrete_columns):

    (
        logx_settings, logy_settings) = adv_scatterplot_settings_with_trend(
        logx_settingsk, logy_settingsk)

    convert_to_bool(logx_settings)
    convert_to_bool(logy_settings)

    (data_colored, plot_color_scale) = select_color_scale_based_on_dtype(
        df, discrete_columns)

    filtered_df = filter_row_values_of_selected_column(df)
    return (filtered_df,

            logx_settings, logy_settings, plot_color_scale, data_colored)


def adv_scatterplot_graphed_data_setup(df,
                                       trendline_settingsk,
                                       logx_settingsk, logy_settingsk, trendline_scope_settingsk, discrete_columns):

    (trendline_settings,
     logx_settings, logy_settings, trendline_scope_settings) = adv_scatterplot_settings(
        trendline_settingsk,
        logx_settingsk, logy_settingsk, trendline_scope_settingsk)

    convert_to_bool(logx_settings)
    convert_to_bool(logy_settings)

    (data_colored, plot_color_scale) = select_color_scale_based_on_dtype(
        df, discrete_columns)

    filtered_df = filter_row_values_of_selected_column(df)

    return (filtered_df,
            trendline_settings, logx_settings, logy_settings, trendline_scope_settings, plot_color_scale, data_colored)
