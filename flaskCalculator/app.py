from flask import Flask,request
from functionsCalculator import functions

app = Flask(__name__)

@app.route('/calculator', methods = ['POST'])
def calculator():
    first_number = request.json['first_number']
    second_number = request.json['second_number']
    operator = request.json['operator']
    output = functions[operator](first_number,second_number)
    return ({"result": output})

