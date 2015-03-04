__author__ = 'degorenko'

from reporter import report as generate_report


def other_functions():
    # Other modules, which will read and generate output for my module
    print "Here will be code"


def generate_output():
    # read example JSON
    import json
    with open("../sample.json") as json_file:
        json_data = json.load(json_file)

    generate_report.generate_rst(json_data)


generate_output()
