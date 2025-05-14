from database import get_db_session
from models import Question

def interactive_add_question():
    """Add a question through interactive prompts"""
    print("=== Add New JEE Question ===")
    
    try:
        year = int(input("Year (e.g., 2023): "))
        shift = input("Shift (Morning/Evening): ")
        subject = input("Subject (Physics/Chemistry/Maths): ")
        topic = input("Topic: ")
        
        print("Enter question in LaTeX format:")
        question_latex = input("> ")
        
        print("Enter option A:")
        option_a = input("> ")
        
        print("Enter option B:")
        option_b = input("> ")
        
        print("Enter option C:")
        option_c = input("> ")
        
        print("Enter option D:")
        option_d = input("> ")
        
        correct_option = input("Correct option (A/B/C/D): ").upper()
        
        if correct_option not in ["A", "B", "C", "D"]:
            print("❌ Error: Correct option must be A, B, C, or D")
            return
        
        # Solution is optional
        solution_latex = None
        add_solution = input("Would you like to add a solution? (y/n): ").lower()
        if add_solution == 'y':
            print("Enter solution in LaTeX format:")
            solution_latex = input("> ")
        
        q = Question(
            year=year,
            shift=shift,
            subject=subject,
            topic=topic,
            question_latex=question_latex,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option,
            solution_latex=solution_latex
        )
        
        session = get_db_session()
        session.add(q)
        session.commit()
        print(f"✅ Question added successfully! (ID: {q.id})")
        session.close()
        
    except ValueError:
        print("❌ Invalid input. Year must be a number.")
    except Exception as e:
        print(f"❌ Error adding question: {str(e)}")

if __name__ == "__main__":
    while True:
        interactive_add_question()
        if input("\nAdd another question? (y/n): ").lower() != 'y':
            break