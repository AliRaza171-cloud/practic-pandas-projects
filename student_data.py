import pandas as pd
dd=pd.read_csv(r"C:\Users\hp\Desktop\practic pandas projects\students_performance.csv")
print(dd)
print("\n here we calculate total " \
"number of student")
print(dd['Name'].count())
print("\n here we print how stundent are in each grade mean student per grade")
grouped=dd.groupby('Grade')['StudentID'].count()
print(grouped)
print("\n here we print gender in each grade")
grouped_gender=dd.groupby(['Grade','Gender']).size().unstack(fill_value=0)
print(grouped_gender)
print("\nAverage, minimum, maximum, median, mode, standard deviation of Math, English, Science scores")
statistics_mean=dd[['Math_Score','English_Score','Science_Score']].mean()
print(statistics_mean)
statistics_mode=dd[['Math_Score','English_Score','Science_Score']].mode()
print(statistics_mode)
statistics_median=dd[['Math_Score','English_Score','Science_Score']].median()
print(statistics_median)
statistics_std=dd[['Math_Score','English_Score','Science_Score']].std()
print(statistics_std)
print(dd[['Math_Score','English_Score','Science_Score']].mean().to_frame('Average'))
print(dd.info())
print(dd.shape)
dd['Total_Score']=dd[['Math_Score','English_Score','Science_Score']].sum(axis=1)
print(dd)
print("\n here we print top 5 student from total_score")
top_student=dd.groupby(['StudentID','Name'])['Total_Score'].max().head(5)
print(top_student)
bottum_student=dd.groupby(['StudentID','Name'])['Total_Score'].max().tail(5)
print(bottum_student)
for subject in ['Math_Score','English_Score','Science_Score']:
    topper=dd.loc[dd[subject].idxmax(),['StudentID','Name',subject]]
    print(f'Topper in {subject}')
    print(topper,"\n")
for pass_or_fail in ['Math_Score','English_Score','Science_Score']:
    pass_fail=dd.loc[dd[pass_or_fail]<50,['StudentID','Name',pass_or_fail]]
    print(f'pass_fail,{pass_or_fail}')
    print(pass_fail,"\n")    
for subject1 in ['Math_Score','English_Score','Science_Score']:
    print(f"\n pass percentage in {subject1} by Grade")
    for grade1 in dd['Grade'].unique():
        total_student=len(dd[dd['Grade'] == grade1])
        passed_student=len(dd[(dd['Grade'] == grade1) & (dd[subject1]>=50)])
        percentage_pass=(passed_student/total_student)*100
        print(f"{grade1} in {percentage_pass:.2f}%")
for subject2 in ['Math_Score','English_Score','Science_Score']:
    print(f"\nfail percentafe in {subject2} by Grade")
    for grade2 in dd['Grade'].unique():
        total_student1=len(dd[dd['Grade'] == grade2])
        fail_student2=len(dd[(dd['Grade'] == grade2) & (dd[subject2]<=50)])
        fail_percentage=(fail_student2/total_student1)*100
        print(f"{grade2} in {fail_percentage:.2f}%")
for subject3 in ['Math_Score','English_Score','Science_Score']:
    print(f"pass percentage in {subject3} by gender")
    for gender in dd['Gender'].unique():
        total_student_gender=len(dd[dd['Gender'] == gender])
        pass_student_gender=len(dd[(dd['Gender'] == gender) & (dd[subject3]>=50)])
        percentage_pass_gender=(pass_student_gender/total_student_gender)*100
        print(f"{gender} in {percentage_pass_gender:.2f}%")
for  subject4 in ['Math_Score','English_Score','Science_Score']:
    print(f'fail percentage in {subject4} by gender')
    for gender1 in dd['Gender'].unique():
        total_student_gender1=len(dd[dd['Gender'] == gender1])
        fail_percentage_gender1=len(dd[(dd['Gender'] == gender1) & (dd[subject4]<50)])
        percentage_fail_gender=(fail_percentage_gender1/total_student_gender1)*100
        print(f"{gender1} in {fail_percentage_gender1:.2f}%")
print("\n")
print("\n average score based on gender")
for subject5 in ['Math_Score','English_Score','Science_Score']:
    print(f"average score in {subject5} by gender")
    print("\n")
    for average_gender in dd['Gender'].unique():
        average_score=dd[dd['Gender'] == average_gender][subject5].mean()
        print(f"{average_gender}: {average_score}")        
