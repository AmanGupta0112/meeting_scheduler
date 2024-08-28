# Meeting Scheduler

## Overview

Meeting Scheduler is a Django-based API that allows users to schedule meetings, manage meeting rooms, and handle conflicts in scheduling. It provides a robust backend for a meeting management system, with features including:

- Creating, updating, and deleting meetings
- Managing meeting rooms
- Automatic conflict detection for overlapping meetings
- RESTful API for easy integration with front-end applications

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- PostgreSQL 12+

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/meeting-scheduler.git
   cd meeting-scheduler
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a PostgreSQL database for the project.

2. In the `meeting_scheduler/settings.py` file, update the database configuration:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

3. Apply the database migrations:
   ```
   python manage.py migrate
   ```

4. (Optional) Create a superuser for the Django admin interface:
   ```
   python manage.py createsuperuser
   ```

## Running the Application

To start the development server, run:

```
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

### Meetings

- `GET /api/meetings/`: List all meetings
- `POST /api/meetings/`: Create a new meeting
- `GET /api/meetings/{id}/`: Retrieve a specific meeting
- `PUT /api/meetings/{id}/`: Update a meeting
- `DELETE /api/meetings/{id}/`: Delete a meeting

### Meeting Rooms

- `GET /api/rooms/`: List all meeting rooms
- `POST /api/rooms/`: Create a new meeting room
- `GET /api/rooms/{id}/`: Retrieve a specific meeting room
- `PUT /api/rooms/{id}/`: Update a meeting room
- `DELETE /api/rooms/{id}/`: Delete a meeting room

For detailed information about request and response formats, please refer to the API documentation.

## Contributing

Contributions to the Meeting Scheduler project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code adheres to the project's coding standards and include tests for new features.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.