import sys
import os

from workflow import Workflow3, ICON_DEVELOPER_FOLDER as ICON

PROJECT_DIR = os.environ["PROJECT_DIR"]


def get_projects(wf):
    project_name = wf.args[0]

    projects_list = os.listdir(PROJECT_DIR)
    if project_name is not None:
        projects_list = filter(lambda name: name.startswith(project_name), projects_list)

    for project in projects_list:
        path_project = os.path.join(PROJECT_DIR, project)
        if not os.path.isdir(path_project):
            continue

        wf.add_item(title=project,
                    arg=path_project,
                    valid=True, icon=ICON)

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(get_projects))
