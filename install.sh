#!/usr/bin/env bash

# Bus Pirate scripts installer

set -e

BIN_DIR="$HOME/bin"

pip3 install --no-cache-dir --user --progress-bar emoji -r requirements.txt
mkdir -p "$BIN_DIR"
cp -vf bp_transparent_bridge.py "$BIN_DIR"
chmod a+x "$BIN_DIR"/bp_transparent_bridge.py

printf "Script installed.\nAdd %s to your PATH" "$BIN_DIR"
