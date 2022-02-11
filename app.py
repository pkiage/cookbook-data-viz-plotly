
import streamlit as st

import plotly.express as px


# IMPORT
# datasets import
from src.data_util.data import (
    data_set_options)

# colors import
from src. format_color_util_plotly.colors import (
    plotly_qualitative_colors, plotly_continuous_colors)


from src. format_color_util_streamlit.color_scale import (
    select_color_scale_based_on_dtype)


# FORMATTING & TOGGLE
# general
from src. format_util_plotly.background import (
    plain_white_background)

from src.format_util_streamlit.title_legend_intercept import (
    update_title_legend_intercept)

from src.format_util_streamlit.axes import (update_axes_visibility)

from src.data_util_streamlit.selection import (
    animated_data_setup,
    semiguided_setup_axes_hover_and_size_data,
    filter_row_values_of_selected_column)


# CREATE FIG & TEXT
# box
from src.plot_util_streamlit.boxplot import (st_boxplot_intro)

from src.plot_util_streamlit.boxplot_basic import (st_basic_boxplot)

from src.plot_util_streamlit.boxplot_adv import (
    st_adv_data_and_settings_boxplot,
    adv_boxplot,
    adv_animated_boxplot)

# scatter
from src.plot_util_streamlit.scatterplot import (scatterplot_intro)


from src.plot_util_streamlit.scatterplot_basic import (st_basic_scatterplot)


from src.plot_util_streamlit.scatterplot_adv import (
    st_adv_scatterplot, adv_scatterplot_settings
)

from src.plot_util_plotly.scatterplot import (
    adv_animated_scatterplot_without_trend,
)


# APP
st.header("Plotly Data Viz Recipes - Scatter Plot & Box Plot")

plot_options = ["Box Plot", "Scatter Chart"]

selected_data = st.selectbox(label="select data set:",
                             options=data_set_options)

df = getattr(px.data, selected_data)()

with st.expander("show selected data:"):
    st.write(df)

"Plotly Built-in Datasets Descriptions: https://plotly.com/python-api-reference/generated/plotly.data.html"

selected_graph = st.selectbox(label="select graph:",
                              options=plot_options)


numeric = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

continous = ['float16', 'float32', 'float64']

discrete_non_numeric = ["object", "category"]

continous_columns = df.select_dtypes(include=numeric).columns
discrete_columns = df.select_dtypes(exclude=continous).columns
columns = df.columns

# BOXPLOT FIG
if selected_graph == plot_options[0]:
    st.subheader(plot_options[0])

    st_boxplot_intro()

    box_plot_extra_show_option = st.sidebar.radio(label="use additional plotly box settings:",
                                                  options=("no", "yes"), key="box_plot_extra")
    if box_plot_extra_show_option == "no":

        fig = st_basic_boxplot(
            df, discrete_columns, continous_columns, plotly_qualitative_colors)
    if box_plot_extra_show_option == "yes":

        (filtered_df,  data_x,  data_y,
            data_colored, data_on_hover, plot_color_scale, points_settings,
            notch_settings, orientation_settings, boxmode_settings,
            logx_settings, logy_settings) = st_adv_data_and_settings_boxplot(df, plotly_qualitative_colors)

        box_plot_animate_option = st.sidebar.radio(label="animate:",
                                                   options=("no", "yes"), key="box_plot_animate")
        if box_plot_animate_option == "no":

            fig = adv_boxplot(filtered_df,  data_x,  data_y,
                              data_colored, data_on_hover, plot_color_scale, points_settings,
                              notch_settings, orientation_settings, boxmode_settings,
                              logx_settings, logy_settings)

        if box_plot_animate_option == "yes":

            (animation_frame_settings, animation_group_settings, xmin, xmax,
             ymin, ymax) = animated_data_setup(filtered_df,  data_x,  data_y)

            fig = adv_animated_boxplot(filtered_df,  data_x,  data_y,
                                       data_colored, data_on_hover, plot_color_scale, points_settings,
                                       notch_settings, orientation_settings, boxmode_settings,
                                       logx_settings, logy_settings,
                                       animation_frame_settings, animation_group_settings,
                                       xmin, xmax, ymin, ymax)

# SCATTER PLOT FIG
if selected_graph == plot_options[1]:

    st.subheader(plot_options[1])

    scatterplot_intro()

    scatter_plot_adv_option = st.sidebar.radio(label="use additional plotly box settings:",
                                               options=("no", "yes"), key="scatter_plot_extra_show")

    scatter_plot_animate_option = st.sidebar.radio(label="animate:",
                                                   options=("no", "yes"), key="scatter_plot_animate")
    discrete_axis = st.sidebar.radio(
        "axes with discrete data:",
        ('x', 'y', 'either/neither'), key='discrete_axes')

    if scatter_plot_adv_option == "no":

        fig = st_basic_scatterplot(df,
                                   discrete_columns,
                                   continous_columns)

    if scatter_plot_adv_option == "yes":

        (data_x, data_y, data_on_hover, data_sized) = semiguided_setup_axes_hover_and_size_data(
            df, discrete_columns, continous_columns, discrete_axis)

        (data_colored, plot_color_scale) = select_color_scale_based_on_dtype(df)

        if scatter_plot_animate_option == "no":

            fig = st_adv_scatterplot(df,
                                     data_x,
                                     data_y,
                                     data_on_hover,
                                     data_sized,
                                     data_colored,
                                     plot_color_scale,
                                     "logx_settingsk",
                                     "logy_settingsk",
                                     "trendline_settingsk",
                                     "trendline_scope_settingsk")

        if scatter_plot_animate_option == "yes":

            filtered_df = filter_row_values_of_selected_column(df)

            (animation_frame_settings, animation_group_settings, xmin, xmax,
             ymin, ymax) = animated_data_setup(filtered_df,  data_x,  data_y)

            (
                logx_settings,
                logy_settings) = adv_scatterplot_settings(
                "logx_settingska",
                "logy_settingska")

            fig = adv_animated_scatterplot_without_trend(df,
                                                         data_x,
                                                         data_y,
                                                         data_on_hover,
                                                         data_sized,
                                                         data_colored,
                                                         plot_color_scale,
                                                         logx_settings,
                                                         logy_settings,
                                                         animation_frame_settings,
                                                         animation_group_settings)
        # DISPLAY FIG
        # general fig settings

update_title_legend_intercept(fig)
plain_white_background(fig)
update_axes_visibility(fig)

# display fig
st.plotly_chart(fig)
