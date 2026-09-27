raw_username = "  Super_Coder_2026  "
username = raw_username.strip().lower().replace("_","-")
print(f"მომხმარებლის სახელი: {username}")
print(f"სიგრძე: {len(username)}")
print(f"იწყება 'super'-ით: {username.startswith("super")}")
print(f"ტირეების რაოდენობა: {username.count("-")}")
print(f"მხოლოდ ასოები და ციფრები: {username.replace("-","").isalnum()}")