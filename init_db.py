#!/usr/bin/env python3
"""
Database initialization script for the URL shortener.
Run this script to create the database tables.
"""

from app import app
from db import db
from models.user import User
from models.link import Link

def init_database():
    """Initialize the database with all tables."""
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        print("Database tables created successfully!")
        
        # Create a test user (optional)
        test_user = User(
            username='admin',
            email='admin@example.com',
            password='pbkdf2:sha256:600000$8gQ8Kq6M$f5c4a4c8a7e7c4a4c8a7e7c4a4c8a7e7c4a4c8a7e7c4a4c8a7e7c4a4c8a7e7'  # password: admin123
        )
        
        try:
            db.session.add(test_user)
            db.session.commit()
            print("Test user created: admin / admin123")
        except Exception as e:
            print(f"Note: Test user already exists or error: {e}")
            db.session.rollback()

if __name__ == '__main__':
    init_database()
