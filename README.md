# DeclareThatColor

DeclareThatColor is a Sublime Text 3 plugin that aims to help developers declare CSS hex codes to their human-readable color names (based on Chirag Mehta's [name that color](http://chir.ag/projects/name-that-color/) tool).

[![Maintainability](https://api.codeclimate.com/v1/badges/dd17b74cb4a19b100fdb/maintainability)](https://codeclimate.com/github/bertdida/DeclareThatColor/maintainability) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/bertdida/DeclareThatColor.svg) ![GitHub](https://img.shields.io/github/license/bertdida/DeclareThatColor.svg)

![preview](img/preview.gif)

## Installation

Download [Package Control](https://packagecontrol.io/) and use the _Package Control: Install Package_ command from the command palette. In this way, DeclareThatColor will stay up to date automatically.

## Usage

- To declare hex codes, click on **Edit** → **Declare That Color**
- To revert declarations, click on **Edit** → **Undeclare That Color**

### Key bindings

DeclareThatColor doesn't ship with default key bindings, but you can use the template below to set up your own.

```json
[
  { "keys": ["Your shortcut"], "command": "declare_that_color" },
  { "keys": ["Your shortcut"], "command": "undeclare_that_color" }
]
```

## Settings

For a comprehensive list of settings navigate to **Preferences** → **Package Settings** → **DeclareThatColor** → **Settings - Default** or visit [DeclareThatColor/declare_that_color.sublime-settings](https://github.com/bertdida/DeclareThatColor/blob/master/declare_that_color.sublime-settings).

To avoid your changes from being overwritten by updates, make sure all edits are saved to **Settings – User**.

## Source

[GitHub](https://github.com/bertdida/DeclareThatColor)

## Contribute

If you have any problem, idea or suggestion, feel free to create issues and pull requests on [GitHub](https://github.com/bertdida/DeclareThatColor).

## License

Distributed under the MIT license. See LICENSE for more information.

## Author

Herbert Verdida / [@bertdida](https://twitter.com/bertdida)

## Credits

This work was inspired by Chirag Mehta's [name that color](http://chir.ag/projects/name-that-color/) tool, much thanks to him for open sourcing his [JavaScript code](http://chir.ag/projects/ntc/ntc.js)!
