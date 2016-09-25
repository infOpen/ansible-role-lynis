# lynis

[![Build Status](https://travis-ci.org/infOpen/ansible-role-lynis.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-lynis)

Ansible role to manage Lynis installation and configuration

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role has some testing methods:

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

### Default role variables

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.lynis }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

