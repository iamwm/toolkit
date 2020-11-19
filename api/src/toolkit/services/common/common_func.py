# Created by wangmeng at 2020/11/19

def is_host_a_bastion(host_info: dict) -> bool:
    return not ('bastion_name' in host_info)
