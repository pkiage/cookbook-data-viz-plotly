def start_axes_from_zero_intersect(fig):
    fig.update_yaxes(
        rangemode="tozero")
    fig.update_xaxes(
        rangemode="tozero")


def hide_yaxes(fig):
    fig.update_yaxes(
        visible=False)


def show_yaxes(fig):
    fig.update_yaxes(
        visible=True)


def hide_yaxes_ticks(fig):
    fig.update_yaxes(
        showticklabels=False)


def show_yaxes_ticks(fig):
    fig.update_yaxes(
        showticklabels=True)
