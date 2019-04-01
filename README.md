# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin for CSS that declares hex color codes to their human-friendly color names.

![preview](https://github.com/bertdida/DeclareThatColor/blob/master/img/preview.gif?raw=true)

## Installation

1. Download and extract the DeclareThatColor [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (Sublime Text > Preferences > Browse Packages...).
2. Rename the extracted folder from DeclareThatColor-master to DeclareThatColor.

## Usage

To declare hex color codes click Edit > Declare That Color from the Sublime Text's main menu.

Or click Edit > Undeclare That Color to undo declarations.

### Key bindings

To avoid conflicts, DeclareThatColor doesn't come with default key bindings. You can use the template below to customize your own.

```json
[
  { "keys": ["Your shortcut"], "command": "declare_that_color" },
  { "keys": ["Your shortcut"], "command": "undeclare_that_color" }
]
```

## Settings

_\*Restart Sublime Text to load the changes properly._

To acces settings click Preferences > Package Settings > DeclareThatColor > Settings - User/Default.

| Name             | Default | Description                                                                                                                                                                                                                                                                                                                        |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| css_selector     | `:root` | Specifies the CSS selector for vanilla declaration.                                                                                                                                                                                                                                                                                |
| css_preprocessor | `null`  | Defines what CSS preprocessor language to be used. Currently, the supported languages are the following (case insensitive): [`scss`](https://sass-lang.com/), [`sass`](https://sass-lang.com/), [`less`](http://lesscss.org/) and [`stylus`](http://stylus-lang.com/). To use the vanilla CSS declaration set its value to `null`. |

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

## Thanks

DeclareThatColor was inspired by Chirag Mehta's [Name That Color](http://chir.ag/projects/name-that-color/) tool. Much thanks to him for open sourcing his JavaScript code.
