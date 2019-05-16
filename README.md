# Shell History Analyzer

[![Build Status](https://travis-ci.org/codequokka/shell-history-analyzer.svg?branch=master)](https://travis-ci.org/codequokka/shell-history-analyzer)

Get insights from your command history with dockernized ELK stask.
![dashboard](/docs/images/dashboard.png)

- [WARNINGS](#warnings)
- [Requirements](#requirements)
- [How to start](#how-to-start)
- [How to stop](#how-to-stop)
- [How to reasume](#how-to-reasume)
- [How to upgrade](#how-to-upgrade)
- [Features](#features)
- [Future works (TODO)](#future-works-todo)
- [Another data source](#another-data-source)


## WARNINGS

- This software is currently POC status.
  - Specifications are subject to change.
  - But it doesn't mess your environment because of using docker.
    Please feel free to try!

- Only minimal features are currently supported.
  - I am new at ELK stack now.
  - History files don't contain enough information to analyze.
    [Another data source](#another-data-source)


## Requirements

1. Install ___docker___, ___docker-compose___ on your computer.
- Linux
  - I'm sure that the linux guys know how to install docker.
    So I won't explain how to install docker here.
  - I tested against ubuntu 16.04 only,
    but it should work on current linux distributions.
- macOS
```
brew cask install docker
```

2. Setup data souce(currently support ___zsh___ only)
- Zsh history file
  - Add minmal settings to your .zshrc.
  - Zsh history file does not log your command history precisely.
    So I ___strongly___ recommend you use another data source.
```
# Set the location of history file to track by logstash
# Currently it does not work with any other value
export HISTFILE="$HOME/.zsh_history"

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
  - Install b4b4r07/zsh-history
  - Add minimal settings to your .zshrc.
```
# Set the location of zsh-history db to track by logstash
# Currently it does not work with any other value
export ZSH_HISTORY_FILE="$HOME/.zsh_history.db"
```

- [larkery/zsh-histdb](https://github.com/larkery/zsh-histdb)
  - Install larkery/zsh-histdb

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


## How to reasume

Start ELK stack.
- If you start again, history entries added after stopping ELK
  are also displayed in kibana dashboard.
```
$ docker-compose start
```


## How to upgrade

1. Down ELK stack, remove their container images.
```
$ docker-compose down --rmi all
```

2. Update repo
```
$ git pull
```

3. Remove logstash files(keeps track of the current position of monitored log files)
- Be careful not to delete your data source file!
```
# For zsh history file data source
$ rm ~/.zsh_history_sincedb

# For b4b4r07/zsh-history data source
$ rm ~/.zsh_history.db_last_run

# For larkery/zsh-histdb data source
$ rm ~/.histdb/.zsh-history.db_last_run
```

4. Boot dockernized ELK stack again.
```
$ docker-compose up -d
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
