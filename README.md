# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin that aims to help developers declare CSS hex codes to their human-readable color names.

![preview](img/preview.gif)

## Behaviors

- This plugin will look for 3 and 6-digit hex codes (case insensitive) and will convert them to their 6-digit lowercase notation.
- Multiple hex codes may have the same color name; for example #FFF, #FEFEFE and #FDFDFD yields the name white. If these hex codes are used sequentially, color names `white`, `white-2` and `white-3` will be given respectively.
- When using the stylus preprocessor, a declaration will be prepended with the dollar sign and will have the trailing semicolon.
- Variable names will be ordered using the [natural sort](https://en.wikipedia.org/wiki/Natural_sort_order) algorithm.

## Installation

### Package Control

1. To search for a plugin, click on Preferences > Package Control > Package Control: Install Package.
2. Type DeclareThatColor and press <kbd>Enter</kbd>.

### Manual installation

1. Download and extract the plugin’s [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (Sublime Text > Preferences > Browse Packages...).
2. Rename the extracted folder from DeclareThatColor-master to DeclareThatColor.

### Using Git

1. Open a terminal and `cd` to your Sublime Text Packages directory.
2. Clone the repository by running `git clone https://github.com/bertdida/DeclareThatColor.git`.

## Usage

From the Sublime Text's main menu click on Edit > Declare/Undeclare That Color.

### Key bindings

DeclareThatColor doesn't provide default key bindings, but you can use the template below to set up your own. To add key bindings click on Preferences > Key Bindings.

```json
[
  { "keys": ["Your shortcut"], "command": "declare_that_color" },
  { "keys": ["Your shortcut"], "command": "undeclare_that_color" }
]
```

## Settings

See the default settings by navigating to Preferences > Package Settings > DeclareThatColor > Settings - Default. To avoid your changes from being overwritten by updates, use the Settings - User.

Note, a restart on Sublime Text is required to load the changes effectively.

### `css_selector`

A string that specifies the CSS selector to use on vanilla CSS declaration, this setting defaults to `:root`.

### `css_preprocessor`

_Nullable_. Can be a string that defines the [CSS preprocessor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_preprocessor) language to use. By default, this is set to null which indicates to use the vanilla CSS declaration. Expected value is any of the following:

- `null`
- [`scss`](https://sass-lang.com/)
- [`sass`](https://sass-lang.com/)
- [`less`](http://lesscss.org/)
- [`stylus`](http://stylus-lang.com/)

### `color_name_prefix`

_Nullable_. Can be a string that sets a prefix for each color names, default value is set to `null`.

## Source

[GitHub](https://github.com/bertdida/DeclareThatColor)

## Contribute

If you have any problem, idea or suggestion, feel free to create issues and pull requests on [GitHub](https://github.com/bertdida/DeclareThatColor).

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

## Thanks

This plugin was inspired by Chirag Mehta's [Name That Color](http://chir.ag/projects/name-that-color/) tool, much thanks to him for open sourcing his [JavaScript code](http://chir.ag/projects/ntc/ntc.js).
