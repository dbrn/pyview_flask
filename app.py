from flask import Flask, render_template, request
import webview
import threading

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/response")
def response():
    username = request.args.get("user")
    lower = False
    upper = False
    number = False
    success = False
    try:
        if str(username)[-1].isnumeric():
            number = True
    except IndexError:
        number = False
    for letter in username:
        if str(letter).islower():
            lower = True
        if str(letter).isupper():
            upper = True
        if upper and lower:
            break
    if lower and upper and number:
        success = True
    print(username)
    return render_template("response.html", username=username, success=success,
                           number=number, lower=lower, upper=upper)


if __name__ == "__main__":
    thread = threading.Thread(target=app.run)
    thread.daemon = True
    thread.start()
    window = webview.create_window("Username checker", "http://127.0.0.1:5000",
                                   resizable=False, text_select=False,
                                   frameless=False, min_size=(500, 500),
                                   confirm_close=True)
    window.height = 500
    window.width = 500
    webview.start(gui="qt")
