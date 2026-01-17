#!/usr/bin/bash

echo "Running dependency check"
echo "(1/3) Checking for Python..."
if pacman -Qs python > /dev/null; then
    echo "Found Python"
else
    echo "Python not installed. Installing..."
    sudo pacman -S python
fi

echo "(2/3) Checking for ani-cli..."
if yay -Qs ani-cli >/dev/null; then
    echo "ani-cli is installed."
else
    echo "ani-cli not installed. Installing..."
    yay -S ani-cl
fi

echo "(3/3) Checking for NetworkManager..."
if pacman -Qs networkmanager >/dev/null; then
    echo "NetworkManager found."
else
    echo "NetworkManager not installed. Installing..."
    sudo pacman -S networkmanager
fi

echo "Dependency check complete!"
read -r -p "Would you like to update? [y/N] " -n 1 REPLY
echo

if [[ "$REPLY" =~ ^[Yy]$ ]]; then
    $REPLY = 0
    echo "Updating..."
    git clone "https://github.com/cpu-gpu-ram/py-man.git"
    cd py-man
    read -r -p "Would you like to run the script? [y/N] " -n 1 REPLY
    echo
    if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
        python main.py
    else
        echo "Closing installer. Goodbye!"
    fi
else
    echo "Operation cancelled. Goodbye!"
    exit 1 # Exit the script
fi

