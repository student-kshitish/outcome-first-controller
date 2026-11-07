#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: ./run.sh <SIM_URL>"
    exit 1
fi

export SIMULATOR_URL="$1"

if [[ -z "${SIMULATOR_URL}" ]]; then
    echo "Error: simulator URL cannot be empty."
    exit 1
fi

if [[ ! -x ".venv/bin/python" ]]; then
    echo "Error: virtual environment not found."
    echo "Run: python3.12 -m venv .venv"
    exit 1
fi

export PYTHONPATH="src${PYTHONPATH:+:$PYTHONPATH}"

exec .venv/bin/python -m controller.main
