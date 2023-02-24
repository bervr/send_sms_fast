import configparser
import os

from fastapi import FastAPI

from send_database import ServerStorage

app = FastAPI()
dir_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(f"{dir_path}/{'server.ini'}")
database = ServerStorage(
        os.path.join(
            # config['SETTINGS']['Database_path'],
            dir_path,
            config['SETTINGS']['Database_file']))


@app.get("/")
async def root():
    return {f"all_campains": database.all_campain()}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
