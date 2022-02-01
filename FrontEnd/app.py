from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/prediction", methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form["content"])
        # keys = request.form.keys()
        # for key in keys:
        #     print(key)
        return "<p>Done</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)