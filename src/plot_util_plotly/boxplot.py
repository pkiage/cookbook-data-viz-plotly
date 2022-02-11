import plotly.express as px


# df, data_x, data_y, data_colored, data_on_hover, plot_color_scale
def basic_boxplot(dataframe, data_x, data_y, data_colored, data_on_hover, plot_color_scale):
    return px.box(data_frame=dataframe,
                  x=data_x,
                  y=data_y,
                  color=data_colored,
                  hover_data=data_on_hover,
                  color_discrete_sequence=getattr(
                      px.colors.qualitative, plot_color_scale)
                  )


def adv_boxplot(df, data_x, data_y, data_colored, data_on_hover, plot_color_scale, points_settings,
                notch_settings, orientation_settings, boxmode_settings,
                logx_settings, logy_settings):
    return px.box(df,
                  x=data_x,
                  y=data_y,
                  color=data_colored,
                  hover_data=data_on_hover,
                  color_discrete_sequence=getattr(
                      px.colors.qualitative, plot_color_scale),
                  points=points_settings,
                  orientation=orientation_settings,
                  notched=notch_settings,
                  boxmode=boxmode_settings,
                  log_x=logx_settings,
                  log_y=logy_settings
                  )


def adv_animated_boxplot(df, data_x, data_y, data_colored, data_on_hover, plot_color_scale, points_settings,
                         notch_settings, orientation_settings, boxmode_settings,
                         logx_settings, logy_settings, animation_frame_settings, animation_group_settings,
                         xmin, xmax, ymin, ymax):
    return px.box(df,
                  x=data_x,
                  y=data_y,
                  color=data_colored,
                  hover_data=data_on_hover,
                  color_discrete_sequence=getattr(
                      px.colors.qualitative, plot_color_scale),
                  points=points_settings,
                  orientation=orientation_settings,
                  notched=notch_settings,
                  boxmode=boxmode_settings,
                  log_x=logx_settings,
                  log_y=logy_settings,
                  animation_frame=animation_frame_settings,
                  animation_group=animation_group_settings,
                  range_x=[xmin, xmax],
                  range_y=[ymin, ymax]
                  )
