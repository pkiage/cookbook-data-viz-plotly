
import streamlit as st


import sys


def import_utils():
    sys.path.append('../src')

    from src. format_util_plotly.axes import (
        show_xaxes,
        show_yaxes,
        hide_xaxes,
        hide_yaxes,
        show_yaxes_ticks,
        show_xaxes_ticks,
        hide_yaxes_ticks,
        hide_xaxes_ticks)

    return (
        show_xaxes,
        show_yaxes,
        hide_xaxes,
        hide_yaxes,
        show_yaxes_ticks,
        show_xaxes_ticks,
        hide_yaxes_ticks,
        hide_xaxes_ticks)


(
    show_xaxes,
    show_yaxes,
    hide_xaxes,
    hide_yaxes,
    show_yaxes_ticks,
    show_xaxes_ticks,
    hide_yaxes_ticks,
    hide_xaxes_ticks) = import_utils()


def update_axes_visibility(fig):

    (yaxes_show_col,
     yticks_show_col,
     xaxes_show_col,
     xticks_show_col) = st.columns(4)

    update_yaxes_visibility(fig, yaxes_show_col,
                            yticks_show_col)

    update_xaxes_visibility(fig, xaxes_show_col,
                            xticks_show_col)
    return fig


def update_yaxes_visibility(fig, yaxes_show_col, yticks_show_col):
    with yaxes_show_col:
        yaxes_show = st.radio(
            "show y-axis:",
            ('yes', 'No'), key='yaxes_show')

        if yaxes_show == 'yes':
            show_yaxes(fig)
        if yaxes_show == 'No':
            hide_yaxes(fig)

    if yaxes_show == 'yes':
        with yticks_show_col:
            show_yaxes_ticks(fig)

            yticks_show = st.radio(
                "show y-ticks:", ("yes", "no"), key='yticks_show')

            if yticks_show == 'yes':
                show_yaxes_ticks(fig)
            if yticks_show == 'No':
                hide_yaxes_ticks(fig)

    return fig


def update_xaxes_visibility(fig, xaxes_show_col, xticks_show_col):
    with xaxes_show_col:
        xaxes_show = st.radio(
            "show x-axis:",
            ('yes', 'No'), key='xaxes_show')

        if xaxes_show == 'yes':
            show_xaxes(fig)
        if xaxes_show == 'No':
            hide_xaxes(fig)

    if xaxes_show == 'yes':
        with xticks_show_col:
            show_xaxes_ticks(fig)

            xticks_show = st.radio(
                "show x-ticks:", ("yes", "no"), key='xticks_show')

            if xticks_show == 'yes':
                show_xaxes_ticks(fig)
            if xticks_show == 'No':
                hide_xaxes_ticks(fig)
    return fig
