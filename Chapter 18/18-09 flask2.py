from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)  
    
    # need to put template files into ./templates/ folder 
    

app.run(port=9997, debug=True)