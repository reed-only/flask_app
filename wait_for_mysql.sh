#!/bin/bash
#
# Wait for MySQL to finish loading before starting API server

wait 1
until mysql flask_app -se "select 'MySQL server is ready'"; do
    echo "Waiting for MySQL to load"
    sleep 1
done
