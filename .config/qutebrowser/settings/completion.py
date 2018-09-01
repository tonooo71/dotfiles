## Number of commands to save in the command history. 0: no history / -1: unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

## Delay (in milliseconds) before updating completions after typing a character.
## Type: Int
# c.completion.delay = 0

## Height (in pixels or as percentage of the window) of the completion.
c.completion.height = '50%'

## Minimum amount of characters needed to update completions.
## Type: Int
# c.completion.min_chars = 1

## Move on to the next part when there's only one possible completion left.
c.completion.quick = True

## Padding (in pixels) of the scrollbar handle in the completion window.
c.completion.scrollbar.padding = 2

## Width (in pixels) of the scrollbar in the completion window.
c.completion.scrollbar.width = 10

## When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
# c.completion.show = 'always'

## Shrink the completion to be smaller than the configured size if there are no scrollbars.
## Type: Bool
# c.completion.shrink = False

## Format of timestamps (e.g. for the history completion).
c.completion.timestamp_format = '%Y-%m-%d'

## Execute the best-matching command on a partial match.
# c.completion.use_best_match = False

## Number of URLs to show in the web history. 0: no history / -1: unlimited
## Type: Int
# c.completion.web_history_max_items = -1
