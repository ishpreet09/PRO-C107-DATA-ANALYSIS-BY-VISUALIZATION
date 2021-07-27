import pandas as pd
import plotly.express as px

df= pd.read_csv("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C107DataAnalysisByVisualization/data.csv")

mean=df.groupby(['student_id',"level"], as_index=False)["attempt"].mean()

fig=px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show() 
