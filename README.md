# alfred-github-gist
[Alfred 3][1] workflow for opening your GitHub Gists in your default browser.

# Installation
1) Install [alfred-github-gists][2] workflow.
2) All further updates are handled automatically.

## Usage
In Alfred, type `gists`. This initiate a gists retrieval process, which shows all your public and private GitHub Gists.
Then, you could preview a selected Gist content by pressing <kbd>⌘</kbd>+<kbd>y</kbd>, or open a selected Gist by pressing <kbd>enter</kbd>.

![alfred-github-gist-menu](doc/images/alfred-gist-menu.png?raw=true "")

![alfred-github-gist-submenu](doc/images/alfred-gist-submenu.png?raw=true "")


## Configuration
Before the first usage, you are required to fill the workflow variables.

- `user` is your Github username,
- `personalToken` is your Github Personal Token created in your [user settings][3]. If you want to show your private gists, not just the public ones, select the `gist scope` during the personal token generation.

[1]: https://www.alfredapp.com/
[2]: https://github.com/vookimedlo/alfred-github-gists/releases/latest
[3]: https://github.com/settings/tokens
