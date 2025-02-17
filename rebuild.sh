#!/bin/sh

set -e

rm -r social.db
sqlite3 social.db < schema.sql
python3 populate_db.py