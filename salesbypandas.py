# وارد کردن کتابخانه
import pandas as pd
# خواندن فایل فروش
sales = pd.read_csv(r"sales.csv")
# بررسی تعداد مقادیر خالی در هر ستون
print(sales.isnull().sum())

# بررسی تعداد ردیف‌های تکراری
print(sales.duplicated().sum())
# حذف ردیف‌های تکراری
sales = sales.drop_duplicates()

# تبدیل ستون‌های عددی به نوع داده مناسب
sales["age"] = pd.to_numeric(sales["age"], errors="coerce")
sales["quantity"] = pd.to_numeric(sales["quantity"], errors="coerce")
sales["unit_price"] = pd.to_numeric(sales["unit_price"], errors="coerce")
sales["discount"] = pd.to_numeric(sales["discount"], errors="coerce")

# تبدیل ستون تاریخ به نوع تاریخ و زمان
sales["created_at"] = pd.to_datetime(sales["created_at"], errors="coerce")

# حذف سن‌های نامعتبر
sales = sales[(sales["age"] > 0) & (sales["age"] <= 100)]

# حذف تعداد و قیمت‌های نامعتبر
sales = sales[(sales["quantity"] > 0) & (sales["unit_price"] > 0)]

# حذف درصد تخفیف نامعتبر
sales = sales[(sales["discount"] >= 0) & (sales["discount"] <= 100)]

# نمایش تعداد تاریخ‌های نامعتبر
print("Invalid dates:", sales["created_at"].isnull().sum())

# نمایش نوع داده ستون‌ها
print(sales.dtypes)

# محاسبه مبلغ نهایی
sales["amount"] = (sales["quantity"] * sales["unit_price"] * (1 - sales["discount"] / 100))

# پیدا کردن شهر با بیشترین فروش
print(sales.groupby("city")["amount"].sum().sort_values(ascending=False))

# پیدا کردن محصول با بیشترین فروش
print(sales.groupby("product")["amount"].sum().sort_values(ascending=False))

# پیدا کردن دسته محصول با بیشترین فروش
print(sales.groupby("category")["amount"].sum().sort_values(ascending=False))

# شمارش تعداد استفاده از هر روش پرداخت
print(sales["payment_method"].value_counts())

# محاسبه میانگین مبلغ تراکنش
print(sales["amount"].mean())

# پیدا کردن مشتری با بیشترین مبلغ خرید
print(sales.groupby("customer_id")["amount"].sum().sort_values(ascending=False))

# پیدا کردن مشتری با بیشترین تعداد تراکنش
print(sales["customer_id"].value_counts())

# پیدا کردن محصول با بیشترین تعداد فروش
print(sales.groupby("product")["quantity"].sum().sort_values(ascending=False))

# محاسبه فروش بر اساس تاریخ
print(sales.groupby(sales["created_at"].dt.date)["amount"].sum())

# پیدا کردن شهر با بیشترین تعداد تراکنش
print(sales["city"].value_counts())

# وارد کردن کتابخانه رسم نمودار
import matplotlib.pyplot as pt
# محاسبه فروش هر شهر
city_sales = sales.groupby("city")["amount"].sum()

# رسم نمودار فروش شهرها
city_sales.plot(kind="bar")
pt.title("Sales by City")
pt.xlabel("City")
pt.ylabel("Sales")
pt.show()

# محاسبه فروش هر دسته محصول
category_sales = sales.groupby("category")["amount"].sum()

# رسم نمودار فروش دسته‌های محصول
category_sales.plot(kind="bar")
pt.title("Sales by Category")
pt.xlabel("Category")
pt.ylabel("Sales")
pt.show()

# محاسبه فروش در طول زمان
daily_sales = sales.groupby(
    sales["created_at"].dt.date
)["amount"].sum()

# رسم نمودار فروش در طول زمان
daily_sales.plot(kind="line")
pt.title("Sales Over Time")
pt.xlabel("Date")
pt.ylabel("Sales")
pt.show()

# محاسبه روش های پرداخت
payment = sales["payment_method"].value_counts()

# رسم نمودار روش های پرداخت
payment.plot(kind="pie", autopct="%1.1f%%")
pt.title("Payment Methods")
pt.ylabel("")
pt.show()

# ساخت جدول ویژگی‌های رفتاری مشتریان
customer_data = sales.groupby("customer_id").agg(
    total_spent=("amount", "sum"),
    transaction_count=("transaction_id", "count"),
    total_quantity=("quantity", "sum"),
    avg_transaction=("amount", "mean"),
    avg_discount=("discount", "mean")
)

print(customer_data)

# ذخیره داده‌های پاکسازی‌شده
sales.to_csv("clean_sales.csv", index=False)

# خواندن فایل‌های بزرگ به صورت بخش‌های 100 هزار ردیفی
for chunk in pd.read_csv("sales.csv", chunksize=100000):
    print(chunk)

