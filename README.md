# Shell History Analyzer
[![Build Status](https://travis-ci.org/codequokka/shell-history-analyzer.svg?branch=master)](https://travis-ci.org/codequokka/shell-history-analyzer)

Get insights from your command history with dockernized ELK stask.
![dashboard](/docs/images/dashboard.png)

- [WARNINGS](#warnings)
- [Requirements](#requirements)
- [How to start](#how-to-start)
- [How to stop](#how-to-stop)
- [Features](#features)
- [Future works (TODO)](#future-works-todo)
- [Another data source](#another-data-source)

## WARNINGS

- This software is currently POC status.
  - Specifications are subject to change.

- Only minimal features are currently supported.
  - I am new at ELK stack now.
  - History files don't contain enough information to analyze.
    [Another data source](#another-data-source)

## Requirements

1. Install ___docker___, ___docker-compose___ on your computer.
  - Ubuntu
    - I'm sure that the linux guys know how to install docker.
    - I tested against ubuntu 16.04 only,
      but it should work on current linux distributions.
  - macOS
```
brew cask install docker
```

2. Setup data souce(currently support ___zsh___ only)
  - Zsh history file
    - Add settings to your .zshrc.
```
# Set the location of history file to track by logstash
export HISTFILE=~/.zsh_history

# Extend the number of history appended to $HISTFILE to analyze
export SAVEHIST=1000000

# Extend history format to retrieve beginning time
# as datetime when command executed
# : <beginning time>:<elapsed seconds>;<command>
setopt extended_history

# Write out the command history immediately to update kibana dashboard soon
setopt share_history
```

  - [b4b4r07/zsh-history](https://github.com/b4b4r07/zsh-history)
    - Add settings to your .zshrc.
```
# Set the location of zsh-history db to track by logstash
export ZSH_HISTORY_FILE="$HOME/.zsh_history.db"
```

3. Set your timezone
  - Add timzone settings to your .zshrc.
```
# Change containers timezone to convert command execution datetime
# to UTC properly
# Change the value according to your timezone
export TZ='Asia/Tokyo'
```

## How to start

1. Clone this repo in your computer then cd into repo.
```
$ git clone https://github.com/codequokka/shell-history-analyzer
$ cd shell-history-analyzer
```

2. Boot dockernized ELK stack.
```
$ docker-compose up -d
```

3. Go into [kibana](http://127.0.0.1:5601) and emjoy it!
    - If you access kibana too soon, you will encounter some errors on kibana.
    - In that case, wait a few minutes until your shell histories are sent to kibana.

## How to stop

Stop ELK stack.
```
$ docker-compose stop
```

If you boot again, history entries added after stopping ELK
are also displayed in kibana dashboard.
```
$ docker-compose start
```

## Features

- Display count of executed commands
- Update dashoboard continously when your shell history added

## Future works (TODO)

- Another data source support
- Display command options in dashboard
- Fish shell support

## Another data source

- Shell history files are designed for reusing them in command line.
  - They does not log your accurate command execution.
  - They does not log context informaton(Ex. pwd, hostname, etc).

- Another data sources are required to analyze more.
  - I examine following data source and support future release.
    - [larkery/zsh-histdb](https://github.com/larkery/zsh-histdb)
    - [b4b4r07/zsh-history](https://github.com/b4b4r07/zsh-history)
    - [b4b4r07/history](https://github.com/b4b4r07/history)

## Author

[Nobuchika Tanaka](https://github.com/codequokka)
