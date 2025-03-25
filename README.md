# Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/j0hanz/dj-template.git .
```
> The trailing `.` tells Git to clone into your **current directory**.

## 2️⃣ Configure Environment Variables
Create a `.env` file in the project root containing:

```dotenv
SECRET_KEY=your_secret_key
DEV=any_value
DATABASE_URL=your_database_url
CLOUDINARY_NAME=your_cloudinary_name
CLOUDINARY_KEY=your_cloudinary_key
CLOUDINARY_SECRET=your_cloudinary_secret
```
- **SECRET_KEY**: any secure random string
- **DEV**: enables Django’s debug mode for local development (set any value, e.g., `1`, to enable it)
- **DATABASE_URL**: the URL of your database (leave `DEV` unset to connect to this database)
- **CLOUDINARY_NAME**: your Cloudinary cloud name
- **CLOUDINARY_KEY**: your Cloudinary API key
- **CLOUDINARY_SECRET**: your Cloudinary API secret

## 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

- Visit http://127.0.0.1:8000 in your browser to see the app live.
