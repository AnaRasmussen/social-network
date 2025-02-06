#!bin/sh

set -e

rm - r social.db
sqlite3 social.db < schema.sqlite3
python3 build.py