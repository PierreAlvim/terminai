#!/bin/bash

# Ensure we are in the project directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INSTALL_DIR="$HOME/.local/share/terminai"
echo "Cleaning up local environment..."
rm -rf venv
mkdir -p "$INSTALL_DIR"

echo "Creating dedicated virtual environment..."
python3 -m venv "$INSTALL_DIR/venv"

echo "Installing Terminai python dependencies..."
"$INSTALL_DIR/venv/bin/python3" -m pip install -e .

echo "Setting up Fish shell integration..."
mkdir -p ~/.config/fish/functions
# Update Q? and q? to use the venv python
sed "s|python3 -m terminai.cli|$INSTALL_DIR/venv/bin/python3 -m terminai.cli|g" shell/q.fish > ~/.config/fish/functions/Q\?.fish
# Also create q?.fish as a symlink or separate file
cp ~/.config/fish/functions/Q\?.fish ~/.config/fish/functions/q\?.fish

echo "Done!"

echo "Please run 'Q? --setup' to configure your Gemini API key."

