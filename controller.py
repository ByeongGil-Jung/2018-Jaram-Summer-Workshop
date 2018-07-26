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
import time

app = Flask(__name__)


# UPLOAD_FOLDER = os.path.basename('uploads')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/input', methods=["POST", "GET"])
def register_user():
    user = None
    repo = None

    if request.method == "POST":
        user = request.form["user"]
        repo = request.form["repo"]

    elif request.method == "GET":
        user = request.args.get("user")
        repo = request.args.get("repo")

    git_readme, issue_list, pull_request_list = ec.execute(user, repo)

    response_ = json.dumps({"git_readme": git_readme, "issue_list": issue_list, "pull_request_list": pull_request_list})

    return Response(response_, status=200, mimetype="application/json")


@app.route('/noti', methods=["POST"])
def notificate():
    git_readme = None
    issue_list = None
    pull_request_list = None

    issue_len = None
    pull_req_len = None
    user = None
    repo = None

    noti_check = True
    sumething_changed = None

    if request.method == "POST":
        issue_len = int(request.form["issue_len"])
        pull_req_len = int(request.form["pull_req_len"])
        user = request.form["user"]
        repo = request.form["repo"]

    while noti_check:
        git_readme, issue_list, pull_request_list = ec.execute(user, repo)

        current_issue_count = len(issue_list)
        current_pull_req_count = len(pull_request_list)

        if issue_len is not current_issue_count:
            noti_check = False
            issue_len = current_issue_count
            sumething_changed = "Issue"
        elif pull_req_len is not current_pull_req_count:
            noti_check = False
            pull_req_len = current_pull_req_count
            sumething_changed = "Pull Request"

        time.sleep(3)

    response_ = json.dumps({
        "git_readme": git_readme,
        "issue_list": issue_list,
        "pull_request_list": pull_request_list,
        "something_changed": sumething_changed
    })

    return Response(response_, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, port=8011)
