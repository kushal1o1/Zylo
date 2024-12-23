# ZYLO - Multi-purpose Landing Website

## 📄 Project Overview

**ZYLO** is a versatile, multi-purpose landing website that can serve various use cases:

- Personal portfolios
- Business or company landing pages
- Hotels, restaurants, and local businesses
- A consolidated site for all your social media and web links

ZYLO is built using Django and Tailwind CSS to create a professional and responsive website with an easy-to-manage backend.

---

## 🚀 Key Features

- **User Authentication**: Secure login and profile management.
- **Profile Management**: Edit profile details, social links, bio, and upload images.
- **Highlights Section**: Add up to 7 highlights with automatic management (oldest is deleted when the limit is reached).
- **Dynamic Sections**: Add content sections for services, projects, or any other information.
- **Responsive Design**: Mobile-friendly with Tailwind CSS.
- **Media Uploads**: Upload images for highlights, sections, and profiles.

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite (default), can switch to PostgreSQL/MySQL
- **Deployment**: Hosted on [zylo.pythonanywhere.com](https://zylo.pythonanywhere.com)

---

## 📦 Installation Guide

### Prerequisites

Ensure you have installed:

- Python 3.x
- `pip`
- `virtualenv`

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/zylo.git
cd zylo
```
### Step 2: Create and Activate Virtual Environment

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

Your development server should now be running at `http://127.0.0.1:8000/`.

---

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For any inquiries or issues, please contact us at [kushalbarl101@gmail.com](mailto:kushalbaral101@gmail.com).