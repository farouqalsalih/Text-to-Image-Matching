from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Process the search query here (e.g., search in a database)
    return f'Searching for: {query}'

if __name__ == '__main__':
    app.run(debug=True)