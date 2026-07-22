# SkillTrack

SkillTrack is a centralized, web-based software platform designed to help students systematically organize, store, and manage their professional certifications, technical skills, and job applications. The system bridges the gap between individual student portfolios and institutional evaluation by providing role-specific dashboards for standard users and staff members.

## Features

- **User Authentication**: Secure registration, login, logout, and lockout security mechanisms.
- **Skill Tracking**: Manage personal technical skills, categorized by technology area and proficiency level.
- **Job Application Tracking**: Track applications sent to companies, statuses (Pending, Interviewing, Offered, Rejected), dates, and required skills.
- **Skill Matching Analysis**: Interactive dashboard comparing your skills list to a job's required skills, giving a percentage match and checklist of missing skills!
- **Administrative Logging**: Activity logging (`AdminLog`) tracking modifications for audit trails.
- **Role-Based Dashboards**:
  - *Standard Users*: Visualization of skill stats, job funnel metrics, and interactive skill matching.
  - *Staff/Admin Users*: Global analytics, user account status manager, and system admin logs.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default) or PostgreSQL (production)
- **Frontend**: HTML5, Vanilla CSS3, Javascript (ES6+)

## Getting Started (Local Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/lyrechjames/SkillTrack-BackUP.git
   cd SkillTrack-BackUP/SkillTrack-main
   ```
2. Set up virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Render Deployment

### Prerequisites
- Render account
- Supabase database (optional, or use SQLite)

### Deployment Steps

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**: `https://github.com/lyrechjames/SkillTrack-BackUP.git`
3. **Set Root Directory**: `SkillTrack-main`
4. **Environment Variables** (MANDATORY):
   ```
   DATABASE_URL=postgresql://postgres.srsoalrumgaodcgpbhqv:YOUR_ACTUAL_PASSWORD@aws-1-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require
   SECRET_KEY=your-strong-secret-key
   DEBUG=False
   ALLOWED_HOSTS=.onrender.com,skilltrack-7cin.onrender.com,localhost,127.0.0.1
   ```
   **IMPORTANT**: Replace `YOUR_ACTUAL_PASSWORD` with your actual Supabase database password from your Supabase dashboard.

5. **Build Command** (auto-filled from `render.yaml`):
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```

6. **Start Command** (auto-filled from `render.yaml`):
   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 4
   ```

7. **Deploy**

### Admin Access
After deployment, log in with:
- **Email**: `jameslyrech@gmail.com`
- **Password**: `James123!`

The admin user will be created automatically on first login attempt.
