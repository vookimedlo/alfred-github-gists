#!/usr/bin/env python3

#########################################################
# License: GPLv3
# Author: Michal Duda <github@vookimedlo.cz>
# Home: https://github.com/vookimedlo/alfred-github-gists
# Project: alfred-github-gist
#
#########################################################

import queue
import base64
import io
import json
import os
import re
import sys
import urllib.request
from urllib.request import urlopen

query = sys.argv[1]
queryPattern = re.compile(query, re.I)

user = os.getenv('user')
token = os.getenv('personalToken')
cache = os.getenv('cache')

# Just a very simple caching
#
if os.path.isfile(cache) and os.path.getsize(cache) == 0:
    data = []
    url = 'https://api.github.com/users/' + user + '/gists'
    auth = {'Authorization': 'Basic ' + (base64.b64encode((user + ':' + token).encode('utf-8',errors = 'strict'))).decode()}

    linkPattern = re.compile('<(https://[^>]+)>\s*;\s*rel="next"')

    queue = queue.Queue()
    queue.put(url)

    while not queue.empty():
        queuedUrl = queue.get()
        response = urlopen(urllib.request.Request(queuedUrl, headers=auth))
        link = response.getheader('Link')
        content = response.read()
        partialData = json.loads(content)

        # Join multiple json data
        #
        for i in range(0, len(partialData)):
            data.append(partialData[i])

        if link:
            result = linkPattern.search(link)
            if result:
                queue.put(result.group(1))

    with io.open(cache, 'w', encoding='utf8') as cacheFile:
        dumpedData = json.dumps(data, ensure_ascii=False)
        cacheFile.write(str(dumpedData))
else:
    with io.open(cache, 'r', encoding='utf8') as cacheFile:
        data = json.loads(cacheFile.read())

# Alfred menu items
#
alfreditems = {"items": []}

for item in data:
    title = list(item['files'].keys())[0]
    mysortkey = title.lower()
    description = item['description']
    url = item['html_url']

    if query != "" and not queryPattern.search(str(title)):
        continue

    icon = "gist.png" if item["public"] else "gist-secret.png"

    alfreditems['items'].append({
        "mysortkey": mysortkey,
        "uid": title,
        "title": title,
        "subtitle": description,
        "autocomplete": title,
        "arg": url,
        "icon": {
            "path": icon
        }
    })

# Sort gists
#
lines = sorted(alfreditems['items'], key=lambda k: k['mysortkey'], reverse=False)
dump = json.dumps({'items': lines}, indent=4)

sys.stdout.write(dump)

