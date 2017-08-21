# lynis

[![Build Status](https://travis-ci.org/infOpen/ansible-role-lynis.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-lynis)

Install lynis package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Managed installation types:
#   - 'git'
lynis_installation_type: 'git'


# Global installation vars
lynis_installation_dir: '/var/lib/lynis'
lynis_installation_version: '2.2.0'

lynis_installation_owner: 'root'
lynis_installation_group: 'root'

# Default vars used with git installation type
#---------------------------------------------

lynis_apt_cache_valid_time: 3600
lynis_apt_update_cache: True
lynis_git_prerequisites:
  - 'git'

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
#-----------------------------
lynis_reports_dir_path: '/var/log/lynis-reports'
lynis_reports_dir_owner: "{{ lynis_installation_owner }}"
lynis_reports_dir_group: "{{ lynis_installation_group }}"
lynis_reports_dir_mode: '0750'

# Crontab management
#-------------------
lynis_manage_crontab: True
lynis_crontab_file_name: 'lynis'
lynis_crontab_vars:
  - name: 'CURRENT_DATE'
    value: 'date +%Y%m%d'
    user: "{{ lynis_installation_owner }}"
    state: 'present'
lynis_crontab_jobs:
  - name: 'Automatic Lynis daily report'
    file_name: "{{ lynis_crontab_file_name }}"
    minute: 13
    hour: 12
    weekday: '*'
    day: '*'
    month: '*'
    job: "{{
      'cd ' ~ lynis_installation_dir
        ~ ' && ./lynis --cronjob --auditor \"Automatic daily scan\"'
        ~ ' --report-file \"'
                ~ lynis_reports_dir_path ~ '/$($CURRENT_DATE)-auto.dat\"'
        ~ ' --logfile \"'
                ~ lynis_reports_dir_path ~ '/$($CURRENT_DATE)-auto.log\"'
        ~ ' > \"' ~ lynis_reports_dir_path ~ '/$($CURRENT_DATE)-cron.log\"'
        ~ ' 2>&1' }}"
    user: "{{ lynis_installation_owner }}"
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
