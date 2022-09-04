from flask import Flask, request, redirect,render_template
app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return me("me.html")

@app.route('/mypage/contact')
def contact():
    return contact("secound.html")


