import pytest
from elasticsearch import Elasticsearch


@pytest.fixture()
def es():
    es = Elasticsearch()
    return es


class TestZshHistoryFileIndex(object):
    def test_index_exists(self, es):
        index = es.indices.exists(index='zsh_history')
        assert index is True

    def test_mapping_exists(self, es):
        mapping = es.indices.get_mapping(index='zsh_history')
        assert 'zsh_history' in mapping

    def test_mapping_has_timestamp_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh_history',
                                               fields='@timestamp')
        field_type = (mapping['zsh_history']['mappings']['@timestamp']
                      ['mapping']['@timestamp']['type'])
        assert field_type == 'date'

    def test_mapping_has_executed_command_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh_history',
                                               fields='executed_command')
        field_type = (mapping['zsh_history']['mappings']['executed_command']
                      ['mapping']['executed_command']['type'])
        assert field_type == 'keyword'


class TestZshHistoryIndex(object):
    def test_index_exists(self, es):
        index = es.indices.exists(index='zsh-history')
        assert index is True

    def test_mapping_exists(self, es):
        mapping = es.indices.get_mapping(index='zsh-history')
        assert 'zsh-history' in mapping

    def test_mapping_has_timestamp_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh-history',
                                               fields='@timestamp')
        field_type = (mapping['zsh-history']['mappings']['@timestamp']
                      ['mapping']['@timestamp']['type'])
        assert field_type == 'date'

    def test_mapping_has_executed_command_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh-history',
                                               fields='executed_command')
        field_type = (mapping['zsh-history']['mappings']['executed_command']
                      ['mapping']['executed_command']['type'])
        assert field_type == 'keyword'

    def test_mapping_has_dir_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh-history',
                                               fields='dir')
        field_type = (mapping['zsh-history']['mappings']['dir']['mapping']
                      ['dir']['type'])
        assert field_type == 'keyword'

    def test_mapping_has_host_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh-history',
                                               fields='host')
        field_type = (mapping['zsh-history']['mappings']['host']['mapping']
                      ['host']['type'])
        assert field_type == 'keyword'

    def test_mapping_has_status_fields(self, es):
        mapping = es.indices.get_field_mapping(index='zsh-history',
                                               fields='status')
        field_type = (mapping['zsh-history']['mappings']['status']['mapping']
                      ['status']['type'])
        assert field_type == 'short'
