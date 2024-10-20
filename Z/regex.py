import re
text = '''Hello! You can reach out to us via email at support@example.com or "
        "sales@mydomain.org. Our customer service hotline is +1 (555) 123-4567, "
        "and our backup number is 123.456.7890. For more information, visit our websites: "
        "https://example.com or http://mydomain.org/about. We also have an event coming up on "
        "12/25/2024 and another on 01-15-2025. If you'd like to contact us on social media, "
        "follow us @ExampleCorp on Twitter.'''

pattern = '([a-zA-Z0-9]+)@([a-zA-Z0-9]+)|([0-9]{2}-[0-9]{2}-[0-9]{4})|([0-9]{2}/[0-9]{2}/[0-9]{4})'
matches = re.findall(pattern, text)

print(matches)

pattern = '([0-9]{2}-[0-9]{2}-[0-9]{4})'

matches = re.findall(pattern, text)

print(matches)

print("Hello\rWorld")
