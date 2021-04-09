from asyncio import get_event_loop
from unittest import TestCase

# Created by wangmeng at 2021/4/9 🍻🍻
from toolkit.models.host import Host
from toolkit.task.python import PythonInstallTask


class TestPythonInstallTask(TestCase):
    def setUp(self) -> None:
        host = Host.create_host(**{
            'label': 'mongo1',
            'group': 'mongo1',
            'address': '192.168.20.128',
            'username': 'root',
            'password': 'abc@123'
        })
        self.host = host
        self.task = PythonInstallTask(host_list=[self.host], scripts=["../services/scripts/python.sh"])

    def tearDown(self) -> None:
        pass

    def test_task_init(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.task_init())

    def test_run(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.run())
