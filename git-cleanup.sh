#!/bin/bash

git fsck
git prune
git reflog expire --expire=now --all
git repack -ad
git prune