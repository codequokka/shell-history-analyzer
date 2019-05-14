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
