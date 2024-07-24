```markdown
# 🛒 Amazon Price Tracker

Automate your Amazon deal-hunting with precision and ease.

## 🌟 Key Features

- 🔄 **Automated Price Monitoring**: Keep tabs on your favorite Amazon products
- 💰 **Custom Price Alerts**: Set your own price thresholds
- 📧 **Instant Email Notifications**: Get alerted as soon as prices drop
- ⏱️ **Flexible Checking Intervals**: Customize how often prices are checked

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/flack74/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ How to Use

Run the tracker with:

```bash
python3 main.py
```

The script will run in the background, vigilantly checking prices and notifying you of any drops.

## ⚙️ Configuration

1. set:
   - `PRODUCT_URL`: URL of the Amazon product to track
   - `TARGET_PRICE`: Your desired price point
   - `CHECK_INTERVAL`: Frequency of price checks (in seconds)

2. Configure your email:
   - `EMAIL_ADDRESS`: Your email address
   - `EMAIL_PASSWORD`: Your email password or app-specific password

## 🛠️ Tech Stack
```
- Python 3
- BeautifulSoup4: For parsing HTML
- Requests: For making HTTP requests
- smtplib: For sending email notifications
```
