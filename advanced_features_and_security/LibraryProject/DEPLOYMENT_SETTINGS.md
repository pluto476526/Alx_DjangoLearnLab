# HTTPS and Security Configuration

This README outlines the steps and configurations applied to secure the Django application.

---

## Overview

This guide details the steps taken to secure the Django application, enforcing HTTPS, securing cookies, and protecting the application from common web attacks.

---

## Security Configuration

### Step 1: Configure Django for HTTPS Support

The following settings ensure that all traffic to the site is over HTTPS and that browsers are instructed to use HTTPS for subsequent requests:

```python
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) header settings
# Instructs browsers to only access the site via HTTPS for the specified time (e.g., 1 year)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds

# Apply HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow preloading of HSTS in browsers that support it
SECURE_HSTS_PRELOAD = True
