from database import get_db_session
from models import Question
from data_entry import interactive_add_question
from query_utils import search_questions, get_stats, display_questions
from seed_data import add_sample_questions, import_from_csv, import_from_json

def main_menu():
    """Main menu for the JEE Questions Database application"""
    while True:
        print("\n=== JEE Questions Database ===")
        print("1. Add a question interactively")
        print("2. View all questions")
        print("3. Search questions")
        print("4. Database statistics")
        print("5. Add sample questions")
        print("6. Import from CSV")
        print("7. Import from JSON")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ")
        
        if choice == '1':
            interactive_add_question()
        
        elif choice == '2':
            session = get_db_session()
            questions = session.query(Question).all()
            session.close()
            display_questions(questions)
        
        elif choice == '3':
            subject = input("Subject (leave blank for all): ")
            topic = input("Topic (leave blank for all): ")
            year_str = input("Year (leave blank for all): ")
            
            year = int(year_str) if year_str.isdigit() else None
            
            questions = search_questions(
                subject=subject if subject else None,
                topic=topic if topic else None,
                year=year
            )
            
            display_questions(questions)
        
        elif choice == '4':
            get_stats()
        
        elif choice == '5':
            add_sample_questions()
        
        elif choice == '6':
            file_path = input("Enter path to CSV file: ")
            try:
                import_from_csv(file_path)
            except Exception as e:
                print(f"Error importing CSV: {str(e)}")
        
        elif choice == '7':
            file_path = input("Enter path to JSON file: ")
            try:
                import_from_json(file_path)
            except Exception as e:
                print(f"Error importing JSON: {str(e)}")
        
        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()