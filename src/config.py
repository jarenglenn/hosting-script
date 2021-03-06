


import os
import logging

import yaml
from pydantic import BaseModel
import pathlib

from . import util


CONFIG_FILE = util.resolve_relative("../config.yaml")


class AccessPointConfig(BaseModel):
    ssidname: str = "RPI-AP1"
    apwpa2passwd: str = "cH4nG3M3"
    ipv4ipwlan0: str = "192.168.0.1/28"

class WebServerConfig(BaseModel):
    directory: pathlib.Path = "~/server/"
    # existing_flask_app: bool = False
    # flask_app_path: str = "~/WebServer"
    # entry_point: str = "hello:app"
    # virtual_environment_dir: str = ".venv"


class Config(BaseModel):
    access_point: AccessPointConfig = AccessPointConfig()
    web_server: WebServerConfig = WebServerConfig()

    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            contents = f.read()

        data = yaml.load(contents, Loader=yaml.CLoader)
        return cls(**data)


if os.path.isfile(CONFIG_FILE):
    logging.debug(f"Loading config from {CONFIG_FILE}")
    config: Config = Config.from_file(CONFIG_FILE)
else:
    logging.debug(f"No config file found, using defaults")
    config = Config()