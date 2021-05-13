Bus Pirate scripts
==================

Requirements
------------

- Linux or macOS
- Python 3
- [Bus Pirate](http://dangerousprototypes.com/docs/Bus_Pirate) with FW v2.3+

Scripts installation
--------------------

> **WARNING:** Installation script will install Python libs to the user install directory for your platform. Typically `~/.local/`, or `$HOME/Library/Python/<major_ver.minor_ver>/lib/python/site-packages` on macOS. (See the Python documentation for `site.USER_BASE` for full details.)

Run `./install.sh` to install scripts to the `$HOME/bin`, this dir should be added to the `PATH`

Usage
-----

See help for the specific script. Example:
```bash
bp_transparent_bridge.py --help
```

If there is no help available then check inline comments inside the specific script
