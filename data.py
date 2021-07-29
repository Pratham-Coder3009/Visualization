import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

df = pd.read_csv(r'F:\Python Projects\Visualization\data.csv')
print(df.groupby("level")['attempt'].mean()) 
fig = px.scatter(df, x="student_id", y="level",color="attempt"  )
fig.show()