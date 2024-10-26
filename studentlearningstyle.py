import pandas as pd

# create a simple data containing student id and their preferred stye alon with scores in various tasks
data = {
    'student_id': [1, 2, 3, 4, 5],
    'resource_1_score': [5, 3, 0, 0, 4],
    'resource_2_score': [4, 0, 0, 0, 5],
    'resource_3_score': [0, 1, 0, 5, 4],
    'preferred_style': ['visual', 'auditory', 'kinesthetic', 'visual', 'auditory'],
}

# create a dataframe of the above data using pandas library
df = pd.DataFrame(data)
df.set_index('student_id', inplace=True)

# using recommend function to identify similar students
def recommend_learning_path(student_id, num_recommendations=2):
    current_student = df.loc[student_id]
    similar_students = df[df['preferred_style'] == current_student['preferred_style']]
    
    recommendations = {}
    for resource in df.columns[:-1]:  # here we exclude the preferred_style
        if current_student[resource] == 0:  # inorder to recommend unrated resources
            avg_rating = similar_students[resource].mean()
            recommendations[resource] = avg_rating

    recommended_resources = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return recommended_resources[:num_recommendations]

# lets illustrate an example for the student with student_id = 4
student_id = 4
recommended_resources = recommend_learning_path(student_id)
print(f"Recommended resources for Student {student_id}: {recommended_resources}")

# here the student 4 and student 1 has similar preferred syle as visual.
# then we look for unrated resource and for student 4, resourse_1_score and resourse_2_score is unrated.
# average resourse_1_score from student 1 and student 4 = 0+5/2 = 2.5
# average resourse_2_score from student 1 and student 4 = 0+4/2 = 2
# since resourse_1_score is of more value, it will be recommended first and then resourse_2_score.

