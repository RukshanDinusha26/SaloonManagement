# Salon Management System

A web-based application for managing salon appointments, employees, and services. Built with Flask (Python) and styled with custom CSS.
<iframe width="560" height="315" src="https://drive.google.com/file/d/1u7obEstmwecpKNqbVL2pRSlFjatGc9Q9/view?usp=drive_link" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Features

*   **User Roles:**
    *   **Admin:** Manage services, employees, and view reports.
    *   **Employee:** Manage assigned appointments.
    *   **Customer:** Browse services, book appointments, and manage profile.
*   **Appointment Booking:** Interactive booking system with real-time availability checking.
*   **Service Management:** Dynamic service list with pricing and images.
*   **Stylist Showcase:** Scrollable view of salon staff.
*   **Account Management:** Profile updates, password changes, and account deletion.
*   **Responsive Design:** Mobile-friendly interface.

## Prerequisites

*   Python 3.8+
*   pip (Python package manager)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd SaloonManagement
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory with the following content:
    ```env
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=sqlite:///site.db
    ADMIN_PASSWORD=admin123
    STRIPE_PUBLIC_KEY=your_stripe_public_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    ```

5.  **Initialize the database:**
    ```bash
    flask db upgrade
    ```

6.  **Seed the database with dummy data:**
    ```bash
    python seed_data.py
    ```

## Usage

1.  **Run the application:**
    ```bash
    python run.py
    ```

2.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Default Credentials

*   **Admin:**
    *   Username: `admin`
    *   Password: `admin123`

*   **Employee:**
    *   Username: `sunil_stylist`
    *   Password: `admin123`

*   **Customer:**
    *   Username: `nimali_client`
    *   Password: `admin123`

## Project Structure

*   `salonManagement/`: Main application package.
    *   `routes.py`: Application routes and logic.
    *   `models.py`: Database models (defined in `__init__.py` in this version).
    *   `templates/`: HTML templates.
    *   `static/`: CSS, JavaScript, and images.
*   `migrations/`: Database migration scripts.
*   `run.py`: Application entry point.
*   `seed_data.py`: Script to populate the database with initial data.


This project is licensed under the MIT License.
