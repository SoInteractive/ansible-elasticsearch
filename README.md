<p><img src="https://static-www.elastic.co/assets/blt6050efb80ceabd47/elastic-logo%20(2).svg" alt="elastic logo" title="elastic" align="right" height="60" /></p>

Ansible Role: elasticsearch
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/elasticsearch/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Felasticsearch/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/99999.svg)](https://galaxy.ansible.com/SoInteractive/elasticsearch/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Elasticsearch, distributed, RESTful search and analytics engine

Disclaimer
----------

Role based on https://github.com/elastic/ansible-elasticsearch

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.elasticsearch
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- user-based install
- clustering
