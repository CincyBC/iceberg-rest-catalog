#!/bin/bash

uv lock --upgrade

git add uv.lock
git commit -m "Upgrade packages"
git push 
