import os


class LoginData:

    def __init__(self, tradingType):
        tmp_logginData = self.readLoginData(tradingType)
        self.API_URL = tmp_logginData[0]
        self.ACCESS_TOKEN = tmp_logginData[1]
        self.ACCOUNT_ID = tmp_logginData[2]

    def readLoginData(self, env):
        dirname = os.path.dirname(__file__)
        if not os.path.exists("Account"):
            os.makedirs("Account")
            print("Login file is missing")
            print("Pls create file in folder Account")
        else:
            file = os.path.join(dirname, "Account/" + env + ".txt")
            logginData = []
            with open(file) as f:
                contents = f.readlines()  # API_URL # ACCESS_TOKEN # ACCOUNT_ID
            for line in contents:
                logginData.append(line.rstrip())
            return logginData[0:3]