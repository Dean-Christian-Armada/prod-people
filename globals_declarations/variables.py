import datetime

_today = datetime.date.today()
today = _today.strftime("%Y-%m-%d")
now = datetime.datetime.now()
fileformat_today = str(_today).replace('-', '')

# These variables are imported inside a request method in the views
crew_on_table = 10
per_page_list = [10, 25, 50, 100]