from flask import Flask
import time
from validate_img import val , rename
#
# app = Flask(__name__)
#
#
# @app.route("/",methods = ['GET','POST'])
# def app():
#     val()
#     return "Hello, World!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def samplefunction():
    #access your DB get your results here
    val()
    m,y = val()
    print("Val done")
    rename(m,y)
    print("Rename done")
    return m,y

if __name__ == '__main__':
    port = 8000 #the custom port you want
    app.run(host='0.0.0.0', port=port,debug=True)
