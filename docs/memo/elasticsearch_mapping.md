# Elasticsearch mapping

## How to update index mapping

- Stop logstash container
```zsh
$ docker-compose kill logstash
```

- Remove sincedb file
```zsh
$ rm ~/.zsh_history_sincedb
```

- Delete index
```zsh
$ curl -X DELETE 'localhost:9200/zsh_history'
```

- Create index
```zsh
$ curl -H "Content-Type: application/json" -XPUT 'http://localhost:9200/zsh_history' -d @elasticsearch/mapping/zsh_history_mapping.json
```

- Restart logstash container
```zsh
$ docker-compose restart logstash
```
