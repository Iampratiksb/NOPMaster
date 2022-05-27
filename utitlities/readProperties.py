import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class readConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getApplicationEmail():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationPassword():
        password=config.get('common info', 'password')
        return password
