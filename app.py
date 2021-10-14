from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        'id':1,
        'title':u'buying grocceries',
        'description':u'burger,momo,sandwhich,pizza',
        'done':False
    },
    {
        'id':2,
        'title':u'playing games',
        'description':u'valo,codm,ark,gi',
        'done':False
    }
]

@app.route("/")
def helloworld():
    return "Hello World"
@app.route("/add-data",methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide The Data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Task Added Successfully"
        })

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })
if(__name__ == "__main__"):
    app.run(debug=True)