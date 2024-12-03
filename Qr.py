import qrcode

import flet as ft



def validate_url(url):
    """
    التحقق من صحة الرابط المُدخل.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def generate_qr_code(url, file_name, format_name, fill_color, back_color):
    """
    إنشاء رمز QR وحفظه.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    output_file = f"{file_name}.{format_name.lower()}"
    img.save(output_file)
    return output_file


def main(page: ft.Page):   # منع تغيير حجم النافذة (باستخدام الخصائص الحديثة)
    def toggle_theme(e):
        page.window.icon = "ico.png"  # اسم الصورة التي تريد استخدامها # تعيين ايقونة التطبيق
        # التبديل بين الوضع الداكن والفاتح
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.text = "Switch to Dark Mode"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.text = "Switch to Light Mode"
        page.update()




    SUPPORTED_FORMATS = ["PNG", "JPEG", "JPG", "BMP", "TIFF", "WEBP"]

    def on_generate_click(e):
        url = url_input.value.strip()
        file_name = file_name_input.value.strip() or "qr_code"
        format_name = format_dropdown.value
        fill_color = color_input.value.strip() or "black"
        back_color = back_color_input.value.strip() or "white"

        if not validate_url(url):
            result_text.value = "❌ Invalid URL! Please enter a valid URL."
            page.update()
            return

        if format_name not in SUPPORTED_FORMATS:
            result_text.value = f"❌ Unsupported format! Choose one of: {', '.join(SUPPORTED_FORMATS)}"
            page.update()
            return

        try:
            output_file = generate_qr_code(url, file_name, format_name, fill_color, back_color)
            result_text.value = f"✅ QR code saved as {output_file}"
            page.update()
        except Exception as ex:
            result_text.value = f"❌ Error: {ex}"
            page.update()

    # إعداد واجهة المستخدم
    page.title = "QR Code Generator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 415
    page.window.top = 50
    page.window.height = 765
    page.window.left = 1110
    # منع تغيير حجم النافذة (باستخدام الخصائص الحديثة)
    page.window.resizable = False  # منع تغيير الحجم
    page.window.maximized = False  # منع التكبيرمنع التكبير
    page.window.icon = (r"C:\Python\Flet GUI\icons.ico")  # رابط الأيقونة
    page.window.title_bar_hidden = True
    page.scroll = 'auto'
    # page.window.full_screen = True

    url_input = ft.TextField(label="Enter URL", width=400,selection_color='#74b9ff',dense=True)
    file_name_input = ft.TextField(label="Output File Name (without extension)", width=400)
    format_dropdown = ft.Dropdown(
        label="Select Image Format",
        width=400,
        options=[ft.dropdown.Option(format) for format in SUPPORTED_FORMATS],
        value="PNG",
    )
    color_input = ft.TextField(label="QR Code Color (default: black)", width=400)
    back_color_input = ft.TextField(label="Background Color (default: white)", width=400)
    generate_button = ft.ElevatedButton(text="Generate QR Code", on_click=on_generate_click,
    # تعيين خصائص الزر مثل طريقة CSS
    style = ft.ButtonStyle(
        bgcolor = '#212230',  # لون الخلفية
        color = '#FFFFFF',  # لون النص
        shape = ft.RoundedRectangleBorder(radius=5),  # زوايا مستديرة

    ),
    )
    generate_button.bgcolor = '#212230'
    generate_button.width = 200
    generate_button.height = 50
    generate_button.color = '#FFFFFF'
    generate_button.elevation = 90
    # إنشاء الزر مع تخصيص النمط


    result_text = ft.Text(value="", color="green", size=16)

    # إضافة العناصر إلى الصفحة
    page.add(
        url_input,
        file_name_input,
        format_dropdown,
        color_input,
        back_color_input,
        generate_button,
        result_text,
    )

       # إنشاء زر لتغيير الوضع

    theme_button = ft.ElevatedButton(
        text="Switch to Dark Mode",  # النص عند البداية
        on_click=toggle_theme,  # عند الضغط يتم التبديل بين الأوضاع
        width=200,  # عرض الزر
        height=50,  # ارتفاع الزر
        style=ft.ButtonStyle(
            bgcolor='#555445',  # لون الخلفية
            color='#FFFFFF',  # لون النص
            shape=ft.RoundedRectangleBorder(radius=2),  # زوايا مستديرة
        ),
    )

    # إضافة الزر إلى الصفحة داخل Container مع وضعه في الأسفل
    page.add(
        ft.Container(
            content=theme_button,
            alignment=ft.alignment.bottom_center,  # محاذاة الزر إلى أسفل الصفحة
            padding=ft.padding.only(bottom=1,top=10)

        )
    )
    by_me = ft.Container(
        content = ft.Text(
        value = 'CREATE BY :| MOHAMMED ALAA MOHAMMED | V.2 BETA.01',
        size = 12,
        color = '#335cfa',
        weight=ft.FontWeight.BOLD,  # جعل النص عريضًا
        selectable=True, # لجعل النص قابلًا للتحديد والنسخ


        ),
    alignment = ft.alignment.center,  # محاذاة النص في وَسَط الحاوية  +==  # محاذاة الزر إلى أسفل الصفحة
    padding = ft.padding.only(bottom=1, top=253),
    )
 # إضافة النص إلى الصفحة
    page.add(by_me)

# تشغيل التطبيق
if __name__ == "__main__":
    ft.app(main)
