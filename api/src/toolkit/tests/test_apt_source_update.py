# Created by wangmeng at 2021/4/8 🍻🍻
from asyncio import get_event_loop
from unittest import TestCase

from toolkit.models.host import Host
from toolkit.task.apt_source_update import AptSourceListUpdateTask


class TestAptSourceListUpdateTask(TestCase):
    def setUp(self) -> None:
        host = Host.create_host(**{
            'label': '144',
            'group': '武汉测试',
            'address': '192.168.20.144',
            'username': 'root',
            'password': '123456'
        })
        self.host = host
        self.task = AptSourceListUpdateTask(host_list=[self.host], scripts=["../services/scripts/apt_source_update.sh"])

    def tearDown(self) -> None:
        pass

    def test_task_init(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.task_init())

    def test_clean_up(self):
        pass

    def test_run(self):
        loop = get_event_loop()
        loop.run_until_complete(self.task.run())
