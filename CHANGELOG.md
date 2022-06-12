# Changelog

*All dates are in ISO-8601 formatting (YYYY-MM-DD).*

## Table of Contents

- Releases
    + [1.0 pre-alpha](#2017-10-03-pre-alpha-release)
    + [1.0 alpha](#2018-11-13-alpha-release)
- Overhauls
    + [OH1](#2019-01-29-code-overhaul)
    + [OH2](#2019-11-20-code-overhaul)
    + [OH3](#2020-11-09-code-overhaul)
    + [OH4](#2022-05-18-code-overhaul)
- Maintenance
    + [M1801](#2018-02-21-maintenance)
    + [M1802](#2018-04-07-maintenance)
    + [M1901](#2019-06-18-maintenance)
    + [M2001](#2020-12-30-maintenance)
    + [M2101](#2021-02-10-maintenance)
- Updates
    + [18AUG28](#2018-08-28-new-branch)

### 2022-05-18: Code Overhaul

- Update project layout.
- Changed license from "WTFPL" to "0BSD".
- Added [contributor](CONTRIBUTING.md) file.
- Added [changelog](CHANGELOG.md) file.
- Removed "SimpleRequests" module.
- Added three new submodules.
    + dsapi: Submodule for linking Discord API endpoints.
    + dsdb: Submodule for linking local SQLite3 databases.
    + dsmain: Submodule for linking scraper functionality.

### 2021-02-10: Maintenance

- Fixed pagination issue.
- Added media scraping.
- Added keyboard halt command.
    + <kbd>CTRL</kbd> <kbd>C</kbd>

### 2020-12-30: Maintenance

- Added JSON caching.
- Added function for retrieving most recent post in a channel.

### 2020-11-09: Code Overhaul

- Merged "experimental" branch into main.
- Modified main branch name.
- Added Python 2 and 3 compatibility to "SimpleRequests".
- Updated API version.
- Updated [wiki.](https://github.com/Dracovian/wiki)
- Removed PEP8 compliance.

### 2019-11-20: Code Overhaul

- Added "experimental" branch.
- Added "SimpleRequests" module.
- Added buffer size option in configuration.
- Merged "experimental" branch into main.

### 2019-06-18: Maintenance

- Added direct message channel scraping.
- Removed page count from configuration.
- Updated the [wiki.](https://github.com/Dracovian/wiki)
- Modified the [readme.](README.md)
    + Updated token gathering method.
    + Removed excess image use.

### 2019-01-29: Code Overhaul

- Merged Python 2 and 3 support.
- Merged "experimental" branch into main.
- Added configuration options.
    + Text data caching
    + Link caching
    + Page count

### 2018-11-13: Alpha Release

- Added concept from "experimental" branch into main.
- Updated "experimental" branch to match main.
- TODO: Solve duplicate file issue.
- TODO: Improve code comments.

### 2018-08-28: New Branch

- Added a separate config for Python 3.
- Added new branch named "experimental".
- Replaced use of "requests" module with a native module.
- Fixed? potential authorization token leakage.
    + TODO: Improve security of token storage.

### 2018-04-07: Maintenance

- Fixed? pagination issue.
- TODO: Improve file name generation.
- Fixed threading issue.
- Fixed file name generation.

### 2018-02-21: Maintenance

- Added warning to [readme.](README.md)
- Added Python 3 compatibility.
- Added threading support.

### 2017-10-03: Pre-Alpha Release

- Fixed URI query issue.
- Fixed multi-page opener issue.
- Added function for resetting opener.