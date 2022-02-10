import sys
import streamlit as st


def import_utils():
    sys.path.append('../src')
    from src. format_util_plotly.title import (
        centre_title,
        align_right_title,
        align_left_title,
    )

    from src. format_util_plotly.legend_scale import (
        show_legend_scale, hide_legend_scale
    )
    from src. format_util_plotly.axes import (
        show_yaxes_ticks,
        start_axes_from_zero_intersect,
    )

    return (centre_title,
            align_right_title,
            align_left_title, show_legend_scale, hide_legend_scale, show_yaxes_ticks,
            start_axes_from_zero_intersect)


(centre_title,
 align_right_title,
 align_left_title, show_legend_scale, hide_legend_scale, show_yaxes_ticks,
 start_axes_from_zero_intersect) = import_utils()


def update_title_legend_intercept(fig):

    title_text = st.text_input("title:")

    fig.update_layout(title=title_text)

    title_pos_col, legend_viz_col, zero_axes_col = st.columns(3)

    with title_pos_col:
        title_pos = st.radio(
            "title position:",
            ('left align', 'centre', 'right align'), key='title_pos')

        if title_pos == 'centre':
            centre_title(fig)
        if title_pos == 'right align':
            align_right_title(fig)
        if title_pos == 'left align':
            align_left_title(fig)

    with legend_viz_col:
        legend_viz = st.radio(
            "show legend/scale:",
            ('yes', 'No'), key='legend_viz')

        if legend_viz == 'yes':
            show_legend_scale(fig)
        if legend_viz == 'No':
            hide_legend_scale(fig)

    with zero_axes_col:
        show_yaxes_ticks(fig)

        zero_intersect = st.radio(
            "start axes from zero intersect:", ("yes", "auto"), key='zero_intersect')

        if zero_intersect == 'yes':
            start_axes_from_zero_intersect(fig)
        if zero_intersect == 'Auto':
            fig.update_yaxes(
                rangemode="normal")
            fig.update_xaxes(
                rangemode="normal")

    return fig
