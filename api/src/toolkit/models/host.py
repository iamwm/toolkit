# Created by wangmeng at 2020/11/19
from asyncio import get_event_loop

from fabric import Result, Connection

from toolkit.models.base_host import BaseHost


class Host(BaseHost):
    bastion: BaseHost = None

    async def get_bastion(self) -> BaseHost:
        if self.bastion_name is None:
            return None
        else:
            target_bastion_info = await self.operator.get_target_bastion_info(self.bastion_name)
            return Host(**target_bastion_info, operator=self.operator)

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

    async def run(self, commands: list, *args, **kwargs) -> Result:
        loop = get_event_loop()
        if self.connection is None:
            self.connection = await self.get_connection()
        with self.connection as conn:
            for command in commands:
                command_result = await loop.run_in_executor(None, conn.run, *[command])
        return command_result
