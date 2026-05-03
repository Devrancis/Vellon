<div align="center">
  <img src="static/images/branding/banner.png" alt="Vellon Banner" width="100%">
  
  # VELLON
  ### The Premium Multi-Vendor Marketplace Solution
  
  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
  [![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Real-time](https://img.shields.io/badge/Real--time-Channels-orange.svg)](https://channels.readthedocs.io/)

  [**Explore the Docs »**](ARCHITECTURE.md)
  
  [**View Demo**](https://vellon.vercel.app) · [**Report Bug**](https://github.com/Devrancis/Vellon/issues) · [**Request Feature**](https://github.com/Devrancis/Vellon/issues)

  **Vellon** is a state-of-the-art multi-vendor marketplace designed for scalability, security, and a premium user experience. It empowers entrepreneurs to build robust digital storefronts with integrated payments, real-time messaging, and sophisticated inventory management.
</div>

---

## 🚀 Features

### 🏪 For Vendors (Stores)
- **Store Management**: Comprehensive dashboard to manage store profiles, settings, and performance.
- **Product Inventory**: Advanced product listing with variants, categories, and high-quality image hosting via Cloudinary.
- **Order Fulfillment**: Streamlined workflow from order placement to delivery tracking.
- **Revenue Analytics**: Real-time insights into sales and customer engagement.

### 🛍️ For Customers
- **Fluid Shopping Experience**: Intuitive search, filtering, and a seamless checkout process.
- **Secure Payments**: Integrated with **Paystack** for safe and reliable transactions.
- **Real-time Messaging**: Instant communication between buyers and sellers powered by Django Channels.
- **Reviews & Ratings**: Transparent feedback system to build trust within the community.
- **Personalized Notifications**: In-app and real-time alerts for order updates and messages.

### 🛠️ Technical Excellence
- **Asynchronous Processing**: Background tasks (emails, notifications, data processing) handled by **Celery** and **Redis**.
- **Real-time Infrastructure**: WebSockets integration for live chat and notifications.
- **Cloud-native Storage**: Seamless media management using **Cloudinary**.
- **Production Ready**: Optimized with Gunicorn, WhiteNoise, and Sentry for monitoring.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Django 4.2
- **API**: Django REST Framework
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Task Queue**: Celery + Redis
- **Real-time**: Django Channels (WebSockets)
- **Frontend**: Django Templates, Bootstrap 5, Crispy Forms
- **Storage**: Cloudinary (Media), WhiteNoise (Static)
- **Monitoring**: Sentry

---

## 🏁 Getting Started

### Prerequisites
- Python 3.10+
- Redis (for Celery and Channels)
- A Cloudinary account (for media storage)
- A Paystack account (for payments)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Devrancis/Vellon.git
   cd Vellon
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://user:password@localhost:5432/vellon
   REDIS_URL=redis://localhost:6379/0
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   PAYSTACK_PUBLIC_KEY=your-public-key
   PAYSTACK_SECRET_KEY=your-secret-key
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Start Celery Worker (in a separate terminal)**
   ```bash
   celery -A vellon worker -l info
   ```

---

## 📂 Project Structure

```text
Vellon/
├── accounts/       # Custom user models and authentication
├── stores/         # Merchant and storefront management
├── products/       # Product listings and inventory
├── orders/         # Cart, checkout, and order tracking
├── messaging/      # Real-time chat system
├── notifications/  # Real-time alerts
├── payments/       # Paystack integration logic
├── reviews/        # Rating and feedback system
├── core/           # Shared utilities and middleware
├── static/         # Global static assets
└── templates/      # Global HTML templates
```

---

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Roadmap

Vellon is continuously evolving. Here are the features currently planned for future releases:

- [ ] **Mobile Application**: Cross-platform mobile app built with React Native/Flutter.
- [ ] **AI-Powered Recommendations**: Personalized product suggestions based on user behavior.
- [ ] **Multi-Currency Support**: Automated currency conversion for international trade.
- [ ] **Advanced Analytics Dashboard**: Deep insights for vendors using D3.js or Chart.js.
- [ ] **Global Search Optimization**: Implementing Elasticsearch for lightning-fast, fuzzy search.
- [ ] **Automated Disputes**: A streamlined system for handling returns and refunds.

---

## 💎 Technical Highlights (Portfolio Focus)

This project was built to demonstrate proficiency in modern web architecture. Key technical challenges addressed include:

- **WebSocket Synchronization**: Implementing a robust messaging system that handles concurrent connections and message delivery guarantees using Django Channels and Redis.
- **Transactional Integrity**: Ensuring that order placements and payment verifications via the Paystack API are atomic and idempotent.
- **Asynchronous Task Management**: Offloading heavy processes like email dispatch and image processing to Celery workers to maintain a snappy UI.
- **Scalable Media Handling**: Using Cloudinary's API for dynamic image transformation and global CDN delivery.

---

## 📬 Contact & Support

If you have any questions about this project or would like to discuss potential opportunities, feel free to reach out!

- **Name**: Francis Iyiola
- **LinkedIn**: https://www.linkedin.com/in/devrancis/
- **Portfolio**: https://devrancis.vercel.app/
- **Email**: francisiyiola.fi@gmail.com

---

<div align="center">
  Built with ❤️ by the Vellon Team
</div>
