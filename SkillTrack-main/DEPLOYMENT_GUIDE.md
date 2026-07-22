# Deployment Guide for SkillTrack on Render with Supabase

## Resolving "password authentication failed for user postgres" Error

If you see this error during deployment:
```
django.db.utils.OperationalError: connection to server at "aws-1-ap-south-1.pooler.supabase.com" (3.109.171.244), port 5432 failed: FATAL:  password authentication failed for user "postgres"
```

This means your `DATABASE_URL` environment variable on Render contains an incorrect password.

---

## Step-by-Step Fix

### Step 1: Verify / Reset Your Supabase Database Password
1. Log into your **Supabase Dashboard**
2. Go to **Project Settings** (gear icon at the bottom left)
3. Click on **Database**
4. Under **Database Settings**, look for **Database Password**
5. Click **Reset database password** and enter a new, strong password
6. **Copy this new password immediately**

### Step 2: Grab the Correct Connection String
1. While still in Supabase **Project Settings → Database**, scroll down to **Connection String**
2. Select the **URI** tab
3. Toggle the option to **Transaction or Session pooler mode** (port 6543 is generally recommended for serverless/pooled connections, though 5432 works if using Direct Connection)
4. Copy the connection string. It will look like this:
   ```
   postgresql://postgres.[YOUR-PROJECT-REF]:[YOUR-PASSWORD]@aws-1-ap-south-1.pooler.supabase.com:6543/postgres
   ```
5. Replace `[YOUR-PASSWORD]` in that string with the password you set in Step 1

### Step 3: Update Environment Variables on Render
1. Log into your **Render Dashboard** and open your Web Service
2. Click **Environment** in the left sidebar
3. Find your `DATABASE_URL` environment variable (or create it if it doesn't exist)
4. Update its value with the **full URI string** from Step 2
5. Click **Save Changes**

---

## Required Environment Variables for Render

| Variable | Value | Required |
|----------|-------|----------|
| `DATABASE_URL` | Your Supabase connection string (from Step 2) | **YES** |
| `SECRET_KEY` | Generate a strong key: `python -c "import secrets; print(secrets.token_urlsafe(50))"` | **YES** |
| `DEBUG` | `False` | Yes |
| `ALLOWED_HOSTS` | `.onrender.com,skilltrack-7cin.onrender.com,localhost,127.0.0.1` | Yes |

---

## Render Service Configuration

### Root Directory
```
SkillTrack-main
```

### Build Command
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### Start Command
```bash
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 4
```

---

## Admin Credentials (After Deployment)

After successful deployment, log in with:
- **Email:** `jameslyrech@gmail.com`
- **Password:** `James123!`

The admin user will be created automatically on first login attempt.

---

## Troubleshooting

### If you still get database errors:
1. **Double-check your password** - Make sure there are no extra spaces or special characters
2. **Verify the connection string** - Ensure it uses the correct port (5432 or 6543)
3. **Check Supabase IP restrictions** - In Supabase Database Settings, make sure your Render service's IP is allowed (or disable IP restrictions temporarily)
4. **Test the connection** - Use a tool like `psql` or TablePlus to verify the connection string works

### If migrations fail:
1. The application will automatically fall back to SQLite
2. Make sure `db.sqlite3` can be created in the `SkillTrack-main/` directory
3. Check file permissions on Render

---

## Notes

- The application has **automatic fallback** to SQLite if database connection fails
- This ensures the build succeeds even if Supabase is not properly configured
- However, for production use, you should configure Supabase correctly
