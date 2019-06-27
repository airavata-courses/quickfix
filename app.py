from flask import Flask, request, render_template
from module import tech
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    #return render_template('index.html', title='Home')
    try:
        result1,result2,result3,result4,result5,result6,result7,result8 = tech.csv_tech()
        if result1 is None:
            return "ERROR 404"
        else:
            return render_template("index.html",len = len(result1), results=result1
            ,results2=result2,results3=result3,results4=result4,
            results5=result5,results6=result6,results7=result7,results8=result8)
    except:
        return "ERROR"
 
if __name__ == '__main__':
    app.run(debug=True)
