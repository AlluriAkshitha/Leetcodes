import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    
    column_mapping = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
    
    
    students.rename(columns=column_mapping, inplace=True)
    
    return students
