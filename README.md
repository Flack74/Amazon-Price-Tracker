```markdown
# Amazon Price Tracker

A Python-based tool for monitoring and alerting users to price changes on Amazon products.

## Overview

Amazon Price Tracker is designed to help users track price fluctuations of specific products on Amazon. It automatically checks prices at regular intervals and sends email notifications when the price drops below a user-defined threshold.

## Features

- Automated price checking for Amazon products
- Customizable price thresholds
- Email notifications for price drops
- Configurable checking intervals

## Requirements

- Python 3
- BeautifulSoup4
- Requests
- smtplib

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/flack74/amazon-price-tracker.git
   ```

2. Navigate to the project directory:
   ```
   cd amazon-price-tracker
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open `config.py` and set the following variables:
   - `PRODUCT_URL`: The Amazon product URL you want to track
   - `TARGET_PRICE`: Your desired price threshold
   - `CHECK_INTERVAL`: How often to check the price (in seconds)

2. add your email credentials:
   - `EMAIL_ADDRESS`: Your email address
   - `EMAIL_PASSWORD`: Your email password or app-specific password

## Usage

```
Run the script with:
```
python3 main.py
```
