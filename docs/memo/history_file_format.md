# History file format

## Zsh

- default
```
# <command>
#     content of command line executed
<command>
ls -alt
```

- extended
```
# <beginning time>
#     command's beginning timestamp (in seconds since the epoch)
# <elapsed seconds>
#     the duration (in seconds)
# <command>
#     content of command line executed
: <beginning time>:<elapsed seconds>;<command>
: 1557101420:0;brew cask info google-japanese-ime
: 1557304257:0;while true;\
do\
sleep 2\
ls -l\
done
```
