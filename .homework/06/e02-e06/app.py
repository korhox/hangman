from flask import Flask
from datetime import datetime
import htmlhelper
import random
from flask import request
from flask import jsonify
import json

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root


@app.route("/hello")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/juuso")
def juuso():
    return "<p>Juuso</p>"


@app.route("/date")
def date():
    date = datetime.now()
    return f"<p>{date}</p>"


@app.route("/date5")
def date5():
    return htmlhelper.generate_html_page("date", f"<p>{datetime.now()}</p>")


@app.route("/slots")
def slots():
    images = [
        "/static/peach.svg",
        "/static/eggplant.svg",
        "/static/chili.svg",
    ]

    slots = []
    for i in range(3):
        slots.append(random.randint(0, 2))

    imageHtml = f""
    win = True
    last = slots[0]
    for i in slots:
        imageHtml += f"<img src='{images[i]}' width='40' height='40'>"
        if last != i:
            win = False
        last = i

    if win:
        winHtml = "<p class='text-center text-success'>Congrats! You won the slot game!</p>"
    else:
        winHtml = "<p class='text-center text-danger'>No win.</p>"

    return htmlhelper.generate_html_page("date", f"""
        <p class='text-center mt-5'>{imageHtml}</p>
        {winHtml}
        """.strip())


@app.route('/bmi')
def bmi_calculator():
    mass = float(request.args.get('mass'))
    height = float(request.args.get('height'))

    bmi = mass / (height ** 2)
    return f"Calculated BMI is: {bmi}"


@app.route('/bmi/json')
def bmi_calculatorjson():
    mass = float(request.args.get('mass'))
    m = (float(request.args.get('height')) / 100) ** 2

    bmi = mass / m
    data = {
        "result": bmi
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
