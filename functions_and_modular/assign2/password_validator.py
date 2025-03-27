def check_pass_strength(**kwargs):
    
    password=kwargs.get("password","")

    if len(password)<8:
        return "Weak: Password must be at least 8 characters long"
    
    has_upper=has_lower=has_digit=False

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        
        if has_upper and has_lower and has_digit:
            return "Strong: Password meets all criteria!"

    if not has_upper:
        return "Weak: Password must contain at least one uppercase letter."
    if not has_lower:
        return "Weak: Password must contain at least one lowercase letter."
    if not has_digit:
        return "Weak: Password must contain at least one digit."

print(check_pass_strength(password="Hello123"))
print(check_pass_strength(password="hello123"))
print(check_pass_strength(password="HELLO123"))
print(check_pass_strength(password="Hello"))