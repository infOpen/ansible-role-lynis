# lynis

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-lynis/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-lynis)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-lynis/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-lynis)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-lynis/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-lynis/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-lynis/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-lynis/)
[![Ansible Role](https://img.shields.io/ansible/role/9965.svg)](https://galaxy.ansible.com/infOpen/lynis/)

Install lynis package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Packages and repositories management
# -----------------------------------------------------------------------------
lynis_repository_cache_valid_time: 3600
lynis_repository_update_cache: True
lynis_git_system_prerequisites: "{{ _lynis_git_system_prerequisites | default([]) }}"


# Global installation vars
# -----------------------------------------------------------------------------
# Managed installation types:
#   - 'git'
lynis_installation_type: 'git'
lynis_installation_version: '2.2.0'
lynis_user:
  name: 'root'
  home:
    path: '/root'
lynis_group:
  name: 'root'


# GIT installation variables
# -----------------------------------------------------------------------------

# Add Github host key
# See: https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/
lynis_git_host_keys:
  - name: 'github.com'
    key: |
      |1|XSnxOghgS/1AkYu80DtXWOBnhcQ=|fc7xOMfZJSHGhNmO1FJ5sAQt2eA= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==
    state: 'present'
lynis_git_accept_host_key: False
lynis_git_repository: 'https://github.com/CISOfy/lynis.git'


# Reports directory management
# -----------------------------------------------------------------------------
lynis_paths:
  dirs:
    install:
      path: '/var/lib/lynis'
      mode: '0750'
    reports:
      path: '/var/log/lynis-reports'
      mode: '0750'


# Crontab management
# -----------------------------------------------------------------------------
lynis_manage_crontab: True
lynis_crontab_file_name: 'lynis'
lynis_crontab_vars:
  - name: 'CURRENT_DATE'
    value: 'date +%Y%m%d'
    user: "{{ lynis_user.name }}"
    state: 'present'
lynis_crontab_jobs:
  - name: 'Automatic Lynis daily report'
    file_name: "{{ lynis_crontab_file_name }}"
    minute: 13
    hour: 12
    weekday: '*'
    day: '*'
    month: '*'
    job: >
      cd {{ lynis_paths.dirs.install.path }}
      && ./lynis --cronjob --auditor "Automatic daily scan"
      --report-file "{{ lynis_paths.dirs.reports.path }}/$($CURRENT_DATE)-auto.dat"
      > "{{ lynis_paths.dirs.reports.path }}/$($CURRENT_DATE)-cron.log" 2>&1
    user: "{{ lynis_user.name }}"
    state: 'present'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.lynis }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
