# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin for CSS that declares hex color codes to their comparable friendly color names.

## Installation

1. Download and extract the DeclareThatColor [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (Sublime Text > Preferences > Browse Packages...).
2. Rename the extracted folder from DeclareThatColor-master to DeclareThatColor.

## Usage

From the main application click Edit > Declare That Color.

## Settings

| Name             | Type   | Default | Description                                                                                                                                                            |
| ---------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| css_selector     | string | :root   | Specifies what selector to be used for vanilla CSS declaration. This setting only applies if `css_preprocessor` is set to `null`.                                      |
| css_preprocessor | string | none    | Specifies what CSS preprocessor to be used. If the value is not set on one of the following `sass`, `scss`, `less` or `stylus` then vanilla CSS notation will be used. |

## Author

Herbert Verdida - [@bertdida](https://twitter.com/bertdida)

## Thanks

This plugin was inspired by Chirag Mehta's [Name That Color](http://chir.ag/projects/name-that-color/) tool. I found myself always using his tool while doing my [#100DaysOfCSSIllustrations](https://codepen.io/collection/XPmjEL/) challenge and decided to have it accessible on my text editor. Much thanks to him for open sourcing his JavaScript code.
