from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/get-multiply/<int:num>', methods=['GET'])
def multiply(num):
    book = request.get_json();
    return jsonify({"Multiplication": num * num}), 200
	
# This is for debug mode on
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
