import plotly.express as px
from pandas.api.types import is_numeric_dtype


def basic_scatterplot_color_cat(df, data_x, data_y, data_sized, data_colored, data_on_hover, plot_color_scale):

    return px.scatter(data_frame=df,
                      x=data_x,
                      y=data_y,
                      size=data_sized,
                      color=data_colored,
                      hover_data=data_on_hover,
                      color_discrete_sequence=getattr(
                          px.colors.qualitative, plot_color_scale)
                      )


def basic_scatterplot_color_seq(df, data_x, data_y, data_sized, data_colored, data_on_hover, plot_color_scale):

    return px.scatter(data_frame=df,
                      x=data_x,
                      y=data_y,
                      size=data_sized,
                      color=data_colored,
                      hover_data=data_on_hover,
                      color_continuous_scale=plot_color_scale
                      )


def adv_scatterplot_without_trend(df,
                                  data_x,
                                  data_y,
                                  data_on_hover,
                                  data_sized,
                                  data_colored,
                                  plot_color_scale,
                                  logx_settings,
                                  logy_settings):
    if is_numeric_dtype(df[data_x]):
        return px.scatter(data_frame=df,
                          x=data_x,
                          y=data_y,
                          size=data_sized,
                          color=data_colored,
                          hover_data=data_on_hover,
                          color_continuous_scale=plot_color_scale,
                          log_x=logx_settings,
                          log_y=logy_settings,
                          )
    else:
        px.scatter(data_frame=df,
                   x=data_x,
                   y=data_y,
                   size=data_sized,
                   color=data_colored,
                   hover_data=data_on_hover,
                   color_discrete_sequence=getattr(
                       px.colors.qualitative, plot_color_scale),
                   log_x=logx_settings,
                   log_y=logy_settings,
                   )


def adv_scatterplot_with_trend(df,
                               data_x,
                               data_y,
                               data_on_hover,
                               data_sized,
                               data_colored,
                               plot_color_scale,
                               logx_settings,
                               logy_settings,
                               trendline_settings,
                               trendline_scope_settings):
    return px.scatter(data_frame=df,
                      x=data_x,
                      y=data_y,
                      size=data_sized,
                      color=data_colored,
                      hover_data=data_on_hover,
                      color_continuous_scale=plot_color_scale,
                      log_x=logx_settings,
                      log_y=logy_settings,
                      trendline=trendline_settings,
                      trendline_scope=trendline_scope_settings
                      )
