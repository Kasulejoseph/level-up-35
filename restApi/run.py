from flask import Flask, Request, jsonify,json

app = Flask(__name__)
@app.route('/level-up/learners', methods =['GET', 'POST'])

def get_learners():
    learners_list = [
        {'musoke':[{'age':20, 'sex':'male','class':'s.1'}]},
        {'ivan':[{'sex':'male','class':'s.1'}]},
        {'hassan':[{'sex':'male','class':'s.1'}]}
        ]
    if len(learners_list)==0:
        return jsonify({"message": "no learners available"}),404
    return jsonify ({"learner":learners_list, "number":len(learners_list)}),200

if __name__ == '__main__':
    app.run(debug=True)