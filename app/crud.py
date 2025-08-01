from sqlalchemy.orm import Session
from app import models


# Create a new SearchTerm entry in the database - topic
def create_search_term(db: Session, term: str):
    # Create instance of SearchTerm model
    db_search_term = models.SearchTerm(term=term)
    db.add(db_search_term)
    db.commit()
    db.refresh(db_search_term)
    return db_search_term


# Create a new GeneratedContent entry tied to a search term
def create_search_content(db: Session, content:str, search_term_id: str):
    db_generated_content = models.GeneratedContent(content=content, search_term_id=search_term_id)
    db.add(db_generated_content)
    db.commit()
    db.refresh(db_generated_content)

    return db_generated_content


# Retrieve an existing SearchTerm by its term (string match)
def get_search_term(db: Session, term: str):
    return db.query(models.SearchTerm).filter(models.SearchTerm.term == term).first()


# Create a new SentimentAnalysis entry tied to a search term
def create_sentiment_analysis(db:Session, readability: str, sentiment: str, search_term_id: int):
    db_sentiment_analysis = models.SentimentAnalysis(readability=readability, sentiment=sentiment, search_term_id=search_term_id)
    db.add(db_sentiment_analysis)
    db.commit()
    db.refresh(db_sentiment_analysis)

    return db_sentiment_analysis


# Create a new GeneratedKeywords entry linked to a search term
def create_keywords(db: Session, content:str, search_term_id: int):
    db_keywords = models.GeneratedKeywords(content=content, search_term_id=search_term_id)
    db.add(db_keywords)
    db.commit()
    db.refresh(db_keywords)
    return db_keywords
