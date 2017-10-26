from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_yum_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'centos':
        present = [
            "libselinux-python",
            "elasticsearch"
        ]
        if present:
            for package in present:
                p = Package(package)
                assert p.is_installed


def test_apt_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'ubuntu':
        present = [
            "apt-transport-https",
            "elasticsearch"
        ]
        if present:
            for package in present:
                p = Package(package)
                assert p.is_installed


def test_directories(File):
    present_elastic = [
        "/var/run/elasticsearch",
        "/var/log/elasticsearch",
        "/etc/elasticsearch",
        "/tmp/elasticsearch"
    ]
    present = [
        "/var/lib/elasticsearch",
        "/usr/share/elasticsearch"
    ]
    if present_elastic:
        for directory in present_elastic:
            d = File(directory)
            assert d.is_directory
            assert d.exists
            assert d.group == "elasticsearch"
            assert d.user == "elasticsearch"
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/elasticsearch/elasticsearch.yml"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file