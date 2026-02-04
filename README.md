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

3. **Credit Card Extraction**
   - Detects numbers with spaces or dashes: `1234 5678 9012 3456`
   - Masks sensitive data in output: `**** **** **** 3456`
   - Ignores incomplete or malformed card numbers

4. **Time Extraction**
   - Detects both 24-hour format (`14:30`) and 12-hour format (`2:30 PM`)
   - Ignores invalid times like `25:00`

---

## Security Considerations

- Sensitive information such as credit card numbers is **masked** before printing
- Malicious scripts or SQL injection attempts are ignored
- Regex patterns are designed to avoid **catastrophic backtracking**
- Only valid and well-formed inputs are extracted

---

## Getting Started

### Prerequisites
- Python 3.x installed  
- Command-line interface (CLI) or VS Code terminal  

### Installation
1. Clone the repository:

```bash
git clone https://github.com/kendra-shenge/alu_regex-data-extraction-kendra-shenge.git
cd alu_regex-data-extraction-kendra-shenge
