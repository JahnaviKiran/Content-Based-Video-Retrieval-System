from flask import Flask, jsonify, request
from project import Project
# from temp import temp as Project
  
# creating a Flask app
app = Flask(__name__)
  
project = Project()
project.getQAModelReady()
print("Project ready")
  
  
@app.route('/query', methods = ['GET', 'POST'])
# def answer():
#     print(request.args)
#     if 'question' not in request.args:
#         return jsonify(None)
#     question = request.args['question']
  
#     if 'videoId' not in request.args:
        
#         return jsonify(project.executeQuery(question))
#     videoId = request.args['videoId']
#     print(videoId)
#     return jsonify(project.executeQuery(question, videoId))

def answer():
    if 'question' not in request.args:
        res = jsonify(None)
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    else:
        question = request.args['question']
        if 'videoId' not in request.args:
            res = jsonify(project.executeQuery(question))
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res
        else:
            videoId = request.args['videoId']
            res = jsonify(project.executeQuery(question, videoId))
            res.headers['Access-Control-Allow-Origin'] = '*'
            return res

# driver function
if __name__ == '__main__':
  
    app.run(debug = False, port=5055)