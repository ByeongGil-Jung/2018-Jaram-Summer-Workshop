import urllib.request
from bs4 import BeautifulSoup


def github_url(ID, Repository):
    return "https://github.com/" + ID + "/" + Repository


def parsing(url):
    return BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')


def return_README(html_README):
    README_box = html_README.find("div", "Box Box--condensed instapaper_body md")
    if README_box == None:
        # print("There is no README.md in the repository.")

        return None
    else:
        # print(README_box.find("article", "markdown-body entry-content"))

        return README_box.find("article", "markdown-body entry-content")


def return_list(html):
    box = html.find("div", "border-right border-bottom border-left")
    if box == None:
        # print("There is no Issuses or PR (Status : \"Open\") in the repository")
        
        return []
    else:
        list_ = []
        parsings = box.findAll("a", "link-gray-dark v-align-middle no-underline h4 js-navigation-open")
        for parsing in parsings:
            list_.append(str(parsing.get_text().replace("\n", "").replace("        ", "").replace("      ", "")))
        # print(list_)

        return list_


def execute(user, repo):
    ID = user
    Repository = repo

    url_README = github_url(ID, Repository)
    url_Issues = github_url(ID, Repository) + "/issues"
    url_PR = github_url(ID, Repository) + "/pulls"

    html_README = parsing(url_README)
    html_Issues = parsing(url_Issues)
    html_PR = parsing(url_PR)

    out_readme = str(return_README(html_README))
    out_issue = return_list(html_Issues)
    out_pr = return_list(html_PR)

    return out_readme, out_issue, out_pr
