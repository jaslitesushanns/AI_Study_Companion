import google.generativeai as genai


def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model


def generate_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text


# 1. Study Plan Generator
def generate_study_plan(model, name, student_class, board, percentage, hours, goal, weak_subjects):

    prompt = f"""
    Create a 7 day study plan for a student.

    Student Name: {name}
    Class: {student_class}
    Board: {board}
    Percentage: {percentage}
    Available Study Hours: {hours}
    Goal: {goal}
    Weak Subjects: {weak_subjects}

    Return ONLY a markdown table.

    Columns:
    | Day | Subject | Topic | Hours |
    """

    return generate_response(model, prompt)



# 2. Smart Timetable
def generate_smart_timetable(model, student_class, hours, weak_subjects):

    prompt = f"""
    Create a smart weekly timetable.

    Class: {student_class}
    Study Hours: {hours}
    Weak Subjects: {weak_subjects}

    Include:
    - Subjects
    - Breaks
    - Revision
    - Weak subject priority

    Return ONLY a markdown table.

    Columns:
    | Time | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
    """

    return generate_response(model, prompt)



# 3. Subject Priority Analyzer
def analyze_subject_priority(model, percentage, weak_subjects, goal):

    prompt = f"""
    Analyze subject priority.

    Current Percentage: {percentage}
    Weak Subjects: {weak_subjects}
    Goal: {goal}

    Give priority ranking and improvement suggestions.
    """

    return generate_response(model, prompt)



# 4. Study Session Planner
def generate_study_session(model, study_hours):

    prompt = f"""
    Create a focused study session.

    Available hours:
    {study_hours}

    Include:
    - Study time
    - Break time
    - Revision time

    Return as a table.
    """

    return generate_response(model, prompt)



# 5. Quiz Generator
def generate_quiz(model, subject, student_class):

    prompt = f"""
    Create a quiz.

    Subject:
    {subject}

    Class:
    {student_class}

    Include:
    - Questions
    - 4 options
    - Correct answer
    """

    return generate_response(model, prompt)



# 6. Progress Tracker
def generate_progress(model, completed_topics, total_topics):

    percentage = (completed_topics / total_topics) * 100

    return f"""
    Progress: {percentage:.2f}%

    Completed Topics:
    {completed_topics}

    Total Topics:
    {total_topics}
    """



# 7. Motivation Generator
def generate_motivation(model, goal):

    prompt = f"""
    Generate motivational message for a student.

    Goal:
    {goal}
    """

    return generate_response(model, prompt)



# 8. AI Study Assistant
def ask_ai(model, question):

    prompt = f"""
    You are an AI Study Assistant.

    Answer this student question:

    {question}

    Explain simply.
    """

    return generate_response(model, prompt)



# Notification
def study_notifications():

    return """
    🔔 Study Reminder:
    
    Keep going!
    Complete your daily study goals.
    """
