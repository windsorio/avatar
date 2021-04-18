#!/bin/sh

set -euo pipefail

rm -rf api/robohash
cd robohash-src
python3 setup.py build
cd ..
mv robohash-src/build/lib/robohash api
rm -r robohash-src/build
