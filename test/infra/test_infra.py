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
def test_container_is_running(host, container):
    container = host.docker(container)
    assert container.is_running is True


@pytest.mark.parametrize('container', [
    'elasticsearch',
    'logstash',
    'kibana',
])
def test_container_is_running_at_tz_env_var(host, container):
    container = host.docker(container)
    date = host.run('docker exec' + ' ' + container.id + ' ' + 'date')
    assert 'JST' in date.stdout


@pytest.mark.parametrize('url', [
    'tcp://127.0.0.1:9200',
    'tcp://127.0.0.1:9300',
])
def test_elasticsearch_port_is_listening(host, url):
    if host.system_info.type == 'darwin':
        pytest.skip("Testinfra does not support port testing on darwin")
    else:
        assert host.socket(url).is_listening


def test_kibana_port_is_listening(host):
    if host.system_info.type == 'darwin':
        pytest.skip("Testinfra does not support port testing on darwin")
    else:
        assert host.socket('tcp://127.0.0.1:5601').is_listening
