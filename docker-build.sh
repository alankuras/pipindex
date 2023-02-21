#!/bin/bash
version=1.0
project=pipindex

docker build --no-cache --rm -t $project:$version .
