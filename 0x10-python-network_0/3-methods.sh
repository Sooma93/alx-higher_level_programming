#!/bin/bash
# disply all HTTP method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
