# کتابخانه برای خواندن فایل
import csv
# باز کردن فایل
f = open(r"sales.csv", "r")
# خواندن فایل و تبدیل داده‌ها به دیکشنری
sales = list(csv.DictReader(f))

# شمارش تعداد تراکنش‌ها
count = 0
# بررسی تمام ردیف‌های جدول
for row in sales:
    # بررسی اینکه کد تراکنش خالی نباشد
    if row[0] != "":
        count += 1
print("Total transactions:", count)

# مجموع فروش
total = 0
# بررسی تمام تراکنش‌ها
for row in sales:
# برای جلوگیری از ارور از ترای اکسپت استفاده شد
    try:
        # تبدیل تعداد، قیمت واحد و تخفیف به عدد
        quantity = int(row["quantity"])
        unit_price = int(row["unit_price"])
        discount = int(row["discount"])

        # بررسی معتبر بودن تعداد، قیمت و تخفیف    
        if quantity > 0 and unit_price > 0 and 0 <= discount <= 100:
            # محاسبه مبلغ نهایی
            amount = (quantity * unit_price) * (1 - discount / 100)
        # اضافه کردن مبلغ به مجموع فروش
        total += amount
    # نادیده گرفتن ردیف‌هایی که مقدار نامعتبر دارند
    except ValueError:
        print("Invalid Value")
        continue
      
print("Total sales:",total)

# محاسبه میانگین
average = total / count

print("Average transaction amount:", average)
