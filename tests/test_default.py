from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'centos':
        present = [
            "python-pip"
        ]
        if present:
            for package in present:
                p = Package(package)
                assert p.is_installed


def test_socket(host):
    present = [
        "tcp://127.0.0.1:9200",
        "tcp://127.0.0.1:9300"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
