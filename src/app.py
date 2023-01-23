from flask import Flask, request
from flask_restful import Api
from handlers.generateClusters.generateClustersHandler import generateClustersHandler

app = Flask(__name__)
api = Api(app)

# Do we open one connection, or a connection for each class in mongo?

@app.route('/')
def index():
    return 'Hello World', 200

@app.route('/generateClusters', methods=['GET', 'POST'])
def generateClusters():
    if request.method == 'POST':
        return generateClustersHandler(request.form['contractAddress'])

    return 'Invalid method', 405

if __name__ == '__main__':
    app.run(port=8010) # run flask app