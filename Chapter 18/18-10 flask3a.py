from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
    return render_template('flask3.html', thing=thing, place=place)  
    
    # need to put template files into ./templates/ folder 
    

app.run(port=9996, debug=True)