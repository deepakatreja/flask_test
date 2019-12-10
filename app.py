from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main <a href="/add/23/19">add</a>
'''

@app.route("/add/<int:a>/<int:b>")
def api_info(a, b):
    return str(a+b)

if __name__ == '__main__': 
  
    app.run(debug=True, host='0.0.0.0') 
    


# from flask import Flask, jsonify
# myapp = Flask(__name__)


# @myapp.route("/")
# def hello():
#     return "hello world"


# # @myapp.route("/deepak")
# # def deepak():
# #     return "hello deepak"

# # @myapp.route("/manish")
# # def manish():
# #     return "hello manish"

# # @myapp.route("/sahil")
# # def sahils():
# #     return "hello sahil"

# # if __name__ == '__main__': 

# # app.run(debug=True, host='0.0.0.0') 

