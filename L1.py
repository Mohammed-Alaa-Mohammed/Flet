from flet import Icons, TextButton, ElevatedButton
from flet import *
import webbrowser
# === SET ALL FUNCTIONS OF HERE TO ALL TOOLS IN THIS APP ===

def on_button_click(e):


    webbrowser.open("https://gallery.flet.dev/icons-browser/")
    e.page.update()
# ==== SET Screen Fun to Set Tools in APP ====

def main (home:Page) :
#
    home.title = 'Dircode | V.2 | dev :: Mohammed Alaa Mohammed' # عنوان التطبيق
    home.window.width = '450' # التحكم في عرض النافذة
    home.window.height = '815' # التحكم في طول النافذة من الطول
    # home.bgcolor = colors.AMBER_ACCENT_100 # مكتبة موجودة تلقائي
    # home.bgcolor = '#21222e' # تعيين لون خاص
    home.window.top = 1 # التحكم في النافذة من الاعلي
    home.window.left = 1080 # التحكم في النافذة من اليسار
    # home.window.resizable = False # لعدم تكبير النافذة او التحكم فيها من حيث الحجم
    # home.window.title_bar_hidden = True # لإخفاء الشريط العلوي من التطبيق
    home.horizontal_alignment = "center" # توسيط العناصر من الأعلي و الأسفل الي منتصف الصفحة
    home.vertical_alignment = "center" # توسيط العناصر من اليسار و اليمين الي منتصف الصفحة
    # rtl => لتحريك ونقل النص العربي من اليسار الي اليمين مع اعطاء قيمة العرض له
    home.theme_mode = ThemeMode.DARK
    home.scroll = ScrollMode.AUTO
# ==== End of SET Screen Fun to Set Tools in APP ====

    #/////////////////////////////////////////////////////////////

 # === Set a Tools of APP ===
    btn_1 = TextButton("Find any One Student", icon=Icons.PERSON_SEARCH_SHARP, icon_color='#3498db',on_click=on_button_click)
    btn_2 = TextButton("Search in DATABASE", icon=Icons.FOLDER_OPEN, tooltip="Open DATABASE", icon_color='#ecf0f1')
    btn_3 = TextButton("Open DATABASE Now", icon=Icons.OPEN_IN_NEW, tooltip="Check DATABASE", icon_color='#e74c3c')
    super_btn = ElevatedButton(text="Login To Home Page Start", color="#c7ecee", bgcolor="#30336b", icon=Icons.ADD_BOX)

    home.add(btn_1,
            btn_2 ,
             btn_3,
            super_btn,
             )
    home.update() # Update All Tools to added..=> # Update All Elements of Set To View in Screen
app(main) # Run as Apk
# ft.app(target=main,view=ft.AppView.WEB_BROWSER) # Run as Website , === Set port if Found Error
# ft.app(target=main,view=ft.AppView.WEB_BROWSER,port='') # Run as Website , === Set port if Found Error
# ft.app(target=main) # Run as Windows