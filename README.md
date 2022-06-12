# Discord Scraper

## Table of Contents

- [Installation](#installation)
- [Credits](#credits)
- [Guides](#guides)
    + [Finding Your Token](#finding-your-token)
    + [Configuration](#configuration)
    + [Updating](#updating)
- [Resources](#additional-resources)
    + [Developer's Reference](#developers-reference)
    + [Background Information](#background-information)
- [Changelog](#changelog)

## Installation

<details>
    <summary>Windows Installation</summary>

1. [Download the latest version of Python](https://www.python.org/downloads/windows/)

2. Open a command line and run the command `py -m pip install -r requirements.txt`

</details>

## Credits

This section of the [readme](README.md) is dedicated to those who have contributed to this project, so that everyone knows that I'm truly grateful for those willing to contribute to this project that I've been intermittently working on since October 2017.

I personally want to thank...

[mukatee](https://github.com/mukatee) for their bugfix to an oversight on my behalf. The oversight in question was one where I had the script compare the current month to the month being scraped. Instead of ensuring that the year in question was also checked, my oversight prevented any scraping of data from previous years if their month exceeded the current month on the calendar. [[PR]](https://github.com/Dracovian/Discord-Scraper/pull/14)

[MRosenst](https://github.com/MRosenst) for their contribution towards replacing my previous use of the "time" module with the more feature-rich alternative "datetime" module. The most important feature in the "datetime" module is the "timedelta" function. This replaced my nested conditional statement for generating dates with a single conditional statement; that simply subtracted one day starting from the current date and ending at the first public release date of Discord. [[PR]](https://github.com/Dracovian/Discord-Scraper/pull/35)

[mataha](https://github.com/mataha) for their contribution to the ratelimit delay that I had implemented in the script as a temporary means to evade the Discord API rate limiter. The delay I had set wasn't adequate enough to prevent users from reaching, or exceeding the number of requests per second limitation set by the developers of Discord. [[PR]](https://github.com/Dracovian/Discord-Scraper/pull/56)

[cr2007](https://github.com/cr2007) for their contributions to the improvement of the [readme](README.md) file. I've been somewhat content with the overall state of this file since my last overhaul. There are many features to [Markdown](https://www.markdownguide.org/) that I'm not aware of and so there's always room for me to learn new things through the contributions of others, especially regarding the formatting and design behind these files. [[PR]](https://github.com/Dracovian/Discord-Scraper/pull/92)

[codekaust](https://github.com/codekaust) for their contribution towards a better way to mitigate an unwanted account suspension from continually sending requests while rate limited. The ratelimit delay method I had implemented didn't keep the script from sending requests; despite those requests inevitably returning [HTTP-429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) responses every time. The official API documentation from Discord includes information regarding the rate limiter, and the JSON response data that can be used to prevent hitting the rate limiter. [[PR]](https://github.com/Dracovian/Discord-Scraper/pull/69)

All of your contributions, no matter their significance, shows me that the sum of my efforts over the years weren't all in vain. For this I cannot express how much it means to me when you take the time from your day to lend a hand with a project. Especially one that's been steadily growing in complexity from [humble beginnings](https://github.com/Dracovian/Discord-Scraper/blob/764801e70ee28a295ce667506309d05018d028f2/Discord.py) to now.

## Guides

### Finding Your Token

### Configuration

### Updating


## Additional Resources

### Developer's Reference

### Background Information


## Changelog

The changelog has been moved [here](CHANGELOG.md) to avoid excessive updates to the README file.