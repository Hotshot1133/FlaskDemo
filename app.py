from flask import Flask,render_template, url_for
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return render_template('index.html')
    return app
app = create_app()

