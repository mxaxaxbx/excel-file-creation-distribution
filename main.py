from pathlib import Path

import datetime
import os
import shutil
import pandas as pd
import win32com.client as win32

today_string = datetime.datetime.today().strftime('%m%d%Y_%I%p')
today_string2 = datetime.datetime.today().strftime('%b %d, %Y')

attachment_path = Path.cwd() / 'data' / 'attachments'
archive_dir     = Path.cwd() / 'archive'
src_file        = Path.cwd() / 'data' / 'Example4.xlsx'
df              = pd.read_excel(src_file)

df.head()

customer_group = df.groupby('CUSTOMER_ID')

attachments = []
for ID, group_df in customer_group:
    attachment = attachment_path / f'{ID}_{today_string}.xlsx'

    group_df.to_excel(attachment, index=False)

    attachments.append( ( ID, str(attachment) ) )

df2 = pd.DataFrame( attachments, columns=['CUSTOMER_ID', 'FILE'] )

email_merge = pd.merge( df, df2, how='left' )
combined    = email_merge[ [ 'CUSTOMER_ID', 'EMAIL', 'FILE'] ].drop_duplicates()
