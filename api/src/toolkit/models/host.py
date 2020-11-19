# Created by wangmeng at 2020/11/19
from fabric import Result, Connection

from toolkit.models.base_host import BaseHost


class Host(BaseHost):
    bastion: BaseHost = None

    async def get_bastion(self) -> BaseHost:
        if self.bastion_name is None:
            return None
        else:
            target_bastion_info = await self.operator.get_target_bastion_info(self.bastion_name)
            return Host(**target_bastion_info)

    def to_dict(self):
        return self.dict(exclude={'connection', 'operator', 'bastion'})

    async def get_connection(self) -> Connection:
        # if bastion is None, connect directly else creat connection through bastion
        self.bastion = await self.get_bastion()
        if self.bastion is not None:
            gateway_connection = await self.bastion.get_connection()
            _connection = Connection(self.address, user=self.username, port=self.port,
                                     connect_kwargs={'password': self.password},
                                     gateway=gateway_connection)
        else:
            _connection = Connection(self.address, user=self.username, port=self.port,
                                     connect_kwargs={'password': self.password})
        return _connection

    async def run(self, command: str, *args, **kwargs) -> Result:
        if self.connection is None:
            self.connection = await self.get_connection()
        with self.connection as conn:
            command_result = conn.run(command, **kwargs)
        return command_result


if __name__ == '__main__':
    host_info = {
        "label": "realtech",
        "address": "192.168.20.6",
        "username": "realtech",
        "password": "abc@123",
        "group": "Test"
    }

    bastion_info = {
        "label": "test_host",
        "address": "192.168.20.144",
        "username": "root",
        "password": "123456",
        "group": "Test"
    }

    bastion = Host(**bastion_info)
    host = Host(**host_info)
    host.bastion = bastion

    import asyncio


    async def execute_command():
        hostname = await host.run("hostname")
        print(hostname)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(execute_command())
