import pytest


def test_docker_command_exists(host):
    assert host.exists('docker') is True


def test_docker_compose_command_exists(host):
    assert host.exists('docker-compose') is True


def test_elasticsearch_container_is_running(host):
    elasticsearch = host.docker('elasticsearch')
    assert elasticsearch.is_running is True


def test_logstash_container_is_running(host):
    elasticsearch = host.docker('logstash')
    assert elasticsearch.is_running is True


def test_kibana_container_is_running(host):
    elasticsearch = host.docker('kibana')
    assert elasticsearch.is_running is True


@pytest.mark.skip(reason='Testinfra does not support port testing on darwin')
def test_elasticsearch_port_is_listening(host):
    assert host.socket('tcp://127.0.0.1:9200').is_listening
    assert host.socket('tcp://127.0.0.1:9300').is_listening


@pytest.mark.skip(reason='Testinfra does not support port testing on darwin')
def test_kibana_port_is_listening(host):
    assert host.socket('tcp://127.0.0.1:5601').is_listening
