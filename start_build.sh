#!/bin/bash

set -x

pnpm build
python manage.py collectstatic