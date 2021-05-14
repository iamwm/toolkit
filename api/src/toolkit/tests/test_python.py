from asyncio import get_event_loop
from unittest import TestCase

# Created by wangmeng at 2021/4/9 🍻🍻
from toolkit.models.host import Host
from toolkit.task.python import PythonInstallTask


class TestPythonInstallTask(TestCase):
    def setUp(self) -> None:
        host1 = Host.create_host(**{
            'label': 'mongo2',
            'group': 'mongo2',
            'address': '192.168.225.248',
            'username': 'root',
            'password': 'abc@123'
        })
        host2 = Host.create_host(**{
            'label': 'mongo3',
            'group': 'mongo3',
            'address': '192.168.20.126',
            'username': 'root',
            'password': 'abc@123'
        })
        host3 = Host.create_host(**{
            'label': 'mongo4',
            'group': 'mongo4',
            'address': '192.168.20.123',
            'username': 'root',
            'password': 'abc@123'
        })
        self.task = PythonInstallTask(host_list=[host1], scripts=["../services/scripts/python.sh"])

    def tearDown(self) -> None:
        loop = get_event_loop()
        loop.close()

    def test_task_init(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.task_init())

    def test_run(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.run())
