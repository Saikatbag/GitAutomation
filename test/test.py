from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

# @app.route('/test')
# def api_root():
#     return "Wellcome to Git web api"


@app.route('/', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        a = json.dumps(request.json)
        data = json.loads(a)
        print(type(data))
        print("###############################################################################################")
        a = "commits"
        b = "action"
        if a in data:
            print(data["commits"][0]["id"])
            print(data["commits"][0]['author']['username'])
            print(data['ref'])
            print(data['commits'][0]['timestamp'])
        elif b in data:
            if data["action"] == "opened":
                print("Pull_Request")
                print("AUTHOR")
                print(data["pull_request"]["base"]['label'])
                print("TO -")
                print(data["pull_request"]["head"]["ref"])
                print("FROM - ")
                print(data["pull_request"]["base"]["ref"])
                print('Time')
                print(data["pull_request"]["updated_at"])
                print(data["pull_request"]["id"])
            elif data["action"] == "closed":
                print("Marge")
                print("AUTHOR")
                print(data["pull_request"]["base"]['label'])
                print("TO -")
                print(data["pull_request"]["head"]["ref"])
                print("FROM - ")
                print(data["pull_request"]["base"]["ref"])
                print('Time')
                print(data["pull_request"]["updated_at"])
                print(data["pull_request"]["id"])
            else:
                print('nothing pull')
        else:
            print("not valid")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return json.dumps(request.json)


if __name__ == '__main__':
    app.run(debug=True)
