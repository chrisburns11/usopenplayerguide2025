from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    section = request.args.get("section", "Welcome Message")
    return render_template("index.html", section=section)

if __name__ == "__main__":
    app.run(debug=False, port=5001)