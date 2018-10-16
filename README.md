# DeclareThatColor
DeclareThatColor is a Sublime Text 3 plugin that searches and declares hex color codes to their equivalent friendly color names based on [http://chir.ag/projects/name-that-color/](http://chir.ag/projects/name-that-color/).

![Demo of latest usage](https://raw.githubusercontent.com/bertdida/DeclareThatColor/master/img/preview.gif)

## Installation
_You may need to restart Sublime Text for the plugin to load properly._
1. Download and extract DeclareThatColor [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (`Sublime Text` -> `Preferences` -> `Browse Packages...`).
2. Rename the extracted folder from `DeclareThatColor-master` to `DeclareThatColor`.

## Usage
From the main application menu navigate to `Edit` -> `Declare That Color`, or use the pre-defined keyboard shortcut `Super` + `Ctrl` + `.`.

## Settings
**variable_prefix**\
Type: _String_\
Default: `''` (empty string)\
Currently this option supports `$`, `@` and `''` values. If default value is set, variables will be declared using vanilla CSS notation.

**declare_alphabetically**\
Type: _Bollean_\
Default: `false`\
Whether or not declare variables alphabetically.

## Author
Herbert Verdida - [@bertdida](https://twitter.com/bertdida)

## Acknowledgments
1. Chirag Mehta - inspiration and the creator of [name-that-color](http://chir.ag/projects/name-that-color/#6195ED) tool.
2. [Matt Fordham](https://github.com/mattfordham/Name-That-Color---Sublime-Plugin) - ported [ntc.js](http://chir.ag/projects/ntc/ntc.js)
