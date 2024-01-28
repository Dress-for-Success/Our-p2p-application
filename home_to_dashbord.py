from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
import sqlite3
from kivy.core.window import Window
from borrower_registration import (
    BorrowerScreen, BorrowerScreen1, BorrowerScreen2, BorrowerScreen3, BorrowerScreen4, BorrowerScreen5,
    BorrowerScreen6,BorrowerScreen7,BorrowerScreen8,BorrowerScreen9,BorrowerScreen10,BorrowerScreen11,
    BorrowerScreen12,BorrowerScreen13,BorrowerScreen14,BorrowerScreen15,BorrowerScreen16,BorrowerScreen17,
    BorrowerScreen18,BorrowerScreen19,Borrower
)
from lender_registration import (
    LenderScreen, LenderScreen1, LenderScreen2, LenderScreen3,
    LenderScreen_Edu_10th, LenderScreen_Edu_Intermediate,LenderScreen_Edu_Bachelors,
    LenderScreen_Edu_Masters, LenderScreen_Edu_PHD, LenderScreen4, LenderScreen5,
    LenderScreenInstitutionalForm1,LenderScreenInstitutionalForm2,LenderScreenInstitutionalForm3,
    LenderScreenInstitutionalForm4,LenderScreenInstitutionalForm5,LenderScreenIndividualForm1,
    LenderScreenIndividualForm2,LenderScreenIndividualForm3,LenderScreenIndividualBankForm1,
    LenderScreenIndividualBankForm2,LenderScreenInstitutionalBankForm1,LenderScreenInstitutionalBankForm2,
    KV
)
from borrower_dashboard import (
    DashboardScreen, ProfileScreen, ViewLoansScreen, OpenLoansScreen, ApplicationTrackerScreen, bd
)
from lender_dashboard import (
    LenderDashboard, ViewProfileScreen, ViewLoansScreen2, ALlLoansScreen, ApprovedLoansScreen, user_helpers1
)

