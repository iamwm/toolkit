# Created by wangmeng at 2020/11/19
from fabric import Result, Connection

from toolkit.models.base_host import BaseHost
from toolkit.models.bastion import Bastion


class Host(BaseHost):
    bastion_name: str = None
    bastion: Bastion = None

    def get_bastion(self) -> Bastion:
        if self.bastion_name is None:
            return None
        else:
            pass

    def get_connection(self) -> Connection:
        # if bastion is None, connect directly else creat connection through bastion
        if self.get_bastion() is not None:
            _connection = Connection(self.address, user=self.username, port=self.port,
                                     connect_kwargs={'password': self.password},
                                     gateway=self.get_bastion().get_connection())
        else:
            _connection = Connection(self.address, user=self.username, port=self.port,
                                     connect_kwargs={'password': self.password})
        return _connection

    def run(self, command: str, *args, **kwargs) -> Result:
        if self.connection is None:
            self.connection = self.get_connection()
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

    bastion = Bastion(**bastion_info)
    host = Host(**host_info)
    host.bastion = bastion

    hostname = host.run("hostname")
    print(hostname)
