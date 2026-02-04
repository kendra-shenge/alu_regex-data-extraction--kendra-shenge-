# ALU Regex Data Extraction - Kendra Shenge

## Overview
This project is a Python program for **data extraction and secure validation** using regular expressions (regex).  
It was developed as part of a Junior Frontend Developer assignment to handle **raw text input** from external sources, extract structured data, and validate it safely.

The program extracts the following types of data:

- **Email addresses** (including complex formats and subdomains)  
- **Phone numbers** (Rwandan formats supported: local and international)  
- **Credit card numbers** (masked for security)  
- **Times** (12-hour and 24-hour formats)

Security is emphasized by ignoring malformed or malicious inputs, such as `<script>` tags or SQL injection attempts, and masking sensitive data like credit card numbers.

---

## Features

1. **Email Extraction**
   - Detects standard emails: `user@example.com`
   - Detects complex emails: `firstname.lastname@company.co.uk`
   - Ignores malformed emails (`user@@example.com`)

2. **Phone Number Extraction**
   - Supports Rwanda formats:
     - `+250 788 123 456`
     - `0785554433`
   - Ignores invalid phone numbers

3. **Credit Card**
