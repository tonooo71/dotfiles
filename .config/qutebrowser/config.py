## Autogenerated config.py
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

# Load color setting
config.source('settings/color.py')
# Load completion setting
config.source('settings/completion.py')
# Load content setting
config.source('settings/content.py')
# Load downloads setting
config.source('settings/downloads.py')
# Load fonts setting
config.source('settings/fonts.py')
# Load hint setting
config.source('settings/hints.py')
# Load input setting
config.source('settings/input.py')
# Load tab setting
config.source('settings/tab.py')
# Load binding setting
config.source('settings/binding.py')

## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
# config.load_autoconfig()

## Aliases for commands. The keys of the given dictionary are the aliases, while the values are the commands they map to.
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save',
             'pass': 'spawn --userscript qute-lastpass',
             'pocket': 'spawn --userscript scripts.sh pocket {url}',
             'ejdict': 'spawn --userscript scripts.sh ejdict'}

## Time interval (in milliseconds) between auto-saves of config/cookies/etc.
c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened.
c.auto_save.session = False

## This setting can be used to map keys to other keys. When the key used as dictionary-key is pressed, the binding for the key used as dictionary-value is invoked instead. This is useful for global remappings of keys, for example to map Ctrl-[ to Escape. Note that when a key is bound (via `bindings.default` or `bindings.commands`), the mapping is ignored.
c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

## Require a confirmation before quitting the application.
## Valid values: always,multiple-tabs,downloads,never
c.confirm_quit = ['downloads']

## Editor (and arguments) to use for the `open-editor` command. The following placeholders are defined: * `{file}`: Filename of the file to be edited. * `{line}`: Line in which the caret is found in the text. * `{column}`: Column in which the caret is found in the text. * `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`: Same as `{column}`, but starting from index 0.
## Type: ShellCommand
c.editor.command = ['nvim', '{file}', '-c', 'normal {line}G{column0}l']

## Encoding to use for the editor.
c.editor.encoding = 'utf-8'

## Maximum minutes between two history items for them to be considered being from the same browsing session. Items with less time between them are grouped in `:history`. Use -1 to disable separation.
c.history_gap_interval = 60

## Keychains that shouldn't be shown in the keyhint dialog. Globs are supported, so `;*` will blacklist all keychains starting with `;`. Use `*` to disable keyhints.
## Type: List of String
c.keyhint.blacklist = []

## Time (in milliseconds) from pressing a key to seeing the keyhint dialog.
c.keyhint.delay = 500

## Rounding radius (in pixels) for the edges of the keyhint dialog.
c.keyhint.radius = 10

## Duration (in milliseconds) to show messages in the statusbar for. Set to 0 to never clear messages.
c.messages.timeout = 5000

## How to open links in an existing instance if a new one is launched.
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
# c.new_instance_open_target = 'tab'

## Which window to choose when opening links as new tabs. When `new_instance_open_target` is not set to `window`, this is ignored.
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

## Show a filebrowser in upload/download prompts.
c.prompt.filebrowser = False

## Rounding radius (in pixels) for the edges of prompts.
c.prompt.radius = 10

## Additional arguments to pass to Qt, without leading `--`. With QtWebEngine, some Chromium arguments (see https://peter.sh/experiments/chromium-command-line-switches/ for a list) will work.
## Type: List of String
# c.qt.args = []

## Force a Qt platform to use. This sets the `QT_QPA_PLATFORM` environment variable and is useful to force using the XCB plugin when running QtWebEngine on Wayland.
## Type: String
# c.qt.force_platform = None

## Force software rendering for QtWebEngine. This is needed for QtWebEngine to work with Nouveau drivers and can be useful in other scenarios related to graphic issues.
## Type: String
## Valid values:
##   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
##   - none: Don't force software rendering.
# c.qt.force_software_rendering = 'none'

## Turn on Qt HighDPI scaling. This is equivalent to setting QT_AUTO_SCREEN_SCALE_FACTOR=1 in the environment. It's off by default as it can cause issues with some bitmap fonts. As an alternative to this, it's possible to set font sizes and the `zoom.default` setting.
# c.qt.highdpi = False

## Show a scrollbar.
c.scrolling.bar = True

## Enable smooth scrolling for web pages. Note smooth scrolling does not work with the `:scroll-px` command.
c.scrolling.smooth = False

## When to find text on a page case-insensitively.
## Type: String
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
# c.search.ignore_case = 'smart'

## Find text on a page incrementally, renewing the search for each typed character.
c.search.incremental = True

## Name of the session to save by default. If this is set to null, the session which was last loaded is saved.
## Type: SessionName
# c.session.default_name = None

## Load a restored tab as soon as it takes focus.
# c.session.lazy_restore = False

## Hide the statusbar unless a message is shown.
c.statusbar.hide = False

## Padding (in pixels) for the statusbar.
c.statusbar.padding = {'top': 4, 'bottom': 4, 'left': 4, 'right': 4}

## Position of the status bar. Valid values: top, bottom
c.statusbar.position = 'bottom'

## List of widgets displayed in the statusbar.
## Valid values:
##   - url: Current page URL.
##   - scroll: Percentage of the current page position like `10%`.
##   - scroll_raw: Raw percentage of the current page position like `10`.
##   - history: Display an arrow when possible to go back/forward in history.
##   - tabs: Current active tab, e.g. `2`.
##   - keypress: Display pressed keys when composing a vi command.
##   - progress: Progress bar for the current page loading.
c.statusbar.widgets = ['keypress', 'url', 'history', 'tabs', 'progress']

## What search to start when something else than a URL is entered.
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
# c.url.auto_search = 'naive'

## Page to open if :open -t/-b/-w is used without URL. Use `about:blank` for a blank page.
## Type: FuzzyUrl
c.url.default_page = 'https://www.google.com/'

## URL segments where `:navigate increment/decrement` will search for a number.
## Type: FlagList
## Valid values: host, port, path, query, anchor
# c.url.incdec_segments = ['path', 'query']

## Open base URL of the searchengine if a searchengine shortcut is invoked without parameters.
# c.url.open_base_url = False

## Search engines which can be used via the address bar. Maps a search engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}` placeholder. The placeholder will be replaced by the search term, use `{{` and `}}` for literal `{`/`}` signs. The search engine named `DEFAULT` is used when `url.auto_search` is turned on and something else than a URL was entered to be opened. Other search engines can be used by prepending the search engine name to the search term, e.g. `:open google qutebrowser`.
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}',
                       'i': 'https://www.google.com/search?q={}&tbm=isch',
                       'm': 'https://maps.google.com/maps?q={}',
                       'e': 'http://ejje.weblio.jp/content?query={}'}

## Page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ['https://www.google.com']

## URL parameters to strip with `:yank url`.
## Type: List of String
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

## Hide the window decoration.  This setting requires a restart on Wayland.
# c.window.hide_decoration = False

## Format to use for the window title. The same placeholders like for `tabs.title.format` are defined.
# c.window.title_format = '{perc}{title}{title_sep}qutebrowser'
c.window.title_format = 'qutebrowser'

## Default zoom level.
c.zoom.default = '100%'

## Available zoom levels.
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
c.zoom.levels = ['50%', '75%', '100%', '125%', '150%', '200%']

## Number of zoom increments to divide the mouse wheel movements to.
# c.zoom.mouse_divider = 512

## Apply the zoom factor on a frame only to the text or to all content.
# c.zoom.text_only = False
