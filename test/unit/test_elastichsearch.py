import pytest
from elasticsearch import Elasticsearch


@pytest.fixture()
def es():
    es = Elasticsearch()
    return es


class TestZshHistoryFileIndex(object):
    def test_index_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Index does not exist at this time.")
        else:
            index = es.indices.exists(index='zsh_history')
            assert index is True

    def test_template_exists(self, es):
        template = es.indices.exists_template(name='zsh_history')
        assert template is True

    def test_mapping_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_mapping(index='zsh_history')
            assert 'zsh_history' in mapping

    def test_mapping_has_timestamp_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh_history',
                                                   fields='@timestamp')
            field_type = (mapping['zsh_history']['mappings']['@timestamp']
                          ['mapping']['@timestamp']['type'])
            assert field_type == 'date'

    def test_mapping_has_executed_command_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh_history',
                                                   fields='executed_command')
            field_type = (
                mapping['zsh_history']['mappings']['executed_command']
                ['mapping']['executed_command']['type'])
            assert field_type == 'keyword'


class TestZshHistoryIndex(object):
    def test_index_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Index does not exist at this time.")
        else:
            index = es.indices.exists(index='zsh-history')
            assert index is True

    def test_template_exists(self, es):
        template = es.indices.exists_template(name='zsh-history')
        assert template is True

    def test_mapping_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_mapping(index='zsh-history')
            assert 'zsh-history' in mapping

    def test_mapping_has_timestamp_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-history',
                                                   fields='@timestamp')
            field_type = (mapping['zsh-history']['mappings']['@timestamp']
                          ['mapping']['@timestamp']['type'])
            assert field_type == 'date'

    def test_mapping_has_executed_command_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-history',
                                                   fields='executed_command')
            field_type = (
                mapping['zsh-history']['mappings']['executed_command']
                ['mapping']['executed_command']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_dir_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-history',
                                                   fields='dir')
            field_type = (mapping['zsh-history']['mappings']['dir']['mapping']
                          ['dir']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_host_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-history',
                                                   fields='host')
            field_type = (mapping['zsh-history']['mappings']['host']['mapping']
                          ['host']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_status_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-history',
                                                   fields='status')
            field_type = (mapping['zsh-history']['mappings']['status']
                          ['mapping']['status']['type'])
            assert field_type == 'short'


class TestZshHistdbIndex(object):
    def test_index_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Index does not exist at this time.")
        else:
            index = es.indices.exists(index='zsh-histdb')
            assert index is True

    def test_template_exists(self, es):
        template = es.indices.exists_template(name='zsh-histdb')
        assert template is True

    def test_mapping_exists(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_mapping(index='zsh-histdb')
            assert 'zsh-histdb' in mapping

    def test_mapping_has_timestamp_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='@timestamp')
            field_type = (mapping['zsh-histdb']['mappings']['@timestamp']
                          ['mapping']['@timestamp']['type'])
            assert field_type == 'date'

    def test_mapping_has_executed_command_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='executed_command')
            field_type = (mapping['zsh-histdb']['mappings']['executed_command']
                          ['mapping']['executed_command']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_dir_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='dir')
            field_type = (mapping['zsh-histdb']['mappings']['dir']['mapping']
                          ['dir']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_host_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='host')
            field_type = (mapping['zsh-histdb']['mappings']['host']['mapping']
                          ['host']['type'])
            assert field_type == 'keyword'

    def test_mapping_has_status_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='status')
            field_type = (mapping['zsh-histdb']['mappings']['status']
                          ['mapping']['status']['type'])
            assert field_type == 'short'

    def test_mapping_has_session_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='session')
            field_type = (mapping['zsh-histdb']['mappings']['session']
                          ['mapping']['session']['type'])
            assert field_type == 'integer'

    def test_mapping_has_duration_fields(self, host, es):
        if host.system_info.type == 'linux':
            pytest.skip("Mapping does not exist at this time.")
        else:
            mapping = es.indices.get_field_mapping(index='zsh-histdb',
                                                   fields='duration')
            field_type = (mapping['zsh-histdb']['mappings']['duration']
                          ['mapping']['duration']['type'])
            assert field_type == 'integer'
