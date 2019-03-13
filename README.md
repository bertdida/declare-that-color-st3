# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin that searches and declares hex color codes to their equivalent friendly color names based on [http://chir.ag/projects/name-that-color/](http://chir.ag/projects/name-that-color/).

![Demo of latest usage](https://raw.githubusercontent.com/bertdida/DeclareThatColor/master/img/preview.gif)

## Installation

_You may need to restart Sublime Text for the plugin to load properly._

1. Download and extract DeclareThatColor [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (`Sublime Text` -> `Preferences` -> `Browse Packages...`).
2. Rename the extracted folder from `DeclareThatColor-master` to `DeclareThatColor`.

## Usage

From the main application menu navigate to `Edit` -> `Declare That Color`.

## Settings

**css_selector**\
Type: _string_\
Default: `':root'` (empty string)\
This option is only applicable if CSS preprocessor is not used.

**css_preprocessor**\
Type: _string_/_null_\
Default: `null`\
Beside from `null` this option supports `sass` or `scss`, `less` and `stylus`.

## Author

Herbert Verdida - [@bertdida](https://twitter.com/bertdida)

## Acknowledgments

- Chirag Mehta - the creator of [name-that-color](http://chir.ag/projects/name-that-color/#6195ED) tool.
