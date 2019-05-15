# Update elasticsearch image

## How to update

- Up all containers
```zsh
$ docker-compose up
```

- Update all vistualizetion and dashboard
  - Get new index-patterns
```zsh
curl -H "Content-Type: application/json" -XGET 'http://localhost:9200/.kibana/_search?pretty' -d @elasticsearch/search/get-index-pattern.json
```

  - Get new visualization
```zsh
curl -H "Content-Type: application/json" -XGET 'http://localhost:9200/.kibana/_search?pretty' -d @elasticsearch/search/get-visualization.json
```

- Down all container
```zsh
$ docker-compose down
```

- Up kibana, elasticsearch containers
```zsh
$ docker-compose up kibana
```

- Delete index
```zsh
$ curl -X DELETE 'localhost:9200/zsh_history'
$ curl -X DELETE 'localhost:9200/zsh-history'
```

- Create index
```zsh
$ curl -H "Content-Type: application/json" -XPUT 'http://localhost:9200/zsh_history' -d @elasticsearch/mapping/zsh_history_mapping.json
$ curl -H "Content-Type: application/json" -XPUT 'http://localhost:9200/zsh-history' -d @elasticsearch/mapping/zsh_history_mapping.json
```

- Get current container image id(Ex. ${IMAGE_ID}: 3f4f149b2f63)
```zsh
$ docker ps | grep elasticsearch
3f4f149b2f63        shell-history-analyzer_elasticsearch   "/usr/local/bin/dock…"   About an hour ago   Up About an hour    0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp   elasticsearch
```

- Commit container image
```zsh
$ docker commit -m '${COMMIT_MESSAGE}' ${IMAGE_ID} elasticsearch-shell-history-analyzer:${NEW_VERSION}
```

- Update tag for dockerhub image
```zsh
$ docker tag ${IMAGE_ID} codequokka/elasticsearch-shell-history-analyzer:${NEW_VERSION}
```

- Push container image to dockerhub
```zsh
docker push codequokka/elasticsearch-shell-history-analyzer:${NEW_VERSION}
```

- Update ./elasticsearch/Dockerfile
```zsh
FROM codequokka/elasticsearch-shell-history-analyzer:${NEW_VERSION}
```
