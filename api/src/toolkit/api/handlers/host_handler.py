# Created by wangmeng at 2020/11/19
from fastapi import APIRouter, HTTPException

from toolkit.models.base_host import BaseHost
from toolkit.services.db_operate.host_operate import get_host_info_by_label, insert_new_host_info

router = APIRouter()


@router.get("/hosts/", tags=["hosts"])
async def get_hosts():
    return [{"label": "bastion"}, {"label": "remote-control"}]


@router.post("/hosts/")
async def create_host(host: BaseHost):
    try:
        insert_result = await insert_new_host_info(host)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return {'operate_result': insert_result}


@router.get("/hosts/{host_label}", tags=["hosts"])
async def get_host_info(host_label: str):
    try:
        target_host = await get_host_info_by_label(host_label)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        if not target_host:
            raise HTTPException(status_code=404, detail='no host founded')
        else:
            return target_host
