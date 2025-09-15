import pandas as pd
EE=pd.read_csv(r"C:\Users\hp\Desktop\practic pandas projects\employee_data.csv")
print(EE)
print("\n first and last 5 employee data")
print(EE.head(5))
print("\n last 5 employees")
print(EE.tail(5))
print("\n now we find how many rows and column are their")
print(EE.shape)
print("\n here we use infor and describe method to explore")
print(EE.info())
print("\n here we use describe to find stats of data like mean median mode std and etc")
print(EE.describe())
umique=EE[['EmployeeID','Name','Department','Gender','Salary','Performance_Score','Experience','Joining_Date','Leave_Days']].unstack().unique()
print(umique)
print("\n here we calculate how many null values are present in each column ")
value_null=EE.isnull().sum()
print(value_null)
print("\n here we have filled estimated values using interpolate in leave_Days")
inter=EE['Leave_Days'].interpolate(inplace=True)
print(EE)
print("\n here we see how many employees have salary > 50000 ")
high_salary=EE[EE['Salary'] > 50000]
print(high_salary['EmployeeID'])
print("\n Number of employees with salary > 50000 are:",high_salary.shape[0])
print("\n here we print employees whom performance score is less than 40")
P_score=EE[EE['Performance_Score']  < 40]
print(P_score['EmployeeID'])
print("\n employees with Score < 40 are:",P_score.shape[0])
print("\n here we check how many employees belongto hr ot it depart")
for Depart in ['IT','HR']:
    count=EE[EE['Department'] == Depart]
    print(f" employee in depart {Depart} ")
    print(count['EmployeeID'])
    print("\n Total number of employee in HR and IT",count.shape[0])

print("\n here we print salary in asceding and descending order")
ascend=EE.sort_values(by='Salary',ascending=True)
print(ascend)
print("\n salary in desceding")
descend=EE.sort_values(by='Salary',ascending=False)
print(descend)
print("\n here we print top 10 highest salaries")
highest_top=EE.sort_values(by='Salary',ascending=True).head(10)
print(highest_top[['Name','EmployeeID','Salary']])
print("\n here we print bottom 10 salaries")
bottom=EE.sort_values(by='Salary',ascending=False).head(10)
print(bottom[['Name','EmployeeID','Salary']])
print("\n calculate average per Department")
avg_sal=EE.groupby('Department')['Salary'].mean()
print(avg_sal)
print("\n here we peint average performance by department")
avg_per=EE.groupby('Department')['Performance_Score'].mean()
print(avg_per)
print("here we print mean salary by depart and experience")
avg_exp_sal=EE.groupby(['Department','Experience'])['Salary'].mean()
print(avg_exp_sal)
print("\n here we see gender wise average salary ")
print("\n here we going to use aggeratiion function")
avg_sal_performance=EE.groupby('Gender').agg({
    'Salary':'mean',
    'Performance_Score':'mean'
})
print(avg_sal_performance)
print("\n here we covert joining column")
EE['Joining_Date']=pd.to_datetime(EE['Joining_Date'])
earliest_employee=EE.loc[EE['Joining_Date'].idxmin()]
print("\n earliest joining employee data")
print(earliest_employee[['EmployeeID','Name','Joining_Date']])
Today=pd.Timestamp.today()
EE['Tenure']=(Today -EE['Joining_Date']).dt.days/365
EE['Tenure']=EE['Tenure'].clip(lower=0)
print(EE)
print("\m here we print  mean median and std of salaru")
stats_salary=EE['Salary'].agg([
    'mean',
    'median',
    'std'
])
print(stats_salary)
print("\n std of std of salary and performance ")
Std_sal_performance=EE[['Salary','Performance_Score']].agg([
    'std'
])
print(Std_sal_performance)
# we find correlation between salary and performance_Score
print("\n")
corelation=EE['Salary'].corr(EE['Performance_Score'])
print("The corelation between salary and performance_Score",corelation)
# here we created c;oumn bonus and we give to those employee whom perfromance > 80
EE['Bonus']=(EE['Salary']*0.10).where(EE['Performance_Score']>80,0)
print(EE)
EE['Rank_Catagory']=pd.cut(
    EE['Performance_Score'],
    bins=[-1,49,60,80],
    labels=['average','medium','high']
)
print(EE[['EmployeeID','Performance_Score','Rank_Catagory']])
print("\n we count employees rank wise")
print(EE['Rank_Catagory'].value_counts())
print("\n here we make csv files of employees")
# employees who have performace score > 80 are:
top_performer=EE[EE['Performance_Score'] > 80]
top_performer.to_csv(r"C:\Users\hp\Desktop\performace_employees.csv", index=False)
print("\n CSV of > 80 performance is saved successfully")
#here we save employees CSV whom salary < 50000
less_salary=EE[EE['Salary'] < 50000]
less_salary.to_csv(r"C:\Users\hp\Desktop\low_salary_employees.csv", index=False)
print("\n CSV of employees < 50000 salary saved successfully")

dep_avg_sal_perfromance=EE.groupby('Department').agg({
    'Salary':'mean',
    'Performance_Score':'mean'
}).reset_index()
dep_avg_sal_perfromance.to_csv(r"C:\Users\hp\Desktop\Avg_salary and performance.csv",index=False)
print("\n Deptarment wise average salary and performance csv saved successfully")