kv = '''
<MainScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(20)

        MDGridLayout:
            cols: 2
            size_hint_y: None
            size_hint_x: 1
            height: self.minimum_height

            MDIconButton:
                icon: "account-group-outline"
                halign: "left"
                background_color: 1, 1, 1, 1
                user_font_size: "65dp" 
                canvas:
                    Color:
                        rgba: 0, 0, 0, 0.5 

            MDLabel:
                text: "GTPL "
                bold: True


        Image:
            source: "C:\Our-p2p-application\man rope.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: None, None
            allow_stretch: True
            size: "350dp", "120dp"
            
        MDLabel:
            text: "Hello!"
            halign: "center"
            bold: True
        MDLabel:
            text: "Welcome to GTPL! We’re glad you have decided to join us."
            halign: "center"
            size_hint_y: None
            height: dp(10)

        MDGridLayout:
            cols: 2
            spacing: 20
            padding: "0dp", "40dp", "0dp", "0dp"

            MDRaisedButton:
                id: logout
                text: "Login"
                on_release: app.root.current = "login"
                on_release: app.root.get_screen("main").change_text()
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                md_bg_color: 2/255, 61/255, 224/255, 1
                font_name: "Roboto-Bold"
                size_hint: 1, None
                canvas.before:
                    Color:
                        rgba: 2/255, 61/255, 224/255, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10,] 

            MDRaisedButton:
                id: signout
                text: "Signup"
                on_release: app.root.current = "signup"
                on_release: app.root.get_screen("main").change_text1()
                pos_hint: {'right': 1, 'y': 0.5}
                md_bg_color: 2/255, 61/255, 224/255, 1
                font_name: "Roboto-Bold"
                size_hint: 1, None
        MDLabel:
            text:''
            
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)

            MDLabel:
                text: 'Follow On Our Social Media'
                halign: "center"

            MDGridLayout:
                cols: 3
                spacing: dp(20)
                size_hint: None, 1
                size: self.minimum_size  # Ensure the grid layout takes its minimum size
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center the grid layout


                MDFloatingActionButton:
                    icon: 'facebook'
                    on_press: app.open_link("https://www.facebook.com")
                    md_bg_color: 2/255, 61/255, 224/255, 1
                MDFloatingActionButton:
                    icon: 'google'
                    on_press: app.open_link("https://www.google.com")
                    md_bg_color: 252/255, 3/255, 65/255, 1
                MDFloatingActionButton:
                    icon: 'linkedin'
                    on_press: app.open_link("https://www.linkedin.com/company/gtplind/")
                    md_bg_color: 2/255, 2/255, 187/255, 1

        MDLabel:
            text:''

<SignupScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 80
        spacing: 10

        MDLabel:
            id: label1
            text: 'Sign Up'
            halign: 'center'
            bold: True

        MDTextField:
            id:name
            hint_text: "Enter Full Name"
            helper_text: "Invalid name"
            helper_text_mode: "on_error"
            icon_right: 'account'

        MDTextField:
            id:mobile
            hint_text: "Mobile No"
            helper_text: "Invalid number"
            helper_text_mode: "on_error"
            icon_right: 'cellphone'

        MDTextField:
            id:email
            hint_text: "Enter Your Email"
            helper_text: "Invalid email"
            helper_text_mode: "on_error"
            icon_right: 'email'

        MDTextField:
            id:password
            hint_text: "Enter Your Password"
            icon_right: 'eye-off'
            helper_text: "Password must greater than 8 characters"
            helper_text_mode: "on_error"
            password: True

        MDTextField:
            id:password2
            hint_text: "Re-Enter Your Password"
            helper_text: "Password does not match"
            helper_text_mode: "on_error"
            icon_right: 'eye-off'
            password: True


        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = "main"
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Signup"
                on_release: app.root.get_screen("signup").login(name.text,mobile.text,email.text, password.text, password2.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<DScreen>:
    id: signout

    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "0dp"

        MDTopAppBar:
            title: "DashBoard"
            elevation: 2
            left_action_items: [["menu", lambda x: app.callback("Menu button pressed")]]
            right_action_items: [["logout", lambda x: app.logout_function()]]

        GridLayout:
            cols: 2
            spacing: 30
            padding: 80

            MDRaisedButton:
                text: "Borrower"
                md_bg_color: 98/255, 30/255, 166/255, 1
                theme_text_color: 'Custom'
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: app.root.current = 'BorrowerScreen'

            MDRaisedButton:
                text: "Lender"
                md_bg_color: 98/255, 30/255, 166/255, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: app.root.current = 'LenderScreen'


        MDTopAppBar:
            title:"FAQ"
            custom_action_items:[['help']]

<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 80
        spacing: 10

        MDLabel:
            id: label1
            text: 'Login Form'
            halign: 'center'
            padding:15
            bold: True

        MDTextField:
            id: email
            hint_text: "Email"
            helper_text_mode: "on_focus"
            icon_right: "account"

        MDTextField:
            id: password
            hint_text: "Password"
            helper_text: "Forgot your password?"
            helper_text_mode: "on_focus"
            icon_right: "key"
            password: True
            spacing: 20

        GridLayout:
            cols: 2
            spacing: 30
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = "main"
                on_release: app.root.get_screen("login").change_text3()
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDRaisedButton:
                text: "Login"
                on_release: app.root.get_screen("login").on_login(email.text, password.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 0, 0, 0, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


        MDLabel:
            id: error_label
            text: ""
'''

Builder.load_string(kv)


class MainScreen(Screen):

    def change_text(self):
        # Access the label in another screen and update its text
        pass

    def change_text1(self):
        # Access the label in another screen and update its text
        pass


