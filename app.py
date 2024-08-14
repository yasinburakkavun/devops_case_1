from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "BC4M"})

def health_check():
    return jsonify({"status": "healthy"})

@app.route("/", methods=["POST"])
def echo():
    data = request.get_json()  
    return jsonify(data)  

if __name__ == "__main__":
    app.run(debug=True)

