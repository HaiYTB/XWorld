from account import user_info, wallet
from giftcode import redeem


def main():
    user_id = input("User ID: ")
    user_secret_key = input("User Secret Key: ")
    while True:
        choices = input("""
=============Tài Khoản=============
1.1 Kiểm Tra Thông Tin
1.2 Kiểm Tra Số Dư(Ví)

=============Gift Codes=============
2.1 Nhập Gift Code

===================================
0. Thoát


Lựa Chọn(VD: Chọn Kiểm Tra Thông Tin Thì Ghi 1.1): """)
        if choices == "1.1":
            info = user_info(user_id=user_id, user_secret_key=user_secret_key)
            print(info)
        elif choices == "1.2":
            balance = wallet(user_id=user_id, user_secret_key=user_secret_key)
            print(balance)
        elif choices == "2.1":
            code = input("Nhập GiftCode: ")
            gift = redeem(user_id=user_id, user_secret_key=user_secret_key, code=code)
            print(gift)
        elif choices == "0":
            break
        else:
            print("Chọn Sai! Vui Lòng Chọn Lại")
        print("\n\n\n")


if __name__ == "__main__":
    main()
