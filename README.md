# Facial Recognition Attendance System

## Project Overview

This project is designed to handle automated attendance marking through facial recognition technology, using a combination of Python, a web framework like Flask, and React Native. The backend is built with Flask, handling facial recognition logic, database management, and API services. OpenCV is used for facial recognition with options for Haar cascades or deep learning models. The frontend is developed in React Native, enabling mobile access for users to register and mark attendance through their device cameras.

### Key Features:

- **User Registration:** Capture facial data and store user profiles.
- **Attendance Marking:** Recognize faces and mark attendance automatically.
- **Attendance Records:** Users can retrieve their attendance history.
- **Database Management:** Use PostgreSQL or MongoDB for storing user information, face encodings, and attendance data.

## Tech Stack

- **Backend:** Python, Flask, OpenCV, PyMongo/SQLAlchemy
- **Frontend:** React Native, react-native-camera/expo-camera
- **Database:** MongoDB/PostgreSQL

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Node.js and npm
- MongoDB or PostgreSQL
- An IDE or text editor of your choice

### Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/suggoooiii/Ai-based-attendance-system.git
cd your-project-directory
```

#### 2. Set Up the Backend

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows | On Linux or macOS use `source venv/bin/activate`

# Install dependencies
pip install Flask opencv-python pymongo sqlalchemy

# Set environment variables
set FLASK_APP=app.py  # Windows | On Linux or macOS use `export FLASK_APP=app.py`
set FLASK_ENV=development  # Windows | On Linux or macOS use `export FLASK_ENV=development`

# Run the Flask app
flask run
```

#### 3. Set Up the Frontend

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the React Native app
npm start
```

#### 4. Database Setup

- **MongoDB:**
  - Ensure MongoDB is installed and running.
  - Configure the connection URI in the backend configuration.
- **PostgreSQL:**
  - Install PostgreSQL and set up a new database.
  - Use SQLAlchemy to integrate with Flask.

### Developing

- **Backend Development:** Modify `app.py` to add more routes or update the facial recognition logic.
- **Frontend Development:** Update React components in the `frontend` directory for handling user interactions.

## Security Measures

- Implement user authentication and authorization.
- Ensure data encryption during storage and transmission.
- Secure API communication channels.
