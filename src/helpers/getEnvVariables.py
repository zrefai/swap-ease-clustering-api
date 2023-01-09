from dotenv import dotenv_values

def getEnvVariables():
    return dotenv_values(".env")