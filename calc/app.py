from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


# @app.route('/add', methods=["GET"])
#TypeError: add_op() missing 2 required positional arguments: 'a' and 'b'
@app.route('/add')
def add_op():
    a = str(request.args.get('a'))
    b = str(request.args.get('b'))
    result = add(a, b)
    return str(result)
    
    
# @app.route('/sub', methods=["POST"])
# @app.route('/sub', methods=["GET"])
@app.route('/sub')
def sub_op():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

    
# @app.route('/mult', methods=["POST"])
@app.route('/mult')
def mult_op():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)
    
    
# @app.route('/div', methods=["POST"])
@app.route('/div')
def div_op():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)


# def sample_code():
#     return "Hello!"

# response = {
#     add : 'add',
#     sub : 'sub',
#     mult : 'mult',
#     div : 'div'
# }

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

# @app.route('/math/<int:op>')
@app.route('/math/<op>')
def math_op(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[op](a, b)
    return str(result)