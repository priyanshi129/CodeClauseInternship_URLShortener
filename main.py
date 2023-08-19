import pyshorteners
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def index():
    
    if request.method == 'POST':
        url=request.form["long_url"]
        s=pyshorteners.Shortener()
    
        
        return render_template('index.html',output=s.tinyurl.short(url))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)



