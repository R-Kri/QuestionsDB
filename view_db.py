from database import get_db_session
from models import Question

def view_all_questions():
    session = get_db_session()
    questions = session.query(Question).all()
    session.close()
    
    if not questions:
        print("No questions found in the database.")
        return
    
    print(f"Found {len(questions)} questions in the database:")
    
    for q in questions:
        print(f"\n===== Question {q.id} =====")
        print(f"Subject: {q.subject} - Topic: {q.topic}")
        print(f"Year: {q.year}, Shift: {q.shift}")
        print(f"\nQuestion: {q.question_latex}")
        print(f"\nA) {q.option_a}")
        print(f"B) {q.option_b}")
        print(f"C) {q.option_c}")
        print(f"D) {q.option_d}")
        print(f"\nCorrect Answer: {q.correct_option}")
        
        # Check if solution exists and display it
        if q.solution_latex:
            print(f"\nSolution:")
            print(q.solution_latex)
        else:
            print("\nSolution: Not available")
            
        print("="*30)

if __name__ == "__main__":
    view_all_questions()