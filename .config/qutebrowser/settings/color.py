# my color
mono0   = '#282c34'  # black
mono1   = '#545862'  # Gray
mono2   = '#abb2bf'  # Silver
mono3   = '#c8ccd4'  # white
mono4   = '#353b45'
red0    = '#e06c75'
green0  = '#98c379'
yellow0 = '#e5c07b'
blue0   = '#61afef'
purple0 = '#c678dd'
teal0   = '#56b6c2'

## Background color of the completion widget category headers.
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:0, stop:0 #282c34, stop:1 #282c34)'
## Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = mono0
## Top border color of the completion widget category headers.
c.colors.completion.category.border.top = mono0
## Foreground color of completion widget category headers.
c.colors.completion.category.fg = mono3
## Text color of the completion widget. May be a single color to use for all columns or a list of three colors, one for each column.
c.colors.completion.fg = [mono3, mono3, mono3]
## Background color of the selected completion item.
c.colors.completion.item.selected.bg = green0
## Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = green0
## Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = green0
## Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = mono0
## Foreground color of the matched text in the completion.
c.colors.completion.match.fg = red0
## Background color of the completion widget for even rows.
c.colors.completion.even.bg = mono0
## Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = mono4
## Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = mono0
## Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = mono2

## Background color for the download bar.
c.colors.downloads.bar.bg = mono0
## Background color for downloads with errors.
c.colors.downloads.error.bg = red0
## Foreground color for downloads with errors.
c.colors.downloads.error.fg = mono0
## Color gradient start for download backgrounds.
c.colors.downloads.start.bg = blue0
## Color gradient start for download text.
c.colors.downloads.start.fg = mono0
## Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = green0
## Color gradient end for download text.
c.colors.downloads.stop.fg = mono0
## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'
## Color gradient interpolation system for download text.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
# c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'
## Font color for hints.
c.colors.hints.fg = mono0
## Font color for the matched part of hints.
c.colors.hints.match.fg = green0

## Background color of the keyhint widget.
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'
c.colors.keyhint.bg = mono0
## Text color for the keyhint widget.
c.colors.keyhint.fg = mono3
## Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = yellow0

## Background color of an error message.
c.colors.messages.error.bg = red0
## Border color of an error message.
c.colors.messages.error.border = red0
## Foreground color of an error message.
c.colors.messages.error.fg = mono0
## Background color of an info message.
c.colors.messages.info.bg = mono0
## Border color of an info message.
c.colors.messages.info.border = mono0
## Foreground color of an info message.
c.colors.messages.info.fg = mono3
## Background color of a warning message.
c.colors.messages.warning.bg = yellow0
## Border color of a warning message.
c.colors.messages.warning.border = yellow0
## Foreground color of a warning message.
c.colors.messages.warning.fg = mono0

## Background color for prompts.
c.colors.prompts.bg = mono0
## Border used around UI elements in prompts.
## Type: String
# c.colors.prompts.border = '1px solid gray'
## Foreground color for prompts.
c.colors.prompts.fg = mono3
## Background color for the selected item in filename prompts.
# c.colors.prompts.selected.bg = 'grey'

## Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = purple0
## Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = mono0
## Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = purple0
## Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = mono0
## Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = mono0
## Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = mono2
## Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = mono0
## Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = mono2
## Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = blue0
## Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = mono0
## Background color of the statusbar.
c.colors.statusbar.normal.bg = mono0
## Foreground color of the statusbar.
c.colors.statusbar.normal.fg = mono2
## Background color of the statusbar in passthrough mode.
# c.colors.statusbar.passthrough.bg = 'darkblue'
## Foreground color of the statusbar in passthrough mode.
# c.colors.statusbar.passthrough.fg = 'white'
## Background color of the statusbar in private browsing mode.
# c.colors.statusbar.private.bg = '#666666'
## Foreground color of the statusbar in private browsing mode.
# c.colors.statusbar.private.fg = 'white'
## Background color of the progress bar.
c.colors.statusbar.progress.bg = mono2

## Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = red0
## Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = mono2
## Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = mono2
## Foreground color of the URL in the statusbar on successful load (http).
c.colors.statusbar.url.success.http.fg = mono2
## Foreground color of the URL in the statusbar on successful load (https).
c.colors.statusbar.url.success.https.fg = mono2
## Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = yellow0

## Background color of the tab bar.
c.colors.tabs.bar.bg = mono0
## Color for the tab indicator on errors.
c.colors.tabs.indicator.error = red0
## Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = yellow0
## Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = green0
## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'
## Background color of unselected even tabs.
c.colors.tabs.even.bg = mono0
## Foreground color of unselected even tabs.
c.colors.tabs.even.fg = mono2
## Background color of unselected odd tabs.
c.colors.tabs.odd.bg = mono0
## Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = mono2
## Background color of selected even tabs.
c.colors.tabs.selected.even.bg = green0
## Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = mono0
## Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = green0
## Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = mono0

## Background color for webpages if unset (or empty to use the theme's color).
# c.colors.webpage.bg = 'white'
