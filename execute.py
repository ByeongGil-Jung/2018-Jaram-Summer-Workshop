"""
 Created by IntelliJ IDEA.
 Project: flask_workshop
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-25
 Time: 오후 3:40
"""


def execute(user, repo):
    git_readme = list()
    issue_list = list()
    full_request_list = list()

    test_html = "<p>Test Html</p>"
    test_issue = ["abc", "qwe", "zxc"]
    test_full_requset = ["ABC", "QWE", "ZXC"]

    git_readme = test_html
    issue_list.append(test_issue)
    full_request_list.append(test_full_requset)

    return git_readme, issue_list, full_request_list
