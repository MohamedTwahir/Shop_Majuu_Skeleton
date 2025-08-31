# Description
This project serves as a prototype for the shop majuu site. From this the project will advance to the desired level before launch.

# Project Structure
```text
SHOPMAJUU/
├─ backend/
│ ├─ manage.py
│ ├─ backend/ # project settings
│ │ ├─ __init__.py
│ │ ├─ settings.py
│ │ ├─ urls.py
│ │ └─ wsgi.py
│ └─ core/ # main app
│ ├─ __init__.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ emails.py
│ ├─ forms.py
│ ├─ migrations/
│ ├─ models.py
│ ├─ signals.py
│ ├─ tests.py
│ ├─ urls.py
│ ├─ utils.py
│ └─ views.py
├─ templates/
│ ├─ base.html
│ ├─ home.html
│ ├─ profile.html
│ ├─ track.html
│ ├─ package_detail.html
│ └─ emails/
│ ├─ invoice_email.txt
│ └─ invoice_email.html
└─ requirements.txt
```