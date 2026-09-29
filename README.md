# College Event Management System with CI/CD

An academic demonstration project illustrating the complete **DevOps Lifecycle** using a clean, beginner-friendly Python Flask web application, SQLite database, PyTest automated testing, Docker containerization, and GitHub Actions CI/CD pipeline.

---

## 1. Project Objective

The primary objective of this project is to **demonstrate modern DevOps practices and continuous integration/continuous deployment (CI/CD)** rather than building an overwhelmingly complex web application. It showcases how code moves reliably from local development to automated testing, container packaging, and deployment readiness.

---

## 2. Features

The application includes three essential, easy-to-demonstrate features:

1. **View Events**: Displays all scheduled events with ID, title, date, venue, and description in responsive cards.
2. **Add Event**: Form allowing users to enter and store new college events into SQLite.
3. **Delete Event**: Immediate removal of an event by ID upon clicking the Delete button.

> **Note**: No login or complicated authentication is required, keeping the project 100% focused on DevOps and CI/CD demonstration.

---

## 3. Technology Stack

* **Programming Language**: Python 3.11+
* **Web Framework**: Flask
* **Database**: SQLite (built-in via Python `sqlite3`)
* **Frontend**: HTML5 & Vanilla CSS (responsive, modern, clean)
* **Testing**: PyTest
* **Containerization**: Docker
* **Version Control**: Git & GitHub
* **CI/CD Automation**: GitHub Actions

---

## 4. Folder Structure

```text
college-event-management/
│
├── app.py                     # Main Flask web application & SQLite logic
├── requirements.txt           # Project dependencies (Flask, pytest)
├── Dockerfile                 # Container image specification
├── .dockerignore              # Files ignored by Docker build
├── .gitignore                 # Files excluded from Git tracking
├── README.md                  # Complete project documentation
│
├── templates/
│   └── index.html             # Single-page UI for view, add, delete
│
├── static/
│   └── style.css              # Clean, modern responsive styling
│
├── tests/
│   └── test_app.py            # Automated tests using PyTest & temporary DB
│
└── .github/
    └── workflows/
        └── ci-cd.yml          # GitHub Actions CI/CD workflow configuration
```

---

## 5. Prerequisites

Before running the project, ensure you have the following installed:

* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Optional for Docker step)
* [Visual Studio Code](https://code.visualstudio.com/)

---

## 6. Installation

1. Open a terminal or VS Code in the project directory:
   ```bash
   cd college-event-management
   ```

2. (Recommended) Create and activate a Python virtual environment:
   * **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD)**:
     ```cmd
     python -m venv venv
     .\venv\Scripts\activate.bat
     ```
   * **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 7. Running Locally

Start the Flask application:

```bash
python app.py
```

Open your browser and navigate to:
```text
http://127.0.0.1:5000
```

The database (`events.db`) is automatically initialized with sample college events when first launched.

---

## 8. Running Automated Tests

Run the PyTest test suite:

```bash
pytest
```

or for verbose output:

```bash
pytest -v
```

All 4 test cases will execute against an isolated temporary database:
1. `test_app_starts`
2. `test_home_page_returns_200`
3. `test_add_event`
4. `test_delete_event`

---

## 9. Running with Docker

1. **Build the Docker container image**:
   ```bash
   docker build -t college-events .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 college-events
   ```

3. Open your browser at:
   ```text
   http://localhost:5000
   ```

To stop the container, press `Ctrl + C` or stop it via Docker Desktop.

---

## 10. Git Commands & Repository Setup

Initialize Git and push the project to your GitHub repository:

```bash
# 1. Initialize git
git init

# 2. Stage all files
git add .

# 3. Create initial commit
git commit -m "Initial project commit"

# 4. Rename default branch to main
git branch -M main

# 5. Add your remote GitHub repo (Replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 6. Push to GitHub
git push -u origin main
```

---

## 11. GitHub Actions (CI/CD Pipeline)

The workflow file is located at `.github/workflows/ci-cd.yml`.

Whenever code is pushed to the `main` branch or a pull request is created:
1. **Checkout Code**: Retrieves the repository source code.
2. **Setup Python**: Configures Python 3.11 environment.
3. **Install Dependencies**: Installs packages listed in `requirements.txt`.
4. **Run PyTest**: Executes the 4 automated unit tests.
5. **Docker Build**: Builds the Docker container to ensure containerizability.
6. **Continuous Deployment**: Triggers a production deployment webhook if configured.

If any test fails, the pipeline automatically halts and flags the build as failed.

---

## 12. CI/CD Explanation

* **Continuous Integration (CI)**: Automates the validation of code changes. Every push automatically executes tests and verifies Docker builds, preventing broken code from entering main branch.
* **Continuous Deployment (CD)**: Automatically deploys the validated application artifact to production without human intervention once all CI stages succeed.

---

## 13. DevOps Lifecycle

```text
Plan → Code → Build → Test → Release
 ↑                              ↓
Feedback ← Monitor ← Operate ← Deploy
```

1. **Plan**: Define requirements for managing events (View, Add, Delete).
2. **Code**: Write minimal, clean Python/Flask code and HTML/CSS.
3. **Build**: Package code, install dependencies, and build Docker image.
4. **Test**: Execute automated PyTest suite on every commit.
5. **Release**: Tag and push verified code to GitHub repository.
6. **Deploy**: Push Docker image or trigger cloud webhook for hosting.
7. **Operate**: Serve user requests with zero downtime.
8. **Monitor**: Inspect GitHub Actions job logs, Flask request logs, and container status.
9. **Feedback**: Review issues, iterate code, and push fixes through the same pipeline.

---

## 14. Deployment

For free and easy cloud deployment suitable for college projects:
* **Platform**: [Render](https://render.com) or [Railway](https://railway.app).
* **Setup**:
  1. Create a Web Service connected to your GitHub repo on Render.
  2. Copy your **Deploy Hook URL** from Render dashboard.
  3. In GitHub, go to **Settings** > **Secrets and variables** > **Actions**.
  4. Create a repository secret named `DEPLOY_WEBHOOK_URL` and paste the URL.
  5. Future pushes to `main` will automatically trigger fresh deployments!

---

## 15. Live Demonstration Procedure

1. **Run Locally**: Execute `python app.py` and open `http://127.0.0.1:5000`.
2. **Add Event**: Fill the form ("Tech Fest 2026", date, venue) and submit.
3. **Delete Event**: Click Delete on an event to verify database operations.
4. **Run PyTest**: Execute `pytest -v` in terminal to show 4 passing tests.
5. **Docker Demo**: Run `docker build -t college-events .` and `docker run -p 5000:5000 college-events`.
6. **Trigger CI/CD**: Edit a title or text in `templates/index.html`, commit and push to GitHub (`git push`).
7. **Show GitHub Actions**: Open the GitHub repository **Actions** tab to show live green checkmarks for checkout, tests, Docker build, and deployment.

---

## 16. Future Enhancements

* Role-based access control (Admin vs Student).
* Event registration and RSVP system with email confirmations.
* Container orchestration using Kubernetes (Minikube).
* Monitoring with Prometheus and Grafana dashboards.

---

## 17. Conclusion

This project successfully demonstrates an end-to-end DevOps workflow for an academic environment. By focusing on essential features and automated tooling, it provides a clear, practical, and defensible demonstration of modern software delivery practices.
