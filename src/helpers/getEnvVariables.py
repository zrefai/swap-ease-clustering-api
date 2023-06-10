from dataclasses import dataclass
from typing import Dict
from dotenv import dotenv_values


@dataclass
class EnvVariable:
    OPENSEA_URL: str
    OPENSEA_API_KEY: str
    MONGO_DB_CONNECTION_STRING: str
    MONGO_DB_NAME: str
    SWAP_EASE_API_URL: str
    ALCHEMY_API_URL: str
    ALCHEMY_API_KEY: str


def verifyEnvVariable(key: str, dotenvObject: Dict[str, str | None]):
    envVariable = dotenvObject[key]

    assert envVariable is not None and len(
        envVariable) > 0, "Environment variable {0} is undefined or empty".format(key)

    return envVariable


def getEnvVariables():
    dotenvObject = dotenv_values('.env')

    OPENSEA_URL = verifyEnvVariable('OPENSEA_URL', dotenvObject)
    OPENSEA_API_KEY = verifyEnvVariable('OPENSEA_API_KEY', dotenvObject)
    MONGO_DB_CONNECTION_STRING = verifyEnvVariable(
        'MONGO_DB_CONNECTION_STRING', dotenvObject)
    MONGO_DB_NAME = verifyEnvVariable('MONGO_DB_NAME', dotenvObject)
    SWAP_EASE_API_URL = verifyEnvVariable('SWAP_EASE_API_URL', dotenvObject)
    ALCHEMY_API_URL = verifyEnvVariable('ALCHEMY_API_URL', dotenvObject)
    ALCHEMY_API_KEY = verifyEnvVariable('ALCHEMY_API_KEY', dotenvObject)

    return EnvVariable(
        OPENSEA_URL,
        OPENSEA_API_KEY,
        MONGO_DB_CONNECTION_STRING,
        MONGO_DB_NAME,
        SWAP_EASE_API_URL,
        ALCHEMY_API_URL,
        ALCHEMY_API_KEY
    )
