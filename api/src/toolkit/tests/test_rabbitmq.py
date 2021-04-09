from asyncio import get_event_loop
from unittest import TestCase

# Created by wangmeng at 2021/4/9 🍻🍻
from toolkit.models.host import Host
from toolkit.task.rabbitmq import RabbitmqTask


class TestRabbitmqTask(TestCase):
    def setUp(self) -> None:
        host = Host.create_host(**{
            'label': '144',
            'group': '武汉测试',
            'address': '192.168.20.144',
            'username': 'root',
            'password': '123456'
        })
        self.host = host
        self.task = RabbitmqTask(host_list=[self.host], scripts=["../services/scripts/rabbitmq.sh"])

    def tearDown(self) -> None:
        pass

    def test_task_init(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.task_init())

    def test_run(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.run())
