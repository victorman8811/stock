from flask import Flask
import json
from flask import render_template
app = Flask(__name__)  # __name__目前執行的模組


@app.route("/")  # 函式的裝飾()
def home():
    a = [{'name': '台積', 'id': '0000', 'price': '590', 'percent': '+1.37%', 'time': '2134上市'},
         {'name': '台積1', 'id': '5000', 'price': '1590',
          'percent': '+11.37%', 'time': '12134上市'},
         {'name': '台積2', 'id': '4000', 'price': '2590',
          'percent': '+21.37%', 'time': '22134上市'},
         {'name': '台積3', 'id': '3000', 'price': '3590',
             'percent': '+31.37%', 'time': '32134上市'},
         {'name': '台積4', 'id': '2000', 'price': '4590',
             'percent': '+41.37%', 'time': '42134上市'},
         {'name': '台積5', 'id': '1000', 'price': '5590', 'percent': '+51.37%', 'time': '52134上市'}]
    return json.dumps(a)


@app.route("/home")
def index():
    return render_template("homepage.html")


@app.route("/homeuser")
def indexuser():
    return render_template("homepage_user.html")


@app.route("/homestock")
def indexstock():
    return render_template("stock.html")


@app.route("/favorite")
def indexfav():
    return render_template("favorite.html")


@app.route("/recommend")
def indexrec():
    return render_template("recommend.html")


@app.route("/register")
def indexreg():
    return render_template("register.html")


@app.route("/a")
def indexa():
    return render_template("a.html")


if __name__ == "__main__":
    app.run()
