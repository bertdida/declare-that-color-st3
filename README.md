# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin that aims to help developers declare CSS hex codes to their human-readable color names based on Chirag Mehta's [name that color](http://chir.ag/projects/name-that-color/) tool.

[![Maintainability](https://api.codeclimate.com/v1/badges/dd17b74cb4a19b100fdb/maintainability)](https://codeclimate.com/github/bertdida/DeclareThatColor/maintainability) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/bertdida/DeclareThatColor.svg) ![GitHub](https://img.shields.io/github/license/bertdida/DeclareThatColor.svg)

![preview](img/preview.gif)

## Installation
### Package Control (recommended)
1. Open Command Palette by clicking on Tools → Command Palette...
2. Choose Package Control: Install Package
3. Type for DeclareThatColor and press <kbd>Enter</kbd>

### Manually
1. Download the [.zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) from Github
2. Extract the contents and rename the extracted folder to DeclareThatColor
3. Copy the folder into the Packages directory (Sublime Text → Preferences → Browse Packages...)

### Git
1. Open a terminal and `cd` to Packages directory
2. Clone the repository, `git clone https://github.com/bertdida/DeclareThatColor.git`

## Usage
From the Sublime Text's main menu click on Edit → Declare/Undeclare That Color.

### Key bindings

DeclareThatColor doesn't provide default key bindings, but you can use the template below to set up your own. To add key bindings click on Preferences → Key Bindings.

```json
[
  { "keys": ["Your shortcut"], "command": "declare_that_color" },
  { "keys": ["Your shortcut"], "command": "undeclare_that_color" }
]
```

## Settings
See the default settings by navigating to Preferences → Package Settings → DeclareThatColor → Settings - Default. To avoid your changes from being overwritten by updates, use the Settings - User.

### `css_selector`

A string that specifies the CSS selector to use on vanilla CSS declaration, this setting defaults to  `:root`.

### `css_preprocessor`

_Nullable_. This setting can be a string that will define the  [CSS preprocessor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_preprocessor)  language. By default, this is set to `null` which indicates to use the vanilla CSS declaration. Expected values are the following:

-   `null`
-   [`scss`](https://sass-lang.com/)
-   [`sass`](https://sass-lang.com/)
-   [`less`](http://lesscss.org/)
-   [`stylus`](http://stylus-lang.com/)

### `color_name_prefix`

_Nullable_. A string that will be prepended on each color names, its default value is `null`.

### `type_case`
If you have [Case Conversion](https://packagecontrol.io/packages/Case%20Conversion) plugin installed, use this setting to change the variable names case type. But whether you have or not the plugin installed, `dash` value will still work which is the default. Supported values are the following:

- `dash`
- `snake`
- `camel`
- `pascal`
- `screaming_snake`

## Source

[GitHub](https://github.com/bertdida/DeclareThatColor)

## [](https://github.com/bertdida/DeclareThatColor/blob/master/README.md#contribute)Contribute

If you have any problem, idea or suggestion, feel free to create issues and pull requests on  [GitHub](https://github.com/bertdida/DeclareThatColor).

## [](https://github.com/bertdida/DeclareThatColor/blob/master/README.md#license)License

Distributed under the MIT license. See LICENSE for more information.

## [](https://github.com/bertdida/DeclareThatColor/blob/master/README.md#author)Author

Herbert Verdida /  [@bertdida](https://twitter.com/bertdida)

## [](https://github.com/bertdida/DeclareThatColor/blob/master/README.md#thanks)Thanks

This plugin was inspired by Chirag Mehta's  [name that color](http://chir.ag/projects/name-that-color/)  tool, much thanks to him for open sourcing his  [JavaScript code](http://chir.ag/projects/ntc/ntc.js).
