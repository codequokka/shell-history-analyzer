import pytest
from elasticsearch import Elasticsearch


@pytest.fixture()
def es():
    es = Elasticsearch()
    return es


def test_zsh_history_index_exists(es):
    index = es.indices.exists(index='zsh_history')
    assert index is True


def test_zsh_history_mapping_exists(es):
    mapping = es.indices.get_mapping(index='zsh_history')
    assert 'zsh_history' in mapping


def test_zsh_history_mapping_has_correct_fields(es):
    timestamp_mapping = es.indices.get_field_mapping(index='zsh_history',
                                                     fields='@timestamp')
    timestamp_type = (timestamp_mapping['zsh_history']['mappings']
                      ['@timestamp']['mapping']['@timestamp']['type'])
    timestamp_mapping = es.indices.get_field_mapping(index='zsh_history',
                                                     fields='executed_command')
    executed_command_type = (
        timestamp_mapping['zsh_history']['mappings']['executed_command']
        ['mapping']['executed_command']['type'])
    assert timestamp_type == 'date'
    assert executed_command_type == 'keyword'
