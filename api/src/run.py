# Created by wangmeng at 2020/11/2
import uvicorn

from toolkit.main import app

api_server = app

if __name__ == '__main__':
    uvicorn.run("run:api_server", host="127.0.0.1", port=4321)
