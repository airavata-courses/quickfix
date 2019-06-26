from flask import Flask, request, render_template
from module import tech
app = Flask(__name__, template_folder='templates')
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/", methods = ['POST'])
def csvfile():
    try:
        result = tech.csv_tech()
        if result is None:
            return "ERROR 404"
        else:
            return render_template("jobs.html", result=result)
    except:
        return "ERROR"
 
if __name__ == '__main__':
    app.run(debug=True)
