# from flask import Flask

# app = Flask(__name__)

# # print(__name__) # __main__
# # __name__ is a speacial attribute you can find out what is teh current func/module

# @app.route("/")
# # "/" is called the homepage 
# # @ - Python decorator 
# def hello_world():
#     return "<p>Hello, World!</p>"

# # runs the flask app instead of runnig it on command line 
# if __name__ == "__main__":
#     app.run()
    
    
from flask import Flask

app = Flask(__name__)

@app.route("/")
def sah_intro():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sahithi | Cloud Engineer</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

            body {
                margin: 0;
                padding: 0;
                font-family: 'VT323', monospace;
                background-color: #f4f1ea;
                color: #333;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-image: radial-gradient(#ccc 1px, transparent 1px);
                background-size: 20px 20px;
            }

            .card {
                background: #fff8f0;
                padding: 3rem;
                border: 2px solid #333;
                border-radius: 8px;
                box-shadow: 4px 4px 0 #000;
                text-align: center;
                max-width: 500px;
            }

            img {
                border-radius: 8px;
                width: 160px;
                height: 160px;
                object-fit: cover;
                margin-bottom: 1.5rem;
                border: 2px solid #000;
            }

            h1 {
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
            }

            h2 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
                color: #444;
            }

            p {
                font-size: 1.2rem;
                color: #555;
                font-weight: 600;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/static/sahithi.jpg" alt="Sahithi profile photo">
            <h1>Hi, I'm Sahithi 🧠</h1>
            <h2>Cloud Engineer @ University of Michigan</h2>
            <p>AWS Certified | Clean Code Enthusiast | Cloud-Native Builder</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

