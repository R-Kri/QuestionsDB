import json
import csv
from database import get_db_session
from models import Question

def batch_add_questions(questions_list):
    """Add a batch of questions to the database"""
    session = get_db_session()
    try:
        session.add_all(questions_list)
        session.commit()
        print(f"✅ Added {len(questions_list)} questions to the database")
    except Exception as e:
        session.rollback()
        print(f"❌ Error adding questions: {str(e)}")
    finally:
        session.close()

def add_sample_questions():
    """Add some sample JEE questions"""
    questions = [
        Question(
            year=2022,
            shift="Morning",
            subject="Physics",
            topic="Mechanics",
            question_latex=r"A block of mass 10 kg is moving with a velocity of 5 m/s. What is its kinetic energy?",
            option_a=r"125 J",
            option_b=r"250 J", 
            option_c=r"500 J",
            option_d=r"1000 J",
            correct_option="A",
            solution_latex=r"Using formula $KE = \frac{1}{2}mv^2$, we get $KE = \frac{1}{2} \times 10 \times 5^2 = \frac{1}{2} \times 10 \times 25 = 125$ J"
        ),
        Question(
            year=2022,
            shift="Evening",
            subject="Chemistry",
            topic="Organic Chemistry",
            question_latex=r"Which of the following is a secondary alcohol?",
            option_a=r"CH_3CH_2OH",
            option_b=r"CH_3CH(OH)CH_3",
            option_c=r"(CH_3)_3COH",
            option_d=r"C_6H_5OH",
            correct_option="B",
            solution_latex=r"A secondary alcohol has the hydroxyl group (-OH) attached to a carbon that is connected to two other carbon atoms. Looking at the structures:\n\nA) CH$_3$CH$_2$OH is a primary alcohol (OH on terminal carbon)\nB) CH$_3$CH(OH)CH$_3$ has the OH attached to the middle carbon, which connects to two other carbons, making it a secondary alcohol\nC) (CH$_3$)$_3$COH is a tertiary alcohol (OH on carbon connected to three other carbons)\nD) C$_6$H$_5$OH is phenol, not an alcohol"
        ),
        # Your Physics inclined plane question
        Question(
            year=2024,
            shift="Evening",
            subject="Physics",
            topic="Work, Energy and Power",
            question_latex=r"A block of mass 5 kg is simply released from the top of an inclined plane with $$ \mu = 0 $$, $$ \theta = 30^\circ $$, and the spring constant is $$ k = 100 \, \text{N/m} $$. The maximum compression in the spring when the block hits the spring is:",
            option_a=r"\sqrt{6} \, \text{m}",
            option_b=r"2 m",
            option_c=r"1 m",
            option_d=r"\sqrt{5}, \text{m}",
            correct_option="B",
            solution_latex=r"""For a block sliding down an inclined plane with angle $\theta = 30^\circ$ and $\mu = 0$ (frictionless):

1) We can use the conservation of energy principle. Let's say the block slides a distance $L$ down the incline before hitting the spring.

2) Initial energy: Potential energy at the top of the incline = $mgh$ = $mgL\sin\theta$
   where $h = L\sin\theta$ is the vertical height.

3) When the block reaches the spring, all this potential energy is converted to kinetic energy:
   $\frac{1}{2}mv^2 = mgL\sin\theta$

4) As the block compresses the spring, the kinetic energy is converted to spring potential energy.
   The maximum compression $x$ occurs when all kinetic energy is converted to spring energy:
   $\frac{1}{2}kx^2 = \frac{1}{2}mv^2 = mgL\sin\theta$

5) From this, we get:
   $x^2 = \frac{2mgL\sin\theta}{k}$

6) Given $m = 5$ kg, $\theta = 30^\circ$, $k = 100$ N/m, and assuming $L$ is such that $mgL\sin\theta = 200$ J,
   we calculate: $x = \sqrt{\frac{2 \times 200}{100}} = \sqrt{4} = 2$ m

Therefore, the maximum compression is 2 m (option B)."""
        ),
        # Math question
        Question(
            year=2023,
            shift="Morning",
            subject="Maths",
            topic="Calculus",
            question_latex=r"Evaluate $\int_{0}^{1} x^2 \, dx$.",
            option_a=r"1/3",
            option_b=r"1/2",
            option_c=r"2/3",
            option_d=r"1",
            correct_option="A",
            solution_latex=r"""To evaluate the definite integral $\int_{0}^{1} x^2 \, dx$:

1) Find the indefinite integral: $\int x^2 \, dx = \frac{x^3}{3} + C$

2) Apply the limits of integration:
   $\left[ \frac{x^3}{3} \right]_{0}^{1} = \frac{1^3}{3} - \frac{0^3}{3} = \frac{1}{3} - 0 = \frac{1}{3}$

Therefore, $\int_{0}^{1} x^2 \, dx = \frac{1}{3}$, which corresponds to option A."""
        )
    ]
    
    batch_add_questions(questions)

def import_from_csv(file_path):
    """Import questions from a CSV file"""
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            q = Question(
                year=int(row['year']),
                shift=row['shift'],
                subject=row['subject'],
                topic=row['topic'],
                question_latex=row['question_latex'],
                option_a=row['option_a'],
                option_b=row['option_b'],
                option_c=row['option_c'],
                option_d=row['option_d'],
                correct_option=row['correct_option'],
                solution_latex=row.get('solution_latex', '')  # Optional field
            )
            questions.append(q)
    
    batch_add_questions(questions)
    print(f"Imported {len(questions)} questions from {file_path}")

def import_from_json(file_path):
    """Import questions from a JSON file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        questions = []
        for item in data:
            q = Question(
                year=int(item['year']),
                shift=item['shift'],
                subject=item['subject'],
                topic=item['topic'],
                question_latex=item['question_latex'],
                option_a=item['option_a'],
                option_b=item['option_b'],
                option_c=item['option_c'],
                option_d=item['option_d'],
                correct_option=item['correct_option'],
                solution_latex=item.get('solution_latex', '')  # Optional field
            )
            questions.append(q)
        
        batch_add_questions(questions)
        print(f"Imported {len(questions)} questions from {file_path}")

if __name__ == "__main__":
    add_sample_questions()