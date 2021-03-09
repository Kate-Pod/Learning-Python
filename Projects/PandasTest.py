import pandas as pd
students =pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
students.head() #первые 5 строк
students.describe() #основные описательные статистики

students.iloc[0:5,0:3] #выберем первые 5 строк и 3 столбца
students.iloc[[0,3,10],[-1,-2,-3]] 
students_with_names=students.iloc[[0,3,4,7,8]]
students_with_names.index=['Cercei','Tywin','Joffrey','Ilyn Payne','Gregor'] #дадим имена индексам
student_performance_with_names.loc =['Cercei', 'Joffrey'],['gender', 'writing score']] #выберем данные по индексам и столбцам


#У какой доли студентов из датасэта в колонке lunch указано free/reduced?
students.lunch.loc[students.lunch=='free/reduced'].count()/students.lunch.count()

#Сравним оценки студентов с урезанным ланчем и стандартным по 3 дисциплинам 
students[students.lunch=='standard'].describe()-students[students.lunch=='free/reduced'].describe()

#Переименуем названия столбцов для удобства работы с ними
students=students.rename(columns={'parental level of education': 'parental_level_of_education',
                                            'test preparation course': 'test_preparation_course',
                                            'math score': 'math_score',
                                            'reading score': 'reading_score',
                                            'writing score': 'writing_score'})
students.query("writing_score>74")
