# Nigerian Music Distribution Platform

A comprehensive Django-based music distribution platform designed specifically for Nigerian artists and labels to distribute their music worldwide while keeping 100% of their royalties.

## Features

### Core Features
- **User Management**: Custom user model with artist and label profiles
- **Music Upload**: Complete release management with track handling
- **Global Distribution**: Integration-ready for 200+ music platforms
- **Royalty Tracking**: Comprehensive analytics and earnings management
- **Withdrawal System**: Secure payment processing for artists
- **Support System**: Built-in ticketing system for customer support

### User Types
- **Artists**: Individual musicians and performers
- **Labels**: Music labels managing multiple artists

### Subscription Plans
- **Free Plan**: Basic features for getting started
- **Artiste Plan**: ₦5,000 per release with full distribution
- **Artist Plus**: ₦15,000/month for unlimited releases with advanced features

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to: `http://127.0.0.1:8000`

## Project Structure

```
project/
├── accounts/              # User management and authentication
├── analytics/             # Royalty reports and analytics
├── core/                  # Core functionality and landing pages
├── distribution/          # Music upload and distribution
├── support/              # Customer support system
├── music_platform/      # Main Django project settings
├── templates/            # HTML templates
├── static/              # CSS, JS, and static assets
├── manage.py
└── requirements.txt
```

## Key Models

### Accounts App
- **CustomUser**: Extended user model with account types and plans
- **ArtistProfile**: Artist-specific information
- **LabelProfile**: Label-specific information

### Distribution App
- **Release**: Music releases (singles, albums, EPs)
- **Track**: Individual tracks within releases
- **Platform**: Music streaming/download platforms
- **Distribution**: Track distribution status across platforms

### Analytics App
- **RoyaltyReport**: Earnings and stream data
- **Withdrawal**: Payment withdrawal requests

### Support App
- **SupportTicket**: Customer support tickets

## URL Structure

- `/` - Home page
- `/accounts/signup/` - User registration
- `/accounts/login/` - User login
- `/accounts/dashboard/` - User dashboard
- `/distribution/upload/` - Music upload
- `/distribution/releases/` - Release management
- `/analytics/royalties/` - Royalty dashboard
- `/pricing/` - Pricing information
- `/about/` - About page
- `/contact/` - Contact page

## Configuration

### Environment Variables (for production)
Create a `.env` file with:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

### Media Files
Configure your media storage for handling audio files and cover art:
- Development: Files stored locally in `media/` directory
- Production: Consider cloud storage (AWS S3, etc.)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up SSL certificate
6. Configure email backend
7. Set up monitoring and logging

### Recommended Hosting
- **Backend**: Heroku, DigitalOcean, AWS
- **Database**: PostgreSQL
- **Static Files**: AWS S3, CloudFront
- **Media Storage**: AWS S3

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is proprietary software for the Nigerian Music Distribution Platform.

## Support

For technical support or questions:
- Email: support@musicdistribute.ng
- Phone: +234 (0) 800 MUSIC NG

---

**Version**: 1.0.0  
**Last Updated**: January 2025
