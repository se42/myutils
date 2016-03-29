#!/bin/bash

# I got this command from jerrykrinock who forked from
# https://gist.github.com/robwierzbowski/5430952/
# and changed it to fit my workflow/scripts

REPONAME=$1
USERNAME=$2
DESCRIPTION="Source control for $REPONAME project"

# Curl some json to the github API oh damn we so fancy
curl -u $USERNAME https://api.github.com/user/repos -d "{\"name\": \"$REPONAME\", \"description\": \"${DESCRIPTION}\", \"private\": false, \"has_issues\": true, \"has_downloads\": true, \"has_wiki\": true}"
