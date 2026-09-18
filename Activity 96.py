from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the main webpage
    return render_template('index.html')

if __name__ == '__main__':
    # Starts the local development server
    app.run(debug=True)