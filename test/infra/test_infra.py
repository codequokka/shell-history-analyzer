import pytest


@pytest.mark.parametrize('command', [
    'docker',
    'docker-compose',
])
def test_docker_command_exists(host, command):
    assert host.exists(command) is True


@pytest.mark.parametrize('container', [
    'elasticsearch',
    'logstash',
    'kibana',
])
def test_elasticsearch_container_is_running(host, container):
    container = host.docker(container)
    assert container.is_running is True


@pytest.mark.skip(reason='Testinfra does not support port testing on darwin')
def test_elasticsearch_port_is_listening(host):
    assert host.socket('tcp://127.0.0.1:9200').is_listening
    assert host.socket('tcp://127.0.0.1:9300').is_listening


@pytest.mark.skip(reason='Testinfra does not support port testing on darwin')
def test_kibana_port_is_listening(host):
    assert host.socket('tcp://127.0.0.1:5601').is_listening
