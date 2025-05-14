from sqlalchemy import Column, Integer, String, Text, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    shift = Column(String)
    subject = Column(String)
    topic = Column(String)
    question_latex = Column(Text)
    option_a = Column(Text)
    option_b = Column(Text)
    option_c = Column(Text)
    option_d = Column(Text)
    correct_option = Column(String)
    solution_latex = Column(Text, nullable=True)  # Optional field for solutions
    
    # Add constraints
    __table_args__ = (
        CheckConstraint('correct_option IN ("A", "B", "C", "D")'),
        CheckConstraint('year >= 2000 AND year <= 2100'),
    )
    
    def __repr__(self):
        return f"<Question(id={self.id}, subject='{self.subject}', topic='{self.topic}')>"