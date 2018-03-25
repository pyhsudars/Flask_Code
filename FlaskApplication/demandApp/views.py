from . import demandApp
from flask import render_template


@demandApp.route('/')
def home():
    """ Home function.
    """
    HomeData = [
        {
            'DemandID': 1000001,
            'Release': "R3",
            'Description': "Some description here."
        },
        {
            'DemandID': 1000002,
            'Release': "R3",
            'Description': "Some description here."
        }
    ]

    return render_template("home.html", homeData=HomeData)