print("\n")
print("\n using groupby method we calculate avaerage score in 9tth and 12th important point groupby is best practice")
grouped_grade=dd.groupby('Grade')[['Math_Score','English_Score','Science_Score']].mean()
print(grouped_grade.loc[['9th','12th']])
print("\n")
print("\n to print average score in 9th and 12th we another method to do by using for loop")
for gradess in ['9th','12th']:
    average_score_forloop=dd[dd['Grade'] == gradess][['Math_Score','English_Score','Science_Score']].mean()
    print(f"average score {gradess} \n {average_score_forloop}")
print("\n correlation find krna")
correlation = dd['Math_Score'].corr(dd['Science_Score'])
print("\n Correlation beteen math  vs science",correlation)
print("\n derived column analysis") 
for total_score in ['Math_Score','English_Score','Science_Score']:
    total_score1=dd[total_score].sum()
    average_score1=dd[total_score].mean()
    print(f"{total_score}: {total_score1}, Average mean score {average_score1}")

print("\n averger score per grade")
for grade_average in ['9th','10th','11th','12th']:
    grade_data = dd[dd['Grade'] == grade_average]
    average_score_grade = grade_data[['Math_Score','English_Score','Science_Score']].mean().mean()
    print(f"Average score in {grade_average}: {average_score_grade:.2f}")
for grade_max in ['9th','10th','11th','12th']:
    grade_max_score=dd[dd['Grade'] == grade_max]
    max_score=grade_max_score[['Math_Score','English_Score','Science_Score']].max().max()
    print(f"max Score  {grade_max} in {max_score} ")
for countof80 in ['9th','10th''11th','12th']:
    max_count=dd[dd['Grade'] == countof80]
    max_count1=max_count[['Math_Score','English_Score','Science_Score']].count()
    print(f"greater than 80 {countof80} \n {max_count1}")


print("\n top student ki csv file bane gy")
 # first we create datafram 
Top_student=pd.DataFrame(columns=['Subject','StudentID','Name','Score'])
#create loop through subject
for subject7 in ['Math_Score','English_Score','Science_Score']:
    #here we select select toppers
    toppers=dd.loc[dd[subject7].idxmax(),['StudentID','Name',subject7]]
#now we create an empty datafram
    Top_student=pd.concat([Top_student,pd.DataFrame({
        'subject':[subject7],
        'StudentID':[toppers['StudentID']],
        'Name':[toppers['Name']],
        'Score':[toppers[subject7]]
    })], ignore_index=True)
Top_student.to_csv(r"C:\Users\hp\Desktop\top_students.csv", index=False)
print("\n CSV is successfully save")

# creating CSV of faol students
failure_student = pd.DataFrame(columns=['StudentID','Name','Subject','Score'])

for failure in ["Math_Score",'English_Score','Science_Score']:
    # Step 1: Filter students jinke marks < 50 hain
    fail_df = dd.loc[dd[failure] < 50, ['StudentID','Name',failure]]
    
    # Step 2: Rename subject column ko 'Score' karna
    fail_df = fail_df.rename(columns={failure: 'Score'})
    
    # Step 3: Ek new column add karna for subject name
    fail_df['Subject'] = failure
    
    # Step 4: Master dataframe ke saath merge karna
    failure_student = pd.concat(
        [failure_student, fail_df[['StudentID','Name','Subject','Score']]],
        ignore_index=True
    )

# Step 5: Save as CSV
failure_student.to_csv(r"C:\Users\hp\Desktop\failing_students.csv", index=False)
print("\nFailure CSV saved successfully!")

# now we create CSV average grade and gender

avg_per_Grade=dd.groupby('Grade')[['Math_Score','English_Score','Science_Score']].mean().reset_index()
avg_per_Grade.to_csv(r"C:\Users\hp\Desktop\Avg_bt_grade.csv", index=False)

avg_per_Grade=dd.groupby('Gender')[['Math_Score','English_Score','Science_Score']].mean().reset_index()
avg_per_Grade.to_csv(r"C:\Users\hp\Desktop\Avg_bt_gender.csv", index=False)
print("\n both avg by grade and gender are saved successfully")