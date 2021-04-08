# Created by wangmeng at 2021/4/8 🍻🍻
from abc import ABC, abstractmethod
from logging import Logger
from typing import List

from pydantic import BaseModel

from toolkit.models.base_host import BaseHost


class TaskBase(BaseModel, ABC):
    class Config:
        arbitrary_types_allowed = True

    name: str
    desc: str
    logger: Logger = None
    host_list: List[BaseHost]
    scripts: List[str] = []

    @abstractmethod
    async def task_init(self):
        pass

    @abstractmethod
    async def clean_up(self):
        pass

    @abstractmethod
    async def run(self):
        pass
