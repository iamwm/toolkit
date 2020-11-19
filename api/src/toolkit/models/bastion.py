# Created by wangmeng at 2020/11/19
from fabric import Result, Connection

from toolkit.models.base_host import BaseHost


class Bastion(BaseHost):
    def get_connection(self) -> Connection:
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
    bastion_info = {
        "label": "test_host",
        "address": "192.168.20.144",
        "username": "root",
        "password": "123456",
        "group": "Test"
    }
    bastion = Bastion(**bastion_info)
    hostname = bastion.run("hostname")
    print(hostname)
