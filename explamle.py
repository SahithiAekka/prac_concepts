from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def start():
    return "welcome to flask basics"

@app.route('/main1')
def main1():
    print("Hello, World! and 67686")
    return "Hello, World!"

@app.route('/main2', methods=['GET', 'POST'])
def main2():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="POST">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)


