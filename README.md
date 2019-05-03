## Simple Path Optimization extension for Inkscape

### Description

A simple extension for [Inkscape](https://inkscape.org/) that optimizes
the paths of the selected objects. Useful for pixel art that has been
converted to scalable vector graphics (SVG).

The script calls the following menu functions on the selected objects
in this order:
- Path 🡆 Combine
- Path 🡆 Union
- Path 🡆 Simplify
- Path 🡆 Break Apart

### Installation

Add the ***simple_path_optimize.py*** & ***simple_path_optimize.inx*** files to Inkscape's extensions directory.

- Windows:
  - System: **<install_dir>\share\extensions**
  - Local user: **%UserProfile%\AppData\Roaming\inkscape\extensions**
- Unix/Linux:
  - System: **/usr/share/inkscape/extensions**
  - Local user: **~/.config/inkscape/extensions**

### Usage

Simply execute the menu option `Extensions 🡆 Modify Path 🡆 Simple Path Optimize`.

### Licensing

This work is released under [Creative Commons Zero (CC0)](LICENSE.txt).

The author hereby waives all copyright and related or
neighboring rights together with all associated claims
and causes of action with respect to this work to the
extent possible under the law.

See: https://creativecommons.org/publicdomain/zero/1.0/legalcode
