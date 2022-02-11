
import streamlit as st


def scatterplot_intro():
    st.write(
        "https://plotly.com/python-api-reference/generated/plotly.express.scatter")

    st.write(
        "This graph can interpret the following datasets as-is: tips, iris, experiment, gapminder, wind, car share, medals long, medals wide, stocks, and election.")

    st.write("Use sidebar on the left for:")
    st.write("i) color scheme")
    st.write("ii) bulk and searchable filter of values")
    st.write("iii) additional scatter plot options")
