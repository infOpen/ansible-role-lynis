"""
Role tests
"""
import pytest


# pytestmark = pytest.mark.docker_images(
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_installation_directory(File):
    """
    Tests about installation folder
    """

    install_directory = File('/var/lib/lynis')

    assert install_directory.exists is True
    assert install_directory.is_directory is True
    assert install_directory.user == 'root'
    assert install_directory.group == 'root'


def test_reports_directory(File):
    """
    Tests about reports folder
    """

    reports_directory = File('/var/log/lynis-reports')

    assert reports_directory.exists is True
    assert reports_directory.is_directory is True
    assert reports_directory.user == 'root'
    assert reports_directory.group == 'root'


def test_crontab(File):
    """
    Tests about crontab file
    """

    crontab_file = File('/etc/cron.d/lynis')

    assert crontab_file.exists is True
    assert crontab_file.is_file is True
    assert crontab_file.user == 'root'
    assert crontab_file.group == 'root'
    assert crontab_file.contains('* root') is True
