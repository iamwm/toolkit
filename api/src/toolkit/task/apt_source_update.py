# Created by wangmeng at 2021/4/8 🍻🍻
from asyncio import gather
from typing import List

from toolkit.models.task import TaskBase


class AptSourceListUpdateTask(TaskBase):
    name = "apt source list update"
    desc = "更新目标主机的apt源"
    scripts: List[str] = ["./toolkit/services/scripts/apt_source_update.sh"]

    async def task_init(self):
        # 将scripts上传到主机列表
        for host in self.host_list:
            connection = await host.get_connection()
            for script in self.scripts:
                connection.put(script)

    async def clean_up(self):
        pass

    async def run(self):
        # 运行已经上传的脚本
        commands = ["bash ./apt_source_update.sh"]
        task_on_hosts = []
        for host in self.host_list:
            task = host.run(commands)
            task_on_hosts.append(task)
        await gather(*task_on_hosts)
