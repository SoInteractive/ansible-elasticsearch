<p><img src="https://static-www.elastic.co/assets/blt6050efb80ceabd47/elastic-logo%20(2).svg" alt="elastic logo" title="elastic" align="right" height="60" /></p>

Ansible Role: elasticsearch
===================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-elasticsearch.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-elasticsearch) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.elasticsearch-blue.svg)](https://galaxy.ansible.com/SoInteractive/elasticsearch/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-elasticsearch.svg)](https://github.com/SoInteractive/ansible-elasticsearch/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Elasticsearch, distributed, RESTful search and analytics engine

# :warning: IMPORTANT NOTICE

THIS PROJECT IS ABANDONED. WE DO NOT ACCEPT ANY NEW ISSUES AND/OR PULL REQUESTS.

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

At least one master node has to be specified
```yaml
all:
  hosts:
    mysrv:
      ansible_host: 127.0.3.1
      elasticsearch_master_node: true
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
