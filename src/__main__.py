import uvicorn
from dotenv import load_dotenv
from .core.config import applicaion_setting
import os

load_dotenv()

if __name__=="__main__":
    app = "src:app"
    uvicorn.run(
        app=app, 
        host=applicaion_setting.HOST_IP, 
        port=applicaion_setting.HOST_PORT, 
        reload=applicaion_setting.DEBUG,
        log_config=None,
        log_level=None,
    )