def hide_legend_scale(fig):
    fig.update_layout(
        showlegend=False,
    )
    fig.update(
        layout_coloraxis_showscale=False)


def show_legend_scale(fig):
    fig.update_layout(
        showlegend=True
    )
    fig.update(
        layout_coloraxis_showscale=True)
