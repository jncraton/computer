Computer
========

![Star Trek LCARS Interface](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lcars_wallpaper.gif/640px-Lcars_wallpaper.gif)

This package implements the basic structure for a natural language intent parser. It is currently missing the implementation for an intent to calculate the effective bandwidth of a piece of storage media transported from one location to another.

This software expects a Unix-like environment with Python 3 and make available, but other environment should work as well.

Tests for this program can be executed as:

`make test` or simply `make`

The program can be invoked from the command line as follows:

    > ./computer what is 2 plus 2?
    4