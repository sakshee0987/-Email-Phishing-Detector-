import re

# Function to detect phishing email
def detect_phishing(email_text):

    phishing_keywords = [
        "urgent",
        "verify your account",
        "click here",
        "bank",
        "password",
        "login",
        "winner",
        "free",
        "update account",
        "limited time"
    ]

    score = 0

    # Convert email to lowercase
    email_text = email_text.lower()

    # Check phishing keywords
    for word in phishing_keywords:
        if word in email_text:
            score += 1

    # Check suspicious links
    links = re.findall(r'http[s]?://', email_text)
    if len(links) > 0:
        score += 2

    # Final Result
    if score >= 3:
        return "Phishing Email Detected!"
    else:
        return "Safe Email"


# Main Program
print("=== Phishing Email Detection ===")

email = input("\nEnter Email Content:\n")

result = detect_phishing(email)

print("\nResult:", result)