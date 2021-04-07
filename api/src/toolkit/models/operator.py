# Created by wangmeng at 2020/11/19

from motor.motor_asyncio import AsyncIOMotorClient


class Operator(object):
    # used to operate with mongodb for hosts

    def __init__(self, host: str, port: int, ):
        self.client = AsyncIOMotorClient(host=host, port=port)


class HostOperator(Operator):
    database_name: str = "toolkit"
    collection_name: str = "hosts"

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    async def insert_host_info(self, host_info: dict) -> bool:
        # Do validation outside here.
        # if `bastion_name` in host_info, try to convert host_info to a host else a bastion
        label = host_info.get('label')
        try:
            await self.collection.find_one_and_update({'label': label}, {'$set': host_info}, upsert=True)
        except Exception:
            return False
        else:
            return True

    async def is_host_exists(self, label: str) -> bool:
        target_host = await self.collection.find_one({'label': label})
        return bool(target_host)

    async def get_host_info_by_filter(self, query_filter: dict) -> dict:
        target_host = await self.collection.find_one(query_filter)
        return target_host

    async def get_target_bastion_info(self, bastion_name: str):
        query_filter = {'label': bastion_name}
        target_host = await self.collection.find_one(query_filter)
        return target_host


class GroupOperator(Operator):
    database_name: str = "toolkit"
    collection_name: str = "groups"

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]
