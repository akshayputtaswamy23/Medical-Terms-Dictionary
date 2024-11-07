# app/routes.py

from flask import render_template, request, jsonify, session, redirect, url_for
import pandas as pd
import os
from app import app

# Initialize session secret key
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Load medical terms from Excel file
def load_medical_terms():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'medical_terms.xlsx')
    try:
        df = pd.read_excel(data_path)
        # Store term, definition, and related terms as a dictionary
        medical_data = {}
        for _, row in df.iterrows():
            related_terms = row['Related Terms'].split(',') if pd.notna(row['Related Terms']) else []
            medical_data[row['Term'].strip().lower()] = {
                'definition': row['Definition'],
                'related_terms': [term.strip() for term in related_terms]
            }
        return medical_data
    except Exception as e:
        print(f"Error loading medical terms: {e}")
        return {}

medical_terms = load_medical_terms()

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term', '').strip().lower()
    result_definition = None
    related_terms = []

    if term in medical_terms:
        result_definition = medical_terms[term]['definition']
        related_terms = medical_terms[term]['related_terms']
        message = f"Definition for '{term.title()}':"
    else:
        message = "No exact match found."
        result_definition = "Definition not found."

    # Find related terms based on partial matching with the search term
    related_terms.extend([t.title() for t in medical_terms if term in t and t != term])

    return render_template(
        'search.html',
        term=term.title(),
        result_definition=result_definition,
        message=message,
        related_terms=related_terms
    )

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '').strip().lower()
    suggestions = [term.title() for term in medical_terms if query in term]
    return jsonify(suggestions)

@app.route('/add_to_favorites', methods=['POST'])
def add_to_favorites():
    term = request.form.get('term', '').strip()
    if 'favorites' not in session:
        session['favorites'] = []
    
    if term not in session['favorites']:
        session['favorites'].append(term)
        session.modified = True
        return jsonify({'message': f"{term} added to favorites."})
    else:
        return jsonify({'message': f"{term} is already in favorites."})

@app.route('/favorites')
def favorites():
    favorites = session.get('favorites', [])
    favorites_with_details = {term: medical_terms.get(term.lower(), None) for term in favorites}
    return render_template('favorites.html', favorites=favorites_with_details)
