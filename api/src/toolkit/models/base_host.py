# Created by wangmeng at 2020/11/19
from fabric import Connection, Result
from pydantic import BaseModel


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
    connection: Connection = None

    def get_connection(self) -> Connection:
        raise NotImplementedError

    def run(self, command: str, *args, **kwargs) -> Result:
        raise NotImplementedError
