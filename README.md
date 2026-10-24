# Expense Tracker

A simple expense tracking web application built with Django and Python. It helps users keep track of their income, expenses, and current balance in one place.

## About the Project

The Expense Tracker provides a dashboard where users can view their financial summary and manage their transaction history. Users can add transactions by entering a description and amount, view previously recorded transactions, and delete entries when needed.

The dashboard displays the current balance, total income, and total expenses based on the transaction data handled by the application.

## Technologies Used

- **Python** – Handles the application's backend logic and financial calculations.
- **Django** – Manages URL routing, views, database operations, form submissions, and template rendering.
- **HTML** – Structures the dashboard, transaction history, and input form.
- **CSS** – Styles the dashboard, form fields, transaction list, and layout.
- **Django Templates** – Display dynamic data from the backend and reuse common page layouts through template inheritance.
- **Database** – Stores transaction records using Django's database layer and models.

## Features

- View current balance, total income, and total expenses.
- Add transactions with a description and amount.
- View transaction history.
- Delete existing transactions.
- Display updated financial information using backend calculations.
- Use a shared base template for a consistent page layout.

## How It Works

1. **Dashboard:** When a user opens the application, Django processes the request and renders the dashboard with the current balance, income, expenses, and transaction history.

2. **Adding a transaction:** The user enters a description and amount in the form and submits it using a POST request. Django processes the submitted data and saves the transaction through the application's backend and database layer.

3. **Updating the summary:** The backend calculates the financial totals from the stored transactions and passes the results to the template for display.

4. **Viewing history:** The dashboard retrieves existing transaction records and displays their descriptions and amounts.

5. **Deleting a transaction:** The user selects the delete option for a transaction, and Django handles the corresponding request to remove that record.

## Project Structure

```text
expense_tracker/
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── public/
│       └── static/
│           └── css/
│               └── style.css
├── tracker/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   └── base.html
|   └── index.html
├── manage.py
└── README.md
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd expense_tracker
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv env_site
source env_site/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Purpose

This project is a practical exercise in building a Django web application, working with database-backed records, handling form submissions, rendering dynamic templates, and connecting frontend components with backend logic.
