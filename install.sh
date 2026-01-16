#!/usr/bin/bash

echo "Running dependency check"
echo "(1/3) Checking for Python..."
if pacman -Qs python > /dev/null; then
    echo "Found Python"
else [[echo "Python not installed. Installing..."; sudo pacman -S python]]
fi

echo "(2/3) Checking for ani-cli..."
if yay -Qs ani-cli >/dev/null; then
    echo "ani-cli is installed."
else [[echo "ani-cli not installed. Installing..." ; yay -S ani-cli]]
fi

echo "(3/3) Checking for NetworkManager..."
if pacman -Qs networkmanager >/dev/null; then
    echo "NetworkManager found."
else [[echo "NetworkManager not installed. Installing..." ; sudo pacman -S networkmanager]]
fi

echo "Dependency check complete!"