class SignupScreen(Screen):

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def login(self, name, mobile, email, password, password2):
        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute(''' CREATE TABLE IF NOT EXISTS registration_table (
                                    customer_id INT PRIME NUMBER NOT NULL,
                                    name TEXT,
                                    mobile INT,
                                    email TEXT,
                                    password TEXT,
                                    gender TEXT ,
                                    date_of_birth DATE,
                                    mobile_number INT ,
                                    alternate_mobile_number TEXT,
                                    alternate_email TEXT ,
                                    profile_file TEXT,
                                    aadhar_number INT,
                                    pan_number TEXT,
                                    aadhar_file TEXT ,
                                    pan_file TEXT, 
                                    highest_qualification TEXT,
                                    tenth_certificate TEXT,
                                    inter_certificate TEXT ,
                                    bachelors_certificate TEXT ,
                                    masters_certificate TEXT,
                                    phd_certificate TEXT,
                                    street_name TEXT ,
                                    city_name TEXT,
                                    zip_code TEXT,
                                    state_name TEXT,
                                    country_name TEXT,
                                    father_name TEXT, 
                                    father_age TEXT, 
                                    father_occupation TEXT, 
                                    father_ph_no TEXT,
                                    mother_name TEXT, 
                                    mother_age TEXT, 
                                    mother_occupation TEXT, 
                                    mother_ph_no TEXT,
                                    proficient_type TEXT,
                                    collage_name TEXT,
                                    college_address TEXT,
                                    collage_id TEXT,
                                    collage_id_file TEXT,
                                    loan_type TEXT,
                                    investment INT,
                                    lending_period TEXT,
                                    employment_type TEXT,
                                    company_name TEXT,
                                    organization_type TEXT,
                                    company_address TEXT,
                                    company_pincode TEXT,
                                    company_country TEXT,
                                    landmark TEXT,
                                    business_number INT,
                                    annual_salary INT,
                                    designation TEXT,
                                    employee_id_file TEXT,
                                    six_months_bank_statement_file TEXT,
                                    account_holder_name TEXT,
                                    account_type TEXT,
                                    account_number INT,
                                    bank_name TEXT,
                                    bank_id TEXT,
                                    salary_id TEXT,
                                    branch_name TEXT,
                                    business_name TEXT,
                                    business_location TEXT,
                                    business_address TEXT,
                                    business_branch_name TEXT,
                                    business_type TEXT,
                                    nearest_location TEXT,
                                    no_of_employees_working TEXT,
                                    year_of_estd INT,
                                    industry_type TEXT,
                                    last_six_months_turnover TEXT,
                                    last_six_months_turnover_file TEXT,
                                    director_name TEXT,
                                    director_mobile_number INT,
                                    DIN TEXT,
                                    CIN TEXT,
                                    registered_office_address TEXT,
                                    proof_of_verification_file TEXT,
                                    marital_status TEXT,
                                    spouse_name TEXT, 
                                    spouse_date_textfield DATE, 
                                    spouse_mobile TEXT, 
                                    spouse_profession TEXT,
                                    spouse_company_name TEXT,
                                    spouse_company_address TEXT, 
                                    spouse_annual_salary TEXT,
                                    spouse_office_no TEXT,
                                    user_type TEXT,
                                    customer_status TEXT
                                    )
                                ''')

        cursor.execute('select * from registration_table')

        p = cursor.fetchall()

        email_list = []
        id_list = []
        for i in p:
            email_list.append(i[3])
            id_list.append(i[0])

        if len(id_list) == 0:
            a = 1000
        else:
            a = id_list[-1]

        if name == '' or mobile == '' or email == '' or password == '' or password2 == '':
            self.show_alert_dialog("You Must Enter All Fields")

        if name.isdigit() or len(name) < 3:
            self.ids.name.error = True

        if not mobile.isdigit() or len(mobile) != 10:
            self.ids.mobile.error = True

        if not email.endswith("@gmail.com"):
            self.ids.email.error = True

        if len(password) < 8:
            self.ids.password.error = True

        if password != password2 or password2 == "":
            self.ids.password2.error = True

        elif email in email_list:
            self.show_alert_dialog("email already exist")

        else:

            if (
                    password == password2
                    and email not in email_list
                    and not name.isdigit()
                    and len(name) >= 3
                    and email.endswith("@gmail.com")
                    and len(mobile) == 10
                    and mobile.isdigit()
                    and len(password) >= 8
            ):
                try:
                    a = a + 1
                    print(a)
                    self.ids.name.error = False
                    self.ids.mobile.error = False
                    self.ids.email.error = False
                    self.ids.password.error = False
                    self.ids.password2.error = False

                    cursor.execute(
                        "INSERT INTO registration_table (customer_id, name, mobile, email, password) VALUES (?,?,?, ?, ?)",
                        (a, name, mobile, email, password))
                    conn.commit()
                    self.show_alert_dialog(f'{email} is successfully signed up')
                    self.manager.current = "login"

                except sqlite3.Error as err:
                    self.show_alert_dialog(f"Error signing up: {err}")

        conn.commit()
        conn.close()


