# alfred-github-gist
[Alfred 4][1] workflow for opening your GitHub Gists in your default browser.

# Installation
1) Install [alfred-github-gists][2] workflow.
2) All further updates are handled automatically.
3) Requires a _python3_ interpreter to be installed via a [Homebrew][4].

## Usage
In Alfred, type `gists`. This initiate a gists retrieval process, which shows all your public and private GitHub Gists.
Then, you could preview a selected Gist content by pressing <kbd>⌘</kbd>+<kbd>y</kbd>, or open a selected Gist by pressing <kbd>enter</kbd>.

![alfred-github-gist-menu](doc/images/alfred-gist-menu.png?raw=true "")

![alfred-github-gist-submenu](doc/images/alfred-gist-submenu.png?raw=true "")


## Configuration
Before the first usage, you are required to fill the workflow variables.

- `user` is your Github username,
- `personalToken` is your Github Personal Token created in your [user settings][3]. If you want to show your private gists, not just the public ones, select the `gist scope` during the personal token generation.

Optionally, the following workflow variables could be set.

- `keyword` contains the main workflow keyword, which is used to start this workflow. By default, it's set to `gists`.

[1]: https://www.alfredapp.com/
[2]: https://github.com/vookimedlo/alfred-github-gists/releases/latest
[3]: https://github.com/settings/tokens
[4]: https://brew.sh/
