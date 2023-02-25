#!/bin/bash
port=5000
fuser -k $port/tcp
python3 wsgi.py