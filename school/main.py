import os
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap 


app = Flask(__name__)
bootstrap = Bootstrap(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/update")
def update():
    return render_template('update.html')

@app.route("/updated", methods=['POST'])
def updated():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('complete.html')

@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route('/deleted', methods=['POST'])
def deleted():
    file = request.form['file']
    target = os.path.join(APP_ROOT, 'images')
    try:
        destination = "/".join([target,file])
        os.remove(destination)
        return render_template("complete.html")
    except:
        return render_template("incomplete.html")

@app.route("/logged")
def logged():
    return render_template('complete.html')

@app.route('/uploaded', methods=['POST'])
def uploaded():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('complete.html')

if __name__ == "__main__":
    app.run(port=5001, debug=True)