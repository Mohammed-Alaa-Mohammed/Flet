import flet as ft
import requests
from datetime import datetime, timezone
import time
import threading

from sympy.physics.units import action

API_KEY = "87652b474028c2d810e1169d146a1cb3"  # استبدل هذا بـ API Key الخاص بك
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# دالة للحصول على بيانات الطقس
def get_weather_data(city: str, units: str):
    """دالة للحصول على بيانات الطقس من API"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,  # درجة الحرارة بالوحدة المطلوبة (Celsius أو Fahrenheit)
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            return None, "حدث خطأ أثناء الحصول على البيانات. تأكد من المدينة أو API Key.", None, None, None, None, None, None

        data = response.json()
        main = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        icon = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon}.png"
        rain = data.get("rain", {}).get("1h", 0)  # كمية الأمطار في الساعة (إن وجدت)

        # تحويل الوقت إلى تنسيق مناسب
        timestamp = data["dt"]
        time = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        return main, description, temperature, humidity, wind_speed, pressure, icon_url, rain, time
    except requests.exceptions.RequestException as e:
        return None, f"حدث خطأ في الاتصال بالإنترنت أو في الـ API: {e}", None, None, None, None, None, None, None


# دالة للحصول على التنبؤات المستقبلية (مثال: 3 أيام)
def get_weather_forecast(city: str, units: str):
    """دالة للحصول على التنبؤات المستقبلية من API"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        if response.status_code != 200:
            return None, "حدث خطأ أثناء الحصول على التنبؤات."

        data = response.json()
        forecasts = []
        for forecast in data["list"][:3]:  # أخذ 3 أيام
            date = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            weather = forecast["weather"][0]["description"]
            rain = forecast.get("rain", {}).get("3h", 0)  # الأمطار في الساعة
            forecasts.append(f"{date}: {weather} - {temp}° | الأمطار: {rain}mm")
        return forecasts
    except requests.exceptions.RequestException as e:
        return None, f"حدث خطأ في الاتصال بالإنترنت أو في الـ API: {e}"



def show_messagebox(page):
    alert = ft.AlertDialog(
        modal=True,
        title=ft.Row([
            ft.Icon(ft.icons.WALLET_GIFTCARD_ROUNDED, color=ft.colors.AMBER, size=30),
            ft.Text("مرحبًا في تطبيق الطقس V.3.1 BETA", weight=ft.FontWeight.BOLD, size=16)
        ], alignment=ft.MainAxisAlignment.CENTER),
        content=ft.Text(
            "\n☀️ تم فتح التطبيق بنجاح!\n\n"
            "🌦️ استمتع بتجربة الطقس بدقة عالية.\n\n"
            "💡 اضغط على زر \"إغلاق\" لإغلاق الرسالة.",
            text_align=ft.TextAlign.CENTER,
            size=14,
        ),
        actions=[
            ft.ElevatedButton(
                "إغلاق",
                on_click=lambda e: close_alert(page, alert)
            )
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.overlay.append(alert)
    alert.open = True
    page.update()

    def close_alert(page, alert):
        alert.open = False
        page.update()


# دالة لإغلاق الـ AlertDialog بشكل آمن
def close_alert(page, alert):
    if alert in page.overlay:
        page.overlay.remove(alert)
        alert.open = False
        page.update()


# دالة واجهة المستخدم
def main(page):
    # تعيين خصائص النافذة
    page.title = "تطبيق الطقس | Mohammed Alaa Mohammed > V.3.1 BETA"
    page.window.icon = (r"C:\Python\Flet GUI\map_icon.ico")  # رابط الأيقونة
    page.window.top = 35
    page.window.width = 500
    page.window.height = 800
    page.window.height = 750
    page.window.left = 500
    page.window.resizable = True
    page.window.title_bar_hidden = False
    page.scroll = 'auto'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#222f3e"  # تحديد اللون الخلفي الداكن

    # إدخال المدينة
    city_input = ft.TextField(label="أدخل اسم المدينة", autofocus=True)
    units_select = ft.Dropdown(
        label="اختر وحدة قياس درجة الحرارة",
        options=[ft.dropdown.Option("metric", "Celsius"), ft.dropdown.Option("imperial", "Fahrenheit")],
        value="metric",
    )
    result_label = ft.Text(value=".....بيانات الــطــقــس تظــهــر هــنا")
    # weather_image = ft.Image(width=150, height=150)
    additional_info_label = ft.Text(value="الرطوبة: --% | الرياح: -- m/s | الضغط الجوي: -- hPa")
    forecast_label = ft.Text(value=" : التنبؤات المستقبلية")
    rain_label = ft.Text(value="كمية الأمطار المتوقعة: -- mm")
    error_label = ft.Text(value="", color="red")
    alert_label = ft.Text(value="", color="green")

    # دالة لتحديث الطقس
    def update_weather(e=None):  # إضافة معطى افتراضي للمعامل e
        city = city_input.value
        units = units_select.value
        main, description, temperature, humidity, wind_speed, pressure, icon_url, rain, time = get_weather_data(city,
                                                                                                                units)

        if main:
            result_label.value = f"الطقس في {city} هو {main} ({description}) ودرجة الحرارة {temperature}°"
            # weather_image.src = icon_url
            additional_info_label.value = f"الرطوبة: {humidity}% | الرياح: {wind_speed} m/s | الضغط الجوي: {pressure} hPa"
            rain_label.value = f"كمية الأمطار المتوقعة: {rain} mm"
            forecast_label.value = f"التنبؤات المستقبلية: ..."
            alert_label.value = "حالة الطقس جيدة."
        else:
            result_label.value = description
            # weather_image.src = ""
            additional_info_label.value = ""
            forecast_label.value = ""
            rain_label.value = ""
            alert_label.value = ""

        page.update()

    # دالة لتحديث الطقس تلقائيًا كل 10 ثواني
    def auto_update_weather():
        while auto_update_toggle.value:
            update_weather()  # الآن دالة update_weather لن تأخذ أي معطيات
            time.sleep(10)  # تحديث كل 10 ثواني

    # زر التحديث التلقائي
    auto_update_toggle = ft.Switch(label="  التحديث التلقائي", value=False)

    # دالة عند التبديل بين التحديث التلقائي
    def on_auto_update_toggle(e):
        if auto_update_toggle.value:
            # بدء التحديث التلقائي في خيط منفصل
            threading.Thread(target=auto_update_weather, daemon=True).start()
        else:
            # إيقاف التحديث التلقائي (سيتم إيقاف التحديث عند تعطيل الـ toggle)
            pass

    # زر الحصول على الطقس
    get_weather_button = ft.ElevatedButton(
        text="الحصول على الطقس",
        on_click=update_weather,
        width=200,
        height=45,
        style=ft.ButtonStyle(
            bgcolor='#212230',  # لون الخلفية
            color='#F2F3F1',  # لون النص
            shadow_color="#0fffff" ,
            shape=ft.RoundedRectangleBorder(radius=10),  # زوايا مستديرة
        ))

    # إضافة نافذة منبثقة عند فتح التطبيق
    show_messagebox(page)

    # إضافة عناصر الصفحة
    page.add(
        ft.Column(
            controls=[
                city_input,
                units_select,
                get_weather_button,
                auto_update_toggle,
                alert_label,
                # weather_image,
                result_label,
                additional_info_label,
                rain_label,
                forecast_label,
                error_label,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
# ft.app(target=main,view=ft.AppView.WEB_BROWSER)
ft.app(target=main)


# V.3.1 BETA
# BY | Mohammed Alaa Mohammed
# Last Update | 2025 - 1 - 30
