df[‘Column_Name’] = pd.to_datetime(df[‘Column_Name’], 
 format = ‘%Y-%m-%dT%H:%M:%SZ’, 
 errors = ‘coerce’)
 
 #assertion:
 assert df.Column_Name.isnull().sum() == 0, ‘missing Column dates’
 
 
 
 df[‘Column_Name_year’] = df[‘Column_Name’].dt.year
df[‘Column_Name_month’] = df[‘Column_Name’].dt.month
df[‘Column_Name_week’] = df[‘Column_Name’].dt.week
df[‘Column_Name_day’] = df[‘Column_Name’].dt.day
df[‘Column_Name_hour’] = df[‘Column_Name’].dt.hour
df[‘Column_Name_minute’] = df[‘Column_Name’].dt.minute
df[‘Column_Name_day_of_week’] = df[‘Column_Name’].dt.dayofweek
