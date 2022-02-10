import streamlit as st


# FILTER DATA

def multi_select_row_values(df, discrete_column):
    row_values = df[discrete_column].unique()

    bulk_select_options = ["show all values", "hide all values"]
    bulk_selection = st.sidebar.selectbox(
        label="bulk selection of column row values to plot:", options=bulk_select_options)

    if bulk_selection == bulk_select_options[0]:
        multi_select_default = row_values

    elif bulk_selection == bulk_select_options[1]:
        multi_select_default = None

    return st.sidebar.multiselect(
        label="column row values plotted:",
        options=row_values,
        default=multi_select_default,
    )


def filter_row_values_of_discrete_column(discrete_axis, df, data_x, data_y):

    if discrete_axis == "x":
        discrete_column = data_x

    elif discrete_axis == "y":
        discrete_column = data_y

    rows_selected = multi_select_row_values(df, discrete_column)

    return df[df[discrete_column].isin(rows_selected)]


def filter_row_values_of_selected_column(df):
    filtercolumn = st.sidebar.selectbox(
        label="column used to filter values plotted:", options=df.columns)

    rows_selected = multi_select_row_values(df, filtercolumn)

    return df[df[filtercolumn].isin(rows_selected)]


def filter_axes_values(df, data_x, data_y, data_colored):

    axes_filtered = st.sidebar.radio(
        "axes_filtered:",
        ('x', 'y', 'color'), key='axes_filtered')
    if axes_filtered == "x":
        filered_column = data_x

    elif axes_filtered == "y":
        filered_column = data_y

    elif axes_filtered == "color":
        filered_column = data_colored

    rows_selected = multi_select_row_values(df, filered_column)

    return df[df[filered_column].isin(rows_selected)]

# SPECIFY AXES RANGE


def specify_xaxis_value_range_plotted(df, data_x):
    if df[data_x].dtype == "object":
        # xmin, xmax
        return st.select_slider(
            label="select x range", options=df[data_x].unique(),
            value=(min(df[data_x]),
                   max(df[data_x])), key="xrange")

    else:
        # xmin, xmax
        return st.slider(label='select x range',
                               min_value=min(df[data_x]), max_value=max(df[data_x]),
                               value=(min(df[data_x]),
                                      max(df[data_x])))


def specify_yaxis_value_range_plotted(df, data_y):
    if df[data_y].dtype == "object":
        #ymin, ymax
        return st.select_slider(
            label="select y range", options=df[data_y].unique(),
            value=(min(df[data_y]),
                   max(df[data_y])), key="yrange")
    else:
        #ymin, ymax
        return st.slider(
            label='select y range',
            min_value=min(df[data_y]), max_value=max(df[data_y]),
            value=(min(df[data_y]),
                   max(df[data_y])), key="yrange")


def specify_axes_value_range_plotted(df, data_x, data_y):
    xrange, yrange = st.columns(2)
    with xrange:
        (xmin, xmax) = specify_xaxis_value_range_plotted(df, data_x)

    with yrange:
        (ymin, ymax) = specify_yaxis_value_range_plotted(df, data_y)

    return (xmin, xmax, ymin, ymax)

# SETUP ANIMATED DATA


def animated_data_setup(filtered_df, data_x, data_y):
    st.write(
        "The gapminder dataset is a good one to animate with year as animation frame.")
    frame_col, group_col = st.columns(2)
    with frame_col:
        animation_frame_settings = st.selectbox(
            label="animation frame:", options=filtered_df.columns)

    with group_col:
        animation_group_settings = st.selectbox(
            label="animation group:", options=filtered_df.columns)

    (xmin, xmax, ymin, ymax) = specify_axes_value_range_plotted(
        filtered_df, data_x, data_y)

    return (animation_frame_settings, animation_group_settings, xmin, xmax, ymin, ymax)

# SETUP AXES AND HOVER DATA


def guided_setup_axes_and_hover_data(df, discrete_columns, continous_columns, discrete_axis):
    (
        x_col,
        y_col,
        data_on_hover_col) = st.columns(3)

    if discrete_axis == "x":
        xcolumns = discrete_columns
        ycolumns = continous_columns

    elif discrete_axis == "y":
        ycolumns = discrete_columns
        xcolumns = continous_columns

    with x_col:
        data_x = st.selectbox(label="data on x-axis", options=xcolumns)

    with y_col:
        data_y = st.selectbox(label="data on y-axis", options=ycolumns)

    with data_on_hover_col:
        data_on_hover = st.multiselect(
            label="data on hover:", options=df.columns)

    return data_x, data_y, data_on_hover


def semiguided_setup_axes_and_hover_data(df, discrete_columns, continous_columns, discrete_axis):
    (
        x_col,
        y_col,
        data_on_hover_col) = st.columns(3)

    if discrete_axis == "x":
        xcolumns = discrete_columns
        ycolumns = continous_columns

    elif discrete_axis == "y":
        ycolumns = discrete_columns
        xcolumns = continous_columns

    elif discrete_axis == "either/neither":
        ycolumns = df.columns
        xcolumns = df.columns

    with x_col:
        data_x = st.selectbox(label="data on x-axis", options=xcolumns)

    with y_col:
        data_y = st.selectbox(label="data on y-axis", options=ycolumns)

    with data_on_hover_col:
        data_on_hover = st.multiselect(
            label="data on hover:", options=df.columns)

    return data_x, data_y, data_on_hover


def unguided_setup_axes_and_hover_data(df):
    (
        x_col,
        y_col,
        data_on_hover_col) = st.columns(3)

    with x_col:
        data_x = st.selectbox(label="data on x-axis", options=df.columns)

    with y_col:
        data_y = st.selectbox(label="data on y-axis", options=df.columns)

    with data_on_hover_col:
        data_on_hover = st.multiselect(
            label="data on hover:", options=df.columns)

    return data_x, data_y, data_on_hover


def semiguided_setup_axes_hover_and_size_data(df, discrete_columns, continous_columns, discrete_axis):

    (data_x, data_y, data_on_hover) = semiguided_setup_axes_and_hover_data(
        df, discrete_columns, continous_columns, discrete_axis)

    data_sized = st.selectbox(
        label="data sized:", options=continous_columns)

    return data_x, data_y, data_on_hover, data_sized


def unguided_setup_axes_hover_and_size_data(df, continous_columns):

    (data_x, data_y, data_on_hover) = unguided_setup_axes_and_hover_data(
        df)

    data_sized = st.selectbox(
        label="data sized:", options=continous_columns)

    return data_x, data_y, data_on_hover, data_sized
