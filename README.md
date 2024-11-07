#### Medical Terms Dictionary

This is a simple web-based application that allows users to search for medical terms, view their definitions, see related terms, and save their favorite terms. The app is built using Flask and loads the medical terms and their data from an Excel file.

## Features
**Search for Medical Terms:** Enter a term in the search bar and get the definition, related terms, and the option to add it to your favorites.
**Favorites:** Users can save their favorite terms and view them on a separate page.
**Responsive UI:** The app adapts to different screen sizes for a better user experience.
**Related Terms:** Displays related terms for each medical term.
Technologies Used
**Flask:** Web framework for Python.
**Pandas:** For reading data from the Excel file.
**OpenPyXL:** To handle Excel files (.xlsx).
**HTML/CSS:** For front-end design.
**Bootstrap:** For responsive UI (if you decide to use it).
Setup Instructions
Follow the steps below to set up the project on your local machine.

## 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/medical-terms-dictionary.git
```
```bash
cd medical-terms-dictionary
```
## 2. Set Up Virtual Environment
Create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv venv
```

# Activate the virtual environment
**For macOS/Linux**
```bash
source venv/bin/activate
```
**For Windows**
```bash
venv\Scripts\activate
```
## 3. Install Dependencies
Install the required Python packages from requirements.txt:
```bash
pip install -r requirements.txt
```

## 4. Add Your Excel File
Place your Excel file containing medical terms in the project directory. The file should have the following columns:

**term:** The medical term.

**definition:** The definition of the term.

**related_terms:** A comma-separated list of related terms.
**Example structure:**

term          |  definition                         |	    related_terms
Hypertension  |	High blood pressure	                |Blood pressure, Cardiovascular

Name the file medical_terms.xlsx and place it in the project’s root folder.

## 5. Run the Application
To run the application, execute the following command:
```bash
python app.py
```
This will start the Flask development server. You can access the app at http://127.0.0.1:5000/.

## 6. Using the Application
**Search:** Enter a medical term in the search bar to view its definition and related terms.
**Favorites:** Click on the "Add to Favorites" button to save a term to your favorites list. You can view and manage your favorites from the "Favorites" page.
**Related Terms:** When you search for a term, you’ll also see related terms displayed below the definition.
**Back to Home:** On the favorites page, you can click the "Back to Home" button to navigate back to the search page.

## How the Application Works
**Loading Medical Terms:** The app reads medical terms from an Excel file (medical_terms.xlsx) using pandas. The terms include their definition and related terms.

**Search Functionality:** When a user types a term in the search box, the app searches for matching terms from the loaded data. It displays the term's definition and related terms.

**Favorites:** Users can save terms they like by clicking the "Add to Favorites" button. These terms are stored in the session and can be viewed on the "Favorites" page.

**Responsive UI:** The app uses Bootstrap for a responsive design, ensuring it works well on both mobile and desktop screens.

## **Additional Notes**
**Error Handling:** Basic error handling is implemented in the app to handle cases where a term is not found or an invalid request is made.
**Case Insensitive Search:** The search functionality is case-insensitive, meaning you can search for terms in any case.

## Screenshots 
<img width="1440" alt="Screenshot 2024-11-07 at 4 46 28 PM" src="https://github.com/user-attachments/assets/65370a14-120e-4a91-b279-45d5548f47bb">
![Screenshot 2024-11-07 at 4 46 18 PM](https://github.com/user-attachments/assets/391fe2f5-cde9-4cc3-9662-142b8eca1a64)
<img width="1440" alt="Screenshot 2024-11-07 at 4 46 11 PM" src="https://github.com/user-attachments/assets/d82ac3ea-ae72-4416-9bb4-5356bf35127a">
<img width="1440" alt="Screenshot 2024-11-07 at 4 46 06 PM" src="https://github.com/user-attachments/assets/fd6cfcb6-e934-4440-bbca-f2b567ee3910">
<img width="1440" alt="Screenshot 2024-11-07 at 4 45 57 PM" src="https://github.com/user-attachments/assets/e7449e80-174e-4d5d-9f1c-9dd69e4c899f">

