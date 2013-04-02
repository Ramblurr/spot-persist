SPOT Persist
============

Tools to fetch and parse the feeds from a [SPOT GPS Messenger][spot] and
save them in a SQL database.

There are two utilites in this package:

1. `spot-fetch`   - A tool to download SPOT data feeds with their various options
2. `spot-persist` - Parses a JSON data feed and saves it to a SQLite database

## Usage

### spot-fetch

```
$ spot-fetch -h
usage: spot-fetch [-h] [-t {message,latest}] [-f {json,xml}] [-p]
                     [-P NO_PROMPT_PASSWORD]
                     glid

Utility for fetching SPOT message feeds

positional arguments:
  glid                  The feed id (glid) see http://faq.findmespot.com/index
                        .php?action=showEntry&data=69

optional arguments:
  -h, --help            show this help message and exit
  -t {message,latest}, --type {message,latest}
                        The type of feed to fetch (default: message)
  -f {json,xml}, --format {json,xml}
                        The desired output format (default: json)
  -p, --password        Prompts for the feed's password interactively
  -P NO_PROMPT_PASSWORD, --no-prompt-password NO_PROMPT_PASSWORD
                        The feed's password read from the arguments
```

### spot-persist
```
$ spot-persist -h
usage: spot-persist [-h] [-n DATABASE_NAME] [-u] [file]

Utility for parsing SPOT feeds in JSON format and saving them to a SQL
database

positional arguments:
  file                  The json data to parse

optional arguments:
  -h, --help            show this help message and exit
  -n DATABASE_NAME, --database-name DATABASE_NAME
                        The filename of the SQLite database (default:
                        messages.db)
  -u, --update          Insert new messages and update existing ones
```

## Examples

**Download JSON data from a feed**

    $ spot-fetch 0ATnNuieqRyM7RYsOFdaHoTNOtoFy9Xq4 > data.json

**Save this data to a SQLite database**

    $ spot-persist < data.json

**Cron job to download data and update the DB every 15 minutes **

    */5 * * * * spot-fetch 0ATnNuieqRyM7RYsOFdaHoTNOtoFy9Xq4 | spot-persist -u -n /some/dir/messages.db

## License

These tools are licensed under the GPLv3.

## Contributions

Bug reports, suggestions, and patches are welcome! Please use the github issue
tracker.

[spot]: http://www.findmespot.com/
