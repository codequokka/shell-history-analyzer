# Update elasticsearch image

## How to update

- Down all container
```zsh
$ docker-compose down
```

- Up elasticsearch container only
```zsh
$ docker-compose up elasticsearch
```

- Delete index
```zsh
$ curl -X DELETE 'localhost:9200/zsh_history'
```

- Create index
```zsh
$ curl -H "Content-Type: application/json" -XPUT 'http://localhost:9200/zsh_history' -d @elasticsearch/mapping/zsh_history_mapping.json
```

- Up kibana container
```zsh
$ docker-compose up kibana
```

- Get new zsh_history index-pattern
```zsh
curl -H "Content-Type: application/json" -XGET 'http://localhost:9200/.kibana/_search?pretty' -d @elasticsearch/search/index_id.json
{
  "took" : 7,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 2.2335923,
    "hits" : [
      {
        "_index" : ".kibana_1",
        "_type" : "_doc",
        "_id" : "index-pattern:d87c4e10-7433-11e9-a264-b93a50569154",
        "_score" : 2.2335923,
        "_source" : {
          "index-pattern" : {
            "title" : "zsh_history*",
            "timeFieldName" : "@timestamp",
            "fields" : "[{\"name\":\"@timestamp\",\"type\":\"date\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":true},{\"name\":\"_id\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":false},{\"name\":\"_index\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":false},{\"name\":\"_score\",\"type\":\"number\",\"count\":0,\"scripted\":false,\"searchable\":false,\"aggregatable\":false,\"readFromDocValues\":false},{\"name\":\"_source\",\"type\":\"_source\",\"count\":0,\"scripted\":false,\"searchable\":false,\"aggregatable\":false,\"readFromDocValues\":false},{\"name\":\"_type\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":false},{\"name\":\"executed_command\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":true},{\"name\":\"tags\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":false,\"readFromDocValues\":false},{\"name\":\"tags.keyword\",\"type\":\"string\",\"count\":0,\"scripted\":false,\"searchable\":true,\"aggregatable\":true,\"readFromDocValues\":true}]"
          },
          "type" : "index-pattern",
          "references" : [ ],
          "updated_at" : "2019-05-11T21:29:25.564Z"
        }
      }
    ]
  }
}
```

- Update charts to use new zsh_history index

- Get current container image id(Ex. ${IMAGE_ID}: 3f4f149b2f63)
```zsh
$ docker-compose restart logstash
$ docker ps | grep elasticsearch
3f4f149b2f63        shell-history-analyzer_elasticsearch   "/usr/local/bin/dock…"   About an hour ago   Up About an hour    0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp   elasticsearch
```

- Commit container image
```zsh
$ docker commit -m '${COMMIT_MESSAGE}' ${IMAGE_ID} elasticsearch-shell-history-analyzer:${NEW_VERSION}
```

- Update tag for dockerhub image
```zsh
$ docker tag ${IMAGE_ID} codequokka/elasticsearch-shell-history-analyzer:0.1.1
```

- Push container image to dockerhub
```zsh
docker push codequokka/elasticsearch-shell-history-analyzer:${NEW_VERSION}
```

- Update ./elasticsearch/Dockerfile
```zsh
FROM codequokka/elasticsearch-shell-history-analyzer:${NEW_VERSION}
```
