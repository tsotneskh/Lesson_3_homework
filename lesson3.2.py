card = "4111222233334444"
phone = "599123456"
print(f"შენიღბული: **** **** **** {card[-4:]}")
print(f"პირველი 4 ციფრი: {card[:4]}")
print(f"ციფრების რაოდენობა: {len(card)}")
print(f"შებრუნებული: {card[::-1]}")
print(f"ტელეფონი: {phone[:3]} {phone[3:5]} {phone[5:7]} {phone[7:9]}")
