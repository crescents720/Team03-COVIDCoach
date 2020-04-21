import requests

headers = {
	'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
	'x-rapidapi-key': "4d79bf1779msh12322835c66a566p1dc930jsnaa9f4295d835"
}


#Get latest data for whole world.
url_Totals = "https://covid-19-data.p.rapidapi.com/totals"
querystring_Totals = {"format":"json"}
response_Totals = requests.request("GET", url_Totals, headers=headers, params=querystring_Totals)


#Get daily report data for the whole world.
url_DailyReportTotals = "https://covid-19-data.p.rapidapi.com/report/totals"
querystring_DailyReportTotals = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-01"}
response_DailyReportTotals = requests.request("GET", url_DailyReportTotals, headers=headers, params=querystring_DailyReportTotals)


#Get latest data for specific country. (in this case, USA)
url_USA = "https://covid-19-data.p.rapidapi.com/country"
querystring_USA = {"format":"json","name":"USA"}
response_USA = requests.request("GET", url_USA, headers=headers, params=querystring_USA)

#Get a daily report for a specific country by country name. 
#Parameters name and date are mandatory.
url_USA_daily = "https://covid-19-data.p.rapidapi.com/report/country/name"
querystring_USA_daily = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-01","name":"USA"}
response_USA_daily = requests.request("GET", url_USA_daily, headers=headers, params=querystring_USA_daily)

#Get a list of name for every country for reference
url_listOfCountries = "https://covid-19-data.p.rapidapi.com/help/countries"
querystring_listOfCountries = {"format":"json"}
response_listOfCountries = requests.request("GET", url_listOfCountries, headers=headers, params=querystring_listOfCountries)


print("Latest data for whole world: ")
print(response_Totals.text)
print("\n\n")

print("Daily report data for the whole world: ")
print(response_DailyReportTotals.text)
print("\n\n")

print("Latest data for USA: ")
print(response_USA.text)
print("\n\n")

print("Daily report for USA: ")
print(response_USA_daily.text)
print("\n\n")

