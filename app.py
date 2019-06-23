from flask import Flask, request, render_template
from module import tech
app = Flask(__name__, template_folder='templates')
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/", methods = ['POST'])
def csvfile():
    try:
        csv_filepath = tech.csv_tech()
        if csv_filepath is None:
            return "ERROR 404"
        else:
            return render_template("employer.html", result=csv_filepath)
    except:
        return "ERROR"
 
if __name__ == '__main__':
    app.run(debug=True)
