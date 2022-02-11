import streamlit as st


def st_boxplot_intro():
    st.write(
        "https://plotly.github.io/plotly.py-docs/generated/plotly.express.box.html")

    st.write(
        "This graph can interpret the following datasets as-is: tips, iris, experiment, gapminder, and wind.")

    st.write("Use sidebar on the left for:")
    st.write("i) color scheme")
    st.write("ii) bulk and searchable filter of graph values")
    st.write("iii) additional box plot options")
