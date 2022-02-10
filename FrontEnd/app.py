from flask import Flask, render_template, request
import prediction

app = Flask(__name__)
predict = prediction.classification()

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/prediction", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        content = request.form["content"]
        answer = predict.predict(content)
        return render_template("result.html", test = answer)

if __name__ == "__main__":
    app.run(debug=True, port=8000)