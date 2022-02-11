
import streamlit as st

import sys

from pandas.api.types import is_numeric_dtype


def import_utils():
    sys.path.append('../src')
    from src. format_color_util_plotly.colors import (
        plotly_qualitative_colors,
        plotly_continuous_colors)

    from src.format_color_util_streamlit.color_scale import (
        select_color_scale_based_on_dtype)

    from src.plot_util_plotly.scatterplot import (
        basic_scatterplot_color_cat,
        basic_scatterplot_color_seq)

    from src.data_util_streamlit.selection import (
        unguided_setup_axes_hover_and_size_data,
        filter_row_values_of_selected_column
    )

    from src.data_util.data import (
        convert_to_bool
    )

    from src.plot_util_plotly.scatterplot import (adv_scatterplot_with_trend,
                                                  adv_scatterplot_without_trend
                                                  )

    return (plotly_qualitative_colors,
            plotly_continuous_colors,
            basic_scatterplot_color_cat,
            basic_scatterplot_color_seq,
            unguided_setup_axes_hover_and_size_data,
            select_color_scale_based_on_dtype,
            filter_row_values_of_selected_column,
            adv_scatterplot_with_trend,
            adv_scatterplot_without_trend,
            convert_to_bool
            )


(plotly_qualitative_colors,
 plotly_continuous_colors,
 basic_scatterplot_color_cat,
 basic_scatterplot_color_seq,
 unguided_setup_axes_hover_and_size_data,
 select_color_scale_based_on_dtype,
 filter_row_values_of_selected_column,
 adv_scatterplot_with_trend,
 adv_scatterplot_without_trend,
 convert_to_bool
 ) = import_utils()


def adv_scatterplot_settings(
        logx_settingsk, logy_settingsk):

    logx_settings = st.sidebar.radio(
        "log_x:",
        ('false', 'true'), key=logx_settingsk)

    logy_settings = st.sidebar.radio(
        "log_y:",
        ('false', 'true'), key=logy_settingsk)

    logx_settings = convert_to_bool(logx_settings)
    logy_settings = convert_to_bool(logy_settings)

    return (logx_settings, logy_settings)


def scatterplot_trend_settings(trendline_settingsk, trendline_scope_settingsk):

    trendline_settings = st.sidebar.radio(
        label="trendline:",
        options=(None, 'ols', 'lowess', 'rolling', 'expanding' or 'ewm'), key=trendline_settingsk)

    trendline_scope_settings = st.sidebar.radio(
        label="trendline scope:",
        options=(None, 'trace', 'overall'), key=trendline_scope_settingsk)
    return trendline_settings, trendline_scope_settings


def st_adv_scatterplot(df,
                       data_x,
                       data_y,
                       data_on_hover,
                       data_sized,
                       data_colored,
                       plot_color_scale,
                       logx_settingsk,
                       logy_settingsk,
                       trendline_settingsk,
                       trendline_scope_settingsk):

    (
        logx_settings,
        logy_settings) = adv_scatterplot_settings(
        logx_settingsk,
        logy_settingsk)

    if is_numeric_dtype(df[data_x]) and is_numeric_dtype(df[data_y]):
        (trendline_settings,
         trendline_scope_settings) = scatterplot_trend_settings(
            trendline_settingsk,
            trendline_scope_settingsk)

        filtered_df = filter_row_values_of_selected_column(df)

        return adv_scatterplot_with_trend(filtered_df,
                                          data_x,
                                          data_y,
                                          data_on_hover,
                                          data_sized,
                                          data_colored,
                                          plot_color_scale,
                                          logx_settings,
                                          logy_settings,
                                          trendline_settings,
                                          trendline_scope_settings)
    else:
        filtered_df = filter_row_values_of_selected_column(df)

        return adv_scatterplot_without_trend(filtered_df,
                                             data_x,
                                             data_y,
                                             data_on_hover,
                                             data_sized,
                                             data_colored,
                                             plot_color_scale,
                                             logx_settings,
                                             logy_settings)
