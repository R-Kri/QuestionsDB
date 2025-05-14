from database import get_db_session
from models import Question

def search_questions(subject=None, topic=None, year=None):
    """Search for questions with filters"""
    session = get_db_session()
    query = session.query(Question)
    
    if subject:
        query = query.filter(Question.subject == subject)
    if topic:
        query = query.filter(Question.topic == topic)
    if year:
        query = query.filter(Question.year == year)
    
    results = query.all()
    session.close()
    return results

def get_question_by_id(question_id):
    """Get a specific question by ID"""
    session = get_db_session()
    question = session.query(Question).filter(Question.id == question_id).first()
    session.close()
    return question

def get_stats():
    """Get database statistics"""
    session = get_db_session()
    
    total_questions = session.query(Question).count()
    subjects = session.query(Question.subject, 
                           session.query(Question).filter(
                               Question.subject == Question.subject
                           ).count()).group_by(Question.subject).all()
    
    years = session.query(Question.year,
                        session.query(Question).filter(
                            Question.year == Question.year
                        ).count()).group_by(Question.year).all()
    
    session.close()
    
    print(f"Total Questions: {total_questions}")
    print("\nBreakdown by Subject:")
    for subject, count in subjects:
        print(f"  - {subject}: {count}")
    
    print("\nBreakdown by Year:")
    for year, count in years:
        print(f"  - {year}: {count}")

def display_questions(questions, show_solutions=True):
    """Display a list of questions in a formatted way"""
    if not questions:
        print("No questions found!")
        return
    
    for i, q in enumerate(questions):
        print(f"\n===== Question {i+1} =====")
        print(f"ID: {q.id}")
        print(f"Subject: {q.subject} - Topic: {q.topic}")
        print(f"Year: {q.year}, Shift: {q.shift}")
        print(f"\nQuestion: {q.question_latex}")
        print(f"\nA) {q.option_a}")
        print(f"B) {q.option_b}")
        print(f"C) {q.option_c}")
        print(f"D) {q.option_d}")
        print(f"\nCorrect Answer: {q.correct_option}")
        
        if show_solutions and q.solution_latex:
            print(f"\nSolution:")
            print(q.solution_latex)
        
        print("="*30)