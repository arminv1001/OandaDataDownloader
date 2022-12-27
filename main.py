import loginData
import datetime
from datetime import date,timedelta
from dataManager import getHistoricalData

# read in account
loginClass = loginData.LoginData("live")
# select asset
asset = input("Select asset")
# select timeframe
timeframe = input("Select timeframe")

# startYear = input("Start year")
# startMonth  = input("Start month")
# startDay = input("Start day")
# start_date = startDay+"-"+startMonth+"-"+startYear
# endYear = input("End year")
# endMonth  = input("End month")
# endDay = input("End day")
# end_date = endDay+"-"+endMonth+"-"+endYear

timeDelay = input("How many days")

start_date = date.today()
end_date = start_date - timedelta(days=int(timeDelay))

# get data
getHistoricalData(end_date,start_date,asset,loginClass.ACCESS_TOKEN,loginClass.ACCOUNT_ID,loginClass.API_URL,timeframe ).to_csv("Data/"+timeframe+"-"+asset+".csv")

 