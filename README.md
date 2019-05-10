# Shell History Analyzer

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

- This software is currenly alpha status.
  - Specifications are subject to change.

- Only minimal features are currently supported.
  - I am new at ELK stack now.
  - History files don't contain enough information to analyze.
    [Another data source](#another-data-source)

## Requirements

- Install ___docker___ on your computer.
  - macOS
```
brew cask install docker
```

- Add history settings to your shell(currently support ___zsh___ only).
```zsh:~/.zshrc
# Set the location of history file to track by logstash
export HISTFILE=~/.zsh_history

# Extend history format to retrieve beginning time as datetime when command executed
# : <beginning time>:<elapsed seconds>;<command>
setopt extended_history

# Write out the command history immediately to update kibana dashboard soon
setopt share_history
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