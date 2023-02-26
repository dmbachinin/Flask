#!/bin/bash
port=5000
fuser -k $port/tcp
flask run