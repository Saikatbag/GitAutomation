


from flask import Flask, render_template, request
from flask import json
from flask import request
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__,template_folder='template')
# connection to Database
try:
    client = MongoClient("mongodb://localhost:27017")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
db = client.mymongodb  # Select the database
collection = db.appdb  # Select the collection name

@app.route('/', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        a = json.dumps(request.json)
        data = json.loads(a)
        print(type(data))
        a = "commits"
        b = "action"
    
        if a in data:
            # if push in gitgub account then run this and save in mongo dbdata base
            collection.insert_one(
                {
                    "request_id": data["commits"][0]["id"],
                    "author": data["commits"][0]['author']['username'],
                    "action": "PUSH",
                    "from_branch": data['ref'],
                    "to_branch": data['ref'],
                    "timestampe": data['commits'][0]['timestamp']}
            )
            print("One File Push .................")

        elif b in data:
            if data["action"] == "opened":
                # if push Request is come then call this and save in mongo dbdata base
                collection.insert_one(
                    {
                        "request_id": data["pull_request"]["id"],
                        "author": data["pull_request"]["base"]['label'],
                        "action": "PULL REQUEST",
                        "from_branch": data["pull_request"]["base"]["ref"],
                        "to_branch": data["pull_request"]["head"]["ref"],
                        "timestampe": data["pull_request"]["updated_at"]}
                )
                print("A Push Request are comeing .................")
 
            elif data["action"] == "closed":
                # if Marge then call this and save in mongo dbdata base
                collection.insert_one(
                    {
                        "request_id": data["pull_request"]["id"],
                        "author": data["pull_request"]["base"]['label'],
                        "action": "Marge",
                        "from_branch": data["pull_request"]["base"]["ref"],
                        "to_branch": data["pull_request"]["head"]["ref"],
                        "timestampe": data["pull_request"]["updated_at"]}
                )
                print("A Marge Done .................")

            else:
                print('nothing pull')
        else:
            print("not valid")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return json.dumps(request.json)

# this api print last valu 
@app.route('/saikat')
def api_root():
    ab = collection.find_one(
        sort=[( '_id', -1 )])
    return render_template('index.html',name=ab) 

if __name__ == "__main__":
    app.run(debug=True)

