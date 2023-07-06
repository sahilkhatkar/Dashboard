# Dashboard

How to deploy on vercel

Step - 1
# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic

Step - 2
{
  "version": 2,
  "builds": [
    {
      "src": "projectname/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles_build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "projectname/wsgi.py"
    }
  ]
}

Step - 3
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
&&
ALLOWED_HOSTS = ['.vercel.app', '.now.sh']
&&
Comment the databases content

Step - 4
python manage.py makemigrations
python manage.py migrate

Step - 5
app = application
