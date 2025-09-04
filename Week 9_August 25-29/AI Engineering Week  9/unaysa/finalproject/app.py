from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/imgGen')
def imgGen():
    return render_template('/pages/imgGen.html')

@app.route('/pages/codie.html')
def codie():
    return render_template('/pages/codie.html')
if _name_ == '_main_':
app.run(debug=True)

