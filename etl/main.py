from generate_data import generate_dates
from load_data import load_dates

dates_df = generate_dates(365)

load_dates(dates_df)