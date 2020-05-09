from redminelib import Redmine

redmine = Redmine("http://127.0.0.1/redmine", username="admin", password="11111111")

project = redmine.project.get('redmine')

print(dir(project))

print(dir(project.issues))

