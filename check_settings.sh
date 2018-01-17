#!/bin/bash

echo Run checks to be sure everything will work fine
./manage.py check --deploy --fail-level WARNING && echo ---- OK ---- || echo ---- FAILED ----

echo ----------------------
echo Run python specific scripts
./manage.py migrate --noinput && ./manage.py collectstatic --noinput && echo ---- OK ---- || echo ---- FAILED ----

echo ----------------------
echo Check that all migrations worked fine
./manage.py makemigrations --dry-run --check && echo ---- OK ---- || echo ---- FAILED ----
