#!/bin/bash

######
# I (Scott) got this from jerrykrinock and made a few little changes for my workflow

######
# This script create a new repo on github.com, then pushes the
# local repo from the current directory to the new remote.

# It is a fork of https://gist.github.com/robwierzbowski/5430952/.
# Some of Rob's lines just didn't work for me, and to fix them I
# needed to make it more verbose so that a mere electrical engineer could understand it.

# This script gets a username from .gitconfig.  If it indicates
# that your default username is an empty string, you can set it with
# git config --add github.user YOUR_GIT_USERNAME

# Gather constant vars
CURRENTDIR=${PWD##*/}
# GITHUBUSER=$(git config github.user)
GITHUBUSER=se42
 
# Get user input
echo "Enter name for new repo, or just <return> to make it $CURRENTDIR"
read REPONAME
echo "Enter username for new, or just <return> to make it $GITHUBUSER"
read USERNAME

REPONAME=${REPONAME:-${CURRENTDIR}}
USERNAME=${USERNAME:-${GITHUBUSER}}
DESCRIPTION="Source control for $REPONAME project"

echo "Creating new repo named $REPONAME on github.com in user account $USERNAME..."

# Curl some json to the github API oh damn we so fancy
curl -u $USERNAME https://api.github.com/user/repos -d "{\"name\": \"$REPONAME\", \"description\": \"${DESCRIPTION}\", \"private\": false, \"has_issues\": true, \"has_downloads\": true, \"has_wiki\": true}"
 
# Set the freshly created repo to the origin
git remote add origin https://github.com/$USERNAME/$REPONAME.git
