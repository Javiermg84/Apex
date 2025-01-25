import configparser

config = configparser.RawConfigParser()
config.read("Configurations\\config.ini")

class Read_Config:

    @staticmethod
    def get_webpage():
        url = config.get('DEFAULT','web_page')
        return url

    @staticmethod
    def console_type():
        cons_type = config.get('MainTestInfo','console')
        return cons_type