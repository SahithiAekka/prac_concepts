from flask import Flask

app = Flask(__name__)

# print(__name__) # __main__
# __name__ is a speacial attribute you can find out what is teh current func/module

@app.route("/")
# "/" is called the homepage 
# @ - Python decorator 
def hello_world():
    return "<p>Hello, World!</p>"

# runs the flask app instead of runnig it on command line 
if __name__ == "__main__":
    app.run()
    
    
# Python decorator - Func that gives additional functonalities to an exsiting function 