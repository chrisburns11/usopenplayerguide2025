from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    section = request.args.get("section", "Welcome Message")
    dark_mode = request.cookies.get("darkMode", "false")
    resp = make_response(render_template("index.html", section=section, dark_mode=dark_mode))
    return resp

if __name__ == "__main__":
    app.run(debug=False, port=5001)
