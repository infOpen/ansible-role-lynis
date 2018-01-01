"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('directory', '/var/lib/lynis', 'root', 'root', 0o755),
    ('directory', '/var/log/lynis-reports', 'root', 'root', 0o750),
    ('file', '/etc/cron.d/lynis', 'root', 'root', 0o644),
])
def test_paths_properties(host, item_type, path, user, group, mode):
    """
    Tests about Lynis paths properties
    """

    current_item = host.file(path)

    assert current_item.exists

    if item_type == 'directory':
        assert current_item.is_directory
    elif item_type == 'file':
        assert current_item.is_file

    assert current_item.user == user
    assert current_item.group == group
    assert current_item.mode == mode


def test_crontab_content(host):
    """
    Tests about crontab file content
    """

    crontab_file = host.file('/etc/cron.d/lynis')

    assert crontab_file.contains('* root')
