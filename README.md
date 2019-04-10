# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin that helps developers declare hex codes to their human-readable color names.

![preview](https://github.com/bertdida/DeclareThatColor/blob/master/img/preview.gif?raw=true)

## Notes

- This plugin recognizes 3 and 6-digits hex codes (case insensitive) and will convert them to their 6-digit lowercased representation.
- There are cases that 2 or more hex codes own the same color name. For example #FFF, #FEFEFE and #FDFDFD are using the name white. If these hex codes are used on the document in order from top to bottom, the following variable names will be used on declarations respectively: `white`, `white-2` and `white-3`.

## Installation

### Manual installation

1. Download and extract the plugin’s [zip file](https://github.com/bertdida/DeclareThatColor/archive/master.zip) to your Sublime Text Packages directory (Sublime Text > Preferences > Browse Packages...).
2. Rename the extracted folder from DeclareThatColor-master to DeclareThatColor.

### Using Git

1. Open the terminal and `cd` to you your Sublime Text Packages directory.
2. Clone the repository by running `git clone https://github.com/bertdida/DeclareThatColor.git`.

## Usage

Click on Edit > Declare That Color from the Sublime Text's main menu or click Undeclare That Color to undo the declarations.

### Key bindings

DeclareThatColor doesn't provide default key bindings, but you can use the template below to set up your own.

```json
[
  { "keys": ["Your shortcut"], "command": "declare_that_color" },
  { "keys": ["Your shortcut"], "command": "undeclare_that_color" }
]
```

## Settings

_Restart Sublime Text to load the changes properly._

To acces settings click Preferences > Package Settings > DeclareThatColor > Settings - User/Default.

| Name             | Default | Description                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| css_selector     | `:root` | A string that specifies the CSS selector to use on vanilla CSS declaration.                                                                                                                                                                                                                                                                             |
| css_preprocessor | `null`  | _Nullable._ A string that defines the CSS preprocessor language to use. Currently, the supported languages are the following (case insensitive): [`scss`](https://sass-lang.com/), [`sass`](https://sass-lang.com/), [`less`](http://lesscss.org/) and [`stylus`](http://stylus-lang.com/). To use the vanilla CSS declaration set its value to `null`. |

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
