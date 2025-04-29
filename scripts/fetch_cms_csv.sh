#!/usr/bin/env bash
set -euo pipefail

mkdir -p data/raw/cms

# Direct CSV endpoint for the Hospital PUF (monthly snapshot)
URL="https://data.cms.gov/resource/xubh-q36u.csv?\$limit=5000000"
OUT="data/raw/cms/hospital_puf.csv"

echo "Downloading PUF CSV from $URL …"
curl --ssl-no-revoke -G "$URL" -o "$OUT"
echo "Done → CSV stored at $OUT"
