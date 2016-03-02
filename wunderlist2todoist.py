import argparse
from getpass import getpass
import json
import time
from pytodoist import todoist
from pytodoist.todoist import RequestError
import logging as log

# try:
#     value = request(*args, **kargs)
#     break
# except RequestError:
#     log.error("Slepping for a minute...")
#     time.sleep(60)

class WunderlistToTodoist():

    def __init__(self, email, password):
        self.user = todoist.login(email, password)

    def parse_wunderlist_dump(self, file_path):
        # Parse the JSON file
        with open(file_path) as f:
            contents = json.load(f)['data']

            lists = {}
            for lst in contents['lists']:
                list_title = lst['title']
                list_id = lst['id']

                # Check if the list exists
                project = self.user.get_project(list_title)

                log.info("Adding list {}".format(list_title))
                if project is None:
                    project = self.user.add_project(list_title)

                lists[list_id] = project

            for w_task in contents['tasks']:
                lst = lists[w_task['list_id']]
                task = w_task['title']

                log.info("Adding task {} to list {}".format(task, lst.name))
                t_task = lst.add_task(task)

                # update task information
                if w_task['completed']:
                    t_task.complete()
                else:
                    t_task.uncomplete()
                time.sleep(1.2)


if __name__ == '__main__':

    log.basicConfig(filename='wunderlist2todoist.log', level=log.INFO)

    # Check command line arguments
    parser = argparse.ArgumentParser(description="Export Wunderlist JSON file into\
                                                  Todoist")
    parser.add_argument('email')
    parser.add_argument('wunderlist_dump')
    args = parser.parse_args()

    # Receive password
    args.password = getpass()

    # Establish connection to Todoist
    exporter = WunderlistToTodoist(args.email, args.password)

    # And make the export
    exporter.parse_wunderlist_dump(args.wunderlist_dump)