class DScreen(Screen):

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label = MDApp.get_running_app().root.get_screen('login')
        login_status_label.ids.email.text = ""
        login_status_label.ids.password.text = ""
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""
        self.manager.current = 'main'


class LoginScreen(Screen):

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.text = alert_text
        self.dialog.open()

    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def on_login(self, email, password):
        # Add your authentication logic here
        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()
        cursor.execute('select * from registration_table')

        p = cursor.fetchall()

        email_list = []
        password_list = []
        id_list = []
        for i in p:
            email_list.append(i[3])
            password_list.append(i[4])
            id_list.append(i[0])

        if email == '' and password == '':
            self.show_alert_dialog(f'Enter All Fields')

        elif email in email_list and password in password_list:
            for i in p:
                if email == i[3] and password == i[4]:
                    l = 'logged'
                    i = email_list.index(email)
                    cursor.execute("UPDATE registration_table SET customer_status = ? WHERE customer_id = ?",
                                   (l, id_list[i]))
                    conn.commit()
                    self.manager.current = "success"
                else:
                    b = ''
                    a = i[0]
                    cursor.execute("UPDATE registration_table SET customer_status = ? WHERE customer_id = ?",
                                   (b, a))
                    conn.commit()

        else:
            self.show_alert_dialog(f'Invalid Credits')

        conn.commit()
        conn.close()


