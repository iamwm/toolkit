# Created by wangmeng at 2020/11/19
from fabric import Connection, Result
from pydantic import BaseModel

from toolkit.models.operator import HostOperator


class BaseHost(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    label: str
    group: str
    address: str
    port: int = 22
    username: str
    password: str
    group: str
    bastion_name: str = None
    connection: Connection = None
    operator: HostOperator = None

    def get_connection(self) -> Connection:
        raise NotImplementedError

    def run(self, command: str, *args, **kwargs) -> Result:
        raise NotImplementedError

    def to_dict(self):
        return self.dict(exclude={'connection', 'operator'})
