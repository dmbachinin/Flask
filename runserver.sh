#!/bin/bash
port=5000
fuser -k $port/tcp
python blog/wsgi.py