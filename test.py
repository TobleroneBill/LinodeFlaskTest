from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)

# You can alter the response by using the make response method, and editing its attributes
@app.route('/')
def index():
    response = make_response("<h1>LOL</h1>")
    response.set_cookie('lol')
    return response

@app.route('/templateExample')
def templateExample():
    return render_template('templateExample.html')

@app.route('/cssTest')
def cssTest():
    return render_template('cssTest.html')

# can manually change the response header to code 400 (error), or others if ur silly
@app.route('/agent')
def agent():
    UA = request.headers.get('User-Agent')
    return f"<h1>You are using {UA}</h1>" , 400

# Redirects to another link (response 300)
@app.route('/youtube')
def youtube():
    return redirect("https://www.youtube.com/")

@app.route('/user/<name>')
def name(name):
    return render_template('username.html', JOHN=name)


if __name__ == "__main__":
    app.run(debug=True)