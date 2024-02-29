#!/bin/bash
# script sends request to URL to displat body size 
curl -s "$1" | wc -c
