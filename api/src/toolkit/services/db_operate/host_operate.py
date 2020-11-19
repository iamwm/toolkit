# Created by wangmeng at 2020/11/19
from toolkit.models.base_host import BaseHost
from toolkit.models.host import Host
from toolkit.models.operator import HostOperator


async def get_host_info_by_label(label: str) -> dict:
    operator = HostOperator('localhost', 27017)
    host_info = await operator.get_host_info_by_filter({'label': label})
    if not host_info:
        return None
    target_host = Host(**host_info)
    return target_host.to_dict()


async def insert_new_host_info(host: BaseHost) -> bool:
    operator = HostOperator('localhost', 27017)
    await operator.insert_host_info(host.to_dict())
    return True
