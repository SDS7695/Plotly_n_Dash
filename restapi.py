from flask import Flask, jsonify
  
# creating a Flask app
app = Flask(__name__)
  
    
# Defining endpoints
@app.route('/endpoint1', methods = ['GET', 'POST'])
def home():
    return jsonify({'text': "Hello World"})
  
    
if __name__ == '__main__':
  
    app.run(debug = True)