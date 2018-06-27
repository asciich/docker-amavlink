import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/amavlink'

class TestAsciichAMavlink(object):

    def test_amavlink_installed(self, docker_container):
        assert docker_container.exists('amavlink')

    def test_amavlink_python_import(self, docker_container):
        docker_container.check_output('python - c "from amavlink.AMavlink import AMavlink"')