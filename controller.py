# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: flask
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-21
 Time: 오전 4:52
"""

from flask import Flask, render_template, request, Response
import json
import execute as ec

app = Flask(__name__)


# UPLOAD_FOLDER = os.path.basename('uploads')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/input', methods=["POST", "GET"])
def upload_file():
    user = None
    repo = None

    if request.method == "POST":
        user = request.form["user"]
        repo = request.form["repo"]

    elif request.method == "GET":
        user = request.args.get("user")
        repo = request.args.get("repo")

    git_readme, issue_list, full_request_list = ec.execute(user, repo)

    response_ = json.dumps({"git_readme": git_readme, "issue_list": issue_list[0], "full_request_list": full_request_list[0]})

    return Response(response_, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, port=8030)
