#!/bin/sh

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# exits if any of your variables is not set
set -o nounset

# alembic revision --autogenerate -m "Add new column to table"
alembic upgrade head
exec gunicorn -w "$NO_API_WORKERS" -k uvicorn.workers.UvicornWorker --timeout "$API_WORKERS_TIMEOUT" main:app --bind "$HOST:$API_PORT" --access-logfile /home/non-root/app/src/log/gunicorn_access.log --error-logfile /home/non-root/app/src/log/gunicorn_error.log
