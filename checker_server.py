from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("checker_index.html", y_num=4, x_num=4)

@app.route('/<int:y_num>')
def y_axis(y_num):
    return render_template("checker_index.html", x_num=4, y_num=y_num)

@app.route('/<int:y_num>/<int:x_num>')
def xy_axis(y_num, x_num):
    return render_template("checker_index.html", y_num=y_num, x_num=x_num)

@app.route('/<int:y_num>/<int:x_num>/<string:color1>')
def color_one(y_num, x_num, color1):
    return render_template("checker_index.html", y_num=y_num, x_num=x_num, color1=color1)

@app.route('/<int:y_num>/<int:x_num>/<string:color1>/<string:color2>')
def color_two(y_num, x_num, color1, color2):
    return render_template("checker_index.html", y_num=y_num, x_num=x_num, color1=color1, color2=color2)



if __name__== "__main__":
    app.run(debug=True)