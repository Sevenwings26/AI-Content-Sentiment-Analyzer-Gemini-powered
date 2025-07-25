from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SearchTerm(Base):
    __tablename__ = "search_terms"
    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, index=True)
    generated_content = relationship("GeneratedContent", back_populates="search_term")
    sentiment_analysis = relationship("SentimentAnalysis", back_populates="search_term")
    generated_keywords = relationship("GeneratedKeywords", back_populates="search_term")


class GeneratedContent(Base):
    __tablename__ = "generated_content"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    search_term_id = Column(Integer, ForeignKey('search_terms.id'))
    search_term = relationship("SearchTerm", back_populates="generated_content")


class SentimentAnalysis(Base):
    __tablename__ = "sentiment_analysis"
    id = Column(Integer, primary_key=True, index=True)
    readability = Column(String)
    sentiment = Column(String)
    search_term_id = Column(Integer, ForeignKey('search_terms.id'))
    search_term = relationship("SearchTerm", back_populates="sentiment_analysis")

class GeneratedKeywords(Base):
    __tablename__ = "generated_keywords"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    search_term_id = Column(Integer, ForeignKey('search_terms.id'))
    search_term = relationship("SearchTerm", back_populates="generated_keywords")

