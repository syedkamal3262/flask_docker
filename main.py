from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def main():
    return "Hello World!"
    
@app.route('/hello_world',methods=["GET"])
def hello_world():
    a=5
    b=5
    return f"another Hello World!{a+b}"


@app.route('/json_data',methods=["GET"])
def data():
    try:
        dict_={
            "name":"kamal",
            "class":"KAI"
            }
        return jsonify(dict_), 200
    except:
        return "failed", 500


@app.route('/arguments',methods=["GET"])
def arguments():
    try:
        page=request.args.get('page')
        name=request.args.get('name')
        all_params = request.args.to_dict()
        return jsonify(all_params), 200
    except:
        return "failed", 500

@app.route('/send_data',methods=["GET","POST"])
def a():
    if request.method == "GET":
        return print("wrong"),400
    if request.method == "POST":
        if request.content_type == "application/json":
            data = request.json
        else:
            data = request.data
        return data, 200

@app.route('/<string:str>',methods=["GET"])
def dynamic(str):
    a=100
    b=200
    return f"heloo-> {str}"

@app.route('/value=<int:num>',methods=["GET"])
def dyn(num):
    a=100
    b=200
    return f"value-> {num}"

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port= 8000
        )
