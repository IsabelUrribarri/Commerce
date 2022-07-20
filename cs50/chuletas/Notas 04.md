Para dar formato a los queries en sqlite3

.mode columns
.headers yes

# Create New Migrations
python manage.py makemigrations

# Migrate
python manage.py migrate