class LoginApp(MDApp):
    def build(self):
        Builder.load_string(Borrower)
        Builder.load_string(KV)
        Builder.load_string(bd)
        Builder.load_string(user_helpers1)
        sm = ScreenManager()

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Blue"

        # Add screens
        main_screen = MainScreen(name="main")
        login_screen = LoginScreen(name="login")
        signup_screen = SignupScreen(name="signup")
        success_screen = DScreen(name="success")

        sm.add_widget(main_screen)
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)
        sm.add_widget(success_screen)

        sm.add_widget(BorrowerScreen(name='BorrowerScreen'))
        sm.add_widget(BorrowerScreen1(name='BorrowerScreen1'))
        sm.add_widget(BorrowerScreen2(name='BorrowerScreen2'))
        sm.add_widget(BorrowerScreen3(name='BorrowerScreen3'))
        sm.add_widget(BorrowerScreen4(name='BorrowerScreen4'))
        sm.add_widget(BorrowerScreen5(name='BorrowerScreen5'))
        sm.add_widget(BorrowerScreen6(name='BorrowerScreen6'))
        sm.add_widget(BorrowerScreen7(name='BorrowerScreen7'))
        sm.add_widget(BorrowerScreen8(name='BorrowerScreen8'))
        sm.add_widget(BorrowerScreen9(name='BorrowerScreen9'))
        sm.add_widget(BorrowerScreen10(name='BorrowerScreen10'))
        sm.add_widget(BorrowerScreen11(name='BorrowerScreen11'))
        sm.add_widget(BorrowerScreen12(name='BorrowerScreen12'))
        sm.add_widget(BorrowerScreen13(name='BorrowerScreen13'))
        sm.add_widget(BorrowerScreen14(name='BorrowerScreen14'))
        sm.add_widget(BorrowerScreen15(name='BorrowerScreen15'))
        sm.add_widget(BorrowerScreen16(name='BorrowerScreen16'))
        sm.add_widget(BorrowerScreen17(name='BorrowerScreen17'))
        sm.add_widget(BorrowerScreen18(name='BorrowerScreen18'))
        sm.add_widget(BorrowerScreen19(name='BorrowerScreen19'))
        sm.add_widget(LenderScreen(name='LenderScreen'))
        sm.add_widget(LenderScreen1(name='LenderScreen1'))
        sm.add_widget(LenderScreen2(name='LenderScreen2'))
        sm.add_widget(LenderScreen3(name='LenderScreen3'))
        sm.add_widget(LenderScreen_Edu_10th(name='LenderScreen_Edu_10th'))
        sm.add_widget(LenderScreen_Edu_Intermediate(name='LenderScreen_Edu_Intermediate'))
        sm.add_widget(LenderScreen_Edu_Bachelors(name='LenderScreen_Edu_Bachelors'))
        sm.add_widget(LenderScreen_Edu_Masters(name='LenderScreen_Edu_Masters'))
        sm.add_widget(LenderScreen_Edu_PHD(name='LenderScreen_Edu_PHD'))
        sm.add_widget(LenderScreen4(name='LenderScreen4'))
        sm.add_widget(LenderScreen5(name='LenderScreen5'))
        sm.add_widget(LenderScreenInstitutionalForm1(name='LenderScreenInstitutionalForm1'))
        sm.add_widget(LenderScreenInstitutionalForm2(name='LenderScreenInstitutionalForm2'))
        sm.add_widget(LenderScreenInstitutionalForm3(name='LenderScreenInstitutionalForm3'))
        sm.add_widget(LenderScreenInstitutionalForm4(name='LenderScreenInstitutionalForm4'))
        sm.add_widget(LenderScreenInstitutionalForm5(name='LenderScreenInstitutionalForm5'))
        sm.add_widget(LenderScreenIndividualForm1(name='LenderScreenIndividualForm1'))
        sm.add_widget(LenderScreenIndividualForm2(name='LenderScreenIndividualForm2'))
        sm.add_widget(LenderScreenIndividualForm3(name='LenderScreenIndividualForm3'))
        sm.add_widget(LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1'))
        sm.add_widget(LenderScreenIndividualBankForm2(name='LenderScreenIndividualBankForm2'))
        sm.add_widget(LenderScreenInstitutionalBankForm1(name='LenderScreenInstitutionalBankForm1'))
        sm.add_widget(LenderScreenInstitutionalBankForm2(name='LenderScreenInstitutionalBankForm2'))
        sm.add_widget(DashboardScreen(name='DashboardScreen'))
        sm.add_widget(ProfileScreen(name='ProfileScreen'))
        sm.add_widget(ViewLoansScreen(name='ViewLoansScreen'))
        sm.add_widget(OpenLoansScreen(name='OpenLoansScreen'))
        sm.add_widget(ApplicationTrackerScreen(name='ApplicationTrackerScreen'))
        sm.add_widget(LenderDashboard(name='LenderDashboard'))
        sm.add_widget(ViewProfileScreen(name='ViewProfileScreen'))
        sm.add_widget(ViewLoansScreen2(name='ViewLoansScreen2'))
        sm.add_widget(ALlLoansScreen(name='ALlLoansScreen'))
        sm.add_widget(ApprovedLoansScreen(name='ApprovedLoansScreen'))

        self.success_screen = success_screen

        return sm

    def logout_function(self):
        # Access the stored reference to the success_screen and call its method
        self.success_screen.change_text3()

    def on_stop(self):
        if hasattr(self.root.get_screen('signup'), 'connection') and self.root.get_screen(
                'signup').connection.is_connected():
            self.root.get_screen('signup').cursor.close()
            self.root.get_screen('signup').connection.close()


if __name__ == "__main__":
    LoginApp().run()