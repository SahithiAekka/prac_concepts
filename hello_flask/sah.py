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
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e0f7fa, #fce4ec);
                color: #333;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .card {
                background: white;
                padding: 3rem 4rem;
                border-radius: 1rem;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
            }
            img {
                border-radius: 50%;
                width: 160px;
                height: 160px;
                object-fit: cover;
                margin-bottom: 1.5rem;
                border: 4px solid #e0f7fa;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            h2 {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                color: #00695c;
            }
            p {
                font-size: 1.2rem;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/static/sahithi.jpg" alt="Sahithi profile photo">
            <h1>Hello, I'm Sahithi 👋</h1>
            <h2>Cloud Engineer | University of Michigan</h2>
            <p>AWS Certified | Passionate about building cloud-native solutions</p>
        </div>
    </body>
    </html>
    """

# Different route using app.route decorator
@app.route("/Certs")
def aws_certs():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sahithi | Cloud Engineer</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e0f7fa, #fce4ec);
                color: #333;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .card {
                background: white;
                padding: 3rem 4rem;
                border-radius: 1rem;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            h2 {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                color: #00695c;
            }
            p {
                font-size: 1.2rem;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AWS Certified Solutions Achitect </h1>
            <h2>AWS Certified  AI Practioner</h2>
            <p>AWS Certified  Cloud Practioner</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
