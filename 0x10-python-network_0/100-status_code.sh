#!/bin/bash
#send request to URL and display statues code
curl -so /dev/null -w "%{http_code}" "$1"
