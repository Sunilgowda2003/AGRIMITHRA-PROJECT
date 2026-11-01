# 🌱 AgriMithra – Integrated Agricultural Platform

AgriMithra is a Django-based agricultural platform designed to support farmers through an online agricultural marketplace, farming education and an AI-powered assistant. It brings useful agricultural resources and shopping features together in one place.

## 🚀 Features

- **Agricultural Marketplace:** Browse agricultural products and view product details.
- **User Accounts:** Customer registration and login.
- **Shopping Cart:** Add products, update quantities and review order totals.
- **Online Payments:** Razorpay payment gateway integration.
- **AI Farming Assistant:** MitraBot helps users with agriculture-related questions using the Google Gemini API.
- **Agricultural Learning:** Tutorials and information about agricultural practices and evolution.
- **Agricultural Resources:** Information about agricultural laws, schemes and success stories.

## 🛠️ Technology Stack

| Area | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Database | SQLite |
| AI Integration | Google Gemini API |
| Payment Integration | Razorpay |
| Image Handling | Pillow |
| Version Control | Git and GitHub |

## 📸 Screenshots

### 🏠 Home Page
![Home Page](Screenshots/home.png)

### 🛍️ Product Catalogue
![Product Catalogue](Screenshots/products.png)

### 🛒 Shopping Cart
![Shopping Cart](Screenshots/cart.png)

### 📝 User Registration
![Registration](Screenshots/registration.png)

### 🔐 User Login
![Login](Screenshots/login.png)

### 🤖 AI Farming Assistant – MitraBot
![MitraBot](Screenshots/chatbot.png)

### 💳 Checkout and Payment
![Payment](Screenshots/payment.png)

### ✅ Payment Confirmation
![Payment Confirmation](Screenshots/payment-confirmation.png)

### 🌿 About Us
![About Us](Screenshots/about-us.png)

### 📚 Agricultural Tutorials
![Tutorials](Screenshots/tutorials.png)

### 🏛️ Agricultural Schemes
![Schemes](Screenshots/schemes.png)

### 🌾 Agricultural Evolution
![Agricultural Evolution](Screenshots/agricultural-evolution.png)

## ⚙️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Sunilgowda2003/AGRIMITHRA-PROJECT.git
cd AGRIMITHRA-PROJECT
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
```

For Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install Dependencies

If your project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_django_secret_key
GOOGLE_GENAI_API_KEY=your_google_gemini_api_key
RAZOR_KEY_ID=your_razorpay_key_id
RAZOR_KEY_SECRET=your_razorpay_key_secret
```

Never commit your `.env` file or expose API keys and secret credentials publicly.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

`http://127.0.0.1:8000/`

## 🔐 Security Notes

- Keep `.env` excluded from Git using `.gitignore`.
- Use your own API credentials in your local environment.
- Do not publish database files containing personal or sensitive user data.
- Use Razorpay test credentials while testing payments.

## 👨‍💻 Author

**Sunil J S**

GitHub: [@Sunilgowda2003](https://github.com/Sunilgowda2003)

---

⭐ If you find this project useful, consider giving the repository a star!