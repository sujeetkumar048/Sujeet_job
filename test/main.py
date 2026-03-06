from helios_python_sdk.services.snowflake_client import SnowflakeClient
import os
import pandas as pd
import gspread
import gspread_dataframe as gd
import json
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
# ---------- Google Sheet Auth ----------
gsheet_creds = os.getenv("sujeet_personal")
creds_json = json.loads(gsheet_creds) if isinstance(gsheet_creds, str) else gsheet_creds
creds = Credentials.from_service_account_info(
    creds_json,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

gc = gspread.authorize(creds)
# ---------- Snowflake ----------
#client = SnowflakeClient()

#----------------------query------------------
#q = """
#select * from table
#"""
#----------------------execution------------------
#result = client.execute_query(sql_query=q)
#if not isinstance(result, pd.DataFrame):
 # df1 = result.to_pandas()

df1="ss"
# ---------- Google Sheet Update ----------
link = "https://docs.google.com/spreadsheets/d/1I6ml4P0wk86W0INCRHs6COtBoiBQqXPN-Z6uag32vxc"
ws1 = gc.open_by_url(link).worksheet("git")
ws1.batch_clear(['A:Y'])
gd.set_with_dataframe(ws1, df1, resize=False, row=1, col=1)
timestamp = (datetime.now() + timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
ws1.update_acell("A1", timestamp)
