import re
import sys

def extract_emails(text):
    """
    Extracts email addresses from text.
    Validates standard email formats including those with subdomains.
    Security: Prevents catastrophic backtracking by avoiding nested quantifiers like (a+)+
    """
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    emails = re.findall(email_pattern, text)
    return list(set(emails))

def extract_phone_numbers(text):
    """
    Extracts phone numbers, focusing on Rwandan formats.
    Supports: 
    - +250 7XX XXX XXX (Rwanda International format)
    - 07X XXX XXXX (Rwanda Local format)
    - Normalizes output to remove spaces/separators for processing.
    """
    phone_pattern = r'(?:\+250[\s-]?|0)7[2389]\d[\s-]?\d{3}[\s-]?\d{3}'
    
    matches = re.findall(phone_pattern, text)
    
    
    valid_phones = []
    for num in matches:
        clean_num = re.sub(r'[\s-]', '', num)
        
        if len(clean_num.replace('+','')) in [10, 12]:
            valid_phones.append(num) 
            
    return list(set(valid_phones))

def extract_credit_cards(text):
    """
    Extracts potential credit card numbers.
    Masks them for security (e.g., **** 3456).
    """
    cc_pattern = r'\b(?:\d{4}[\s-]?){3}\d{4}\b'
    
    cards = re.findall(cc_pattern, text)
    masked_cards = []
    
    for card in cards:
        
        clean_card = re.sub(r'[\s-]', '', card)
        

        
        if len(clean_card) == 16:
            
            last_4 = clean_card[-4:]
            masked = f"**** **** **** {last_4}"
            masked_cards.append(masked)
            
    return list(set(masked_cards))

def extract_times(text):
    """
    Extracts times in 12-hour (AM/PM) and 24-hour formats.
    """
    pattern_12hr = r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?[APap][Mm]\b'
    pattern_24hr = r'\b(?:2[0-3]|[01]?[0-9]):[0-5][0-9]\b'
    
    time_pattern = f"({pattern_12hr})|({pattern_24hr})"
    
    raw_matches = re.findall(time_pattern, text)
    times = []
    for m in raw_matches:
    
        if m[0]: 
            times.append(m[0])
        elif m[1]: 
            times.append(m[1])
        
    return list(set(times))

def process_file(filepath):
    """
    Main execution flow.
    Reads file -> Extracts Data -> Validates/Masks -> Prints Report.
    """
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        print(f"--- Data Extraction Report: {filepath} ---")
        

        emails = extract_emails(content)
        phones = extract_phone_numbers(content)
        cards = extract_credit_cards(content)
        times = extract_times(content)
        
        print(f"\n[+] Extracted Emails ({len(emails)} found):")
        for email in emails:
            print(f"  - {email}")
            
        print(f"\n[+] Extracted Phone Numbers ({len(phones)} found):")
        for phone in phones:
            print(f"  - {phone}")
            
        print(f"\n[+] Extracted Credit Cards ({len(cards)} found):")
        if not cards:
            print("  - None found (or all invalid)")
        else:
            print("  - [SECURE] Sensitive data masked:")
            for card in cards:
                print(f"  - {card}")
            
        print(f"\n[+] Extracted Times ({len(times)} found):")
        for time_val in times:
            print(f"  - {time_val}")
            
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python regex_extractor.py <input_file>")
        print("Example: python regex_extractor.py sample_input.txt")
    else:
        process_file(sys.argv[1])
        