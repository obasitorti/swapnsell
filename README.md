# SwapNSell

SwapNSell is a Django-based web application for listing, selling, and swapping items.  
It integrates AWS S3 for media storage, allowing you to store and serve uploaded images directly from an Amazon S3 bucket.

---

## Features

- User registration and authentication
- Post items for sale or swap
- Upload item images (stored in AWS S3)
- Browse and search for items
- Responsive UI for desktop and mobile
- Admin dashboard for content management

---

## Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv
- AWS account with an S3 bucket configured

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/obasitorti/swapnsell.git
   cd swapnsell


2. **Create a virtual environment**
    ```bash
    python -m venv venv

3. **Activate the virtual environment**
    #### Windows
    venv\Scripts\activate

    #### macOS/Linux
    source venv/bin/activate

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt

5. **Configure environment variables**
    Create a .env file in the project root and add:

    SECRET_KEY=your-django-secret-key
    DEBUG=True
    AWS_ACCESS_KEY_ID=your-aws-access-key
    AWS_SECRET_ACCESS_KEY=your-aws-secret-key
    AWS_STORAGE_BUCKET_NAME=your-s3-bucket-name

6. **Run migrations**
    ```bash
    python manage.py migrate

7. **Create a superuser**
    ```bash
    python manage.py createsuperuser

8. **Run the development server**
    ```bash
    python manage.py runserver

## Usage
### Posting an Item

    Log in or register.

    Click Post Item.

    Fill in details and upload an image.

    Submit — the image will be stored in AWS S3 and served directly from the bucket.

### Browsing Items

    Visit the homepage to see all listed items.

    Use the search bar to filter results.

### Admin Management

    Visit /admin and log in with your superuser account.

    Manage items, users, and site settings.


## Deployment

For production deployment:

    Set DEBUG=False in .env

    Use a production-ready server like Gunicorn or uWSGI

    Configure a domain and HTTPS