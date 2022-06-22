#!/usr/bin/env python3

import re
import operator
import csv

errors = {}
per_user = {}

with open('syslog.log', 'r') as syslog:
    for line in syslog:
        error = re.search(r"ticky: ERROR ([\w ]*) \(([\w]*)\)", line)
        if error != None:
            err = error.group(1)
            user = error.group(2)
            if err in errors:
                errors[err] = errors.get(err,0) + 1
            else:
                errors[err] = 1

            if user in per_user:
                a,b = per_user[user]
                per_user[user] = [a+1,b]
            else:
                per_user[user] = [1,0]

        info = re.search(r"ticky: INFO ([\w ]*) \[([\w \#]*)\] \((\w*)\)", line)
        if info != None:
            user=info.group(3)
            if user in per_user:
                a,b = per_user[user]
                per_user[user] = [a,b+1]
            else:
                per_user[user] = [0,1]

with open('error_message.csv', 'w') as em:
    ew = csv.writer(em)
    ew.writerow(['Error', 'Count'])
    for error in sorted(errors.items(), key=operator.itemgetter(1), reverse=True):
        ew.writerow(error)

with open('user_statistics.csv', 'w') as us:
    uw = csv.writer(us)
    uw.writerow(['Username', 'INFO', 'ERROR'])
    for user in sorted(per_user.items(), key=operator.itemgetter(0)):
        name, erin = user
        uw.writerow([name, erin[1], erin[0]])