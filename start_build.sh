#!/bin/bash

set -x
set -e

pnpm build
python manage.py collectstatic