import json

data_set_options = [
    "carshare",
    "election",
    "experiment",
    "gapminder",
    "iris",
    "medals_wide",
    "medals_long",
    "stocks",
    "tips",
    "wind",
]


def convert_to_bool(var):
    return json.loads(var.lower())
