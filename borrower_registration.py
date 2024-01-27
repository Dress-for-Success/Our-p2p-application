from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import sqlite3
from datetime import date
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.filemanager import MDFileManager

Borrower = '''
<BorrowerScreen>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"
        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: username
            hint_text: 'Enter Full Name'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: email
            hint_text: 'Enter Email ID'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Email ID"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        Spinner:
            padding:  10
            id: gender_id
            text: "Select Gender"
            values: ["Select Gender","Male", "Female", "Others"]
            multiline: False
            size_hint: 1 , None
            bold: True
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTextField:
            id: date_textfield
            hint_text: 'Select Date of Birth'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Select Valid Date of Birth"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            on_focus: root.show_date_picker()

        MDTextField:
            id: mobile_number
            hint_text: ' Enter Mobile No'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Mobile No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'vertical'
            padding: "40dp"

            MDRaisedButton:
                text: 'Next'
                text_color: 0, 0, 0, 1  
                md_bg_color: 0.031, 0.463, 0.91, 1
                size_hint: 1, None
                height: "50dp"
                on_release: root.add_data(username.text, gender_id.text, email.text, date_textfield.text, mobile_number.text)


<BorrowerScreen1>:

    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "50dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: alternate_mobile_number
            hint_text: ' Enter Alternate Mobile No'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Alternate Mobile No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: alternate_email
            hint_text: ' Enter Alternate Email ID'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Alternate Email ID"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1 
                Line:
                    width: 0.4  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon1
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label1
                text: 'Upload Profile Image'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(alternate_mobile_number.text, alternate_email.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ''

<BorrowerScreen2>:

    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: aadhar_number
            hint_text: 'Enter Gov ID1 Number '
            multiline: False
            helper_text: "Enter Valid Gov ID1 No"
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon2
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label1
                text: 'Upload Gov ID1'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTextField:
            id: pan_number
            hint_text: 'Enter Gov ID2 Number '
            multiline: False
            helper_text: "Enter Valid Gov ID2 No"
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon3
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_2()

            MDLabel:
                id: upload_label2
                text: 'Upload Gov ID2'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1 
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}



        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen1'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(aadhar_number.text, pan_number.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""  


<BorrowerScreen3>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Address'
            font_size: 25
            halign: 'center'
            bold: True


        MDTextField:
            id: street_address
            hint_text: 'Enter Street Address '
            multiline: False
            helper_text: 'Enter Valid Address'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: city
            hint_text: 'Enter City'
            multiline: False
            helper_text: 'Enter valid City'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: Zip_code
            hint_text: 'Enter postal/zipcode'
            multiline: False
            helper_text: 'Enter valid postal/zipcode'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: state
            hint_text: 'Enter State'
            multiline: False
            helper_text: 'Enter State Name'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: country
            hint_text: 'Enter Country'
            multiline: False
            helper_text: 'Enter valid Country Name'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen2'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(street_address.text, city.text, Zip_code.text, state.text, country.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen4>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Father Information'
            font_size: 25
            halign: 'center'
            bold: True


        MDTextField:
            id: father_name
            hint_text: 'Enter Father Name'
            helper_text: 'Enter valid Father Name'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: father_age
            hint_text: 'Enter Father Age'
            helper_text: 'Enter valid Father Age'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: father_occupation
            hint_text: 'Enter Father Occupation'
            helper_text: 'Enter valid Father Occupation'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: father_ph_no
            hint_text: 'Enter Father Phone NO'
            multiline: False
            helper_text: 'Enter valid PH No'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen3'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(father_name.text, father_age.text, father_occupation.text, father_ph_no.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen5>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Mother Information'
            font_size: 25
            halign: 'center'
            bold: True


        MDTextField:
            id: mother_name
            hint_text: 'Enter Mother Name'
            helper_text: 'Enter Valid Mother Name'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: mother_age
            hint_text: 'Enter Mother Age'
            helper_text: 'Enter Valid Mother Age'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: mother_occupation
            hint_text: 'Enter Mother Occupation'
            helper_text: 'Enter Valid Mother Occupation'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: mother_ph_no
            hint_text: 'Enter Mother Phone No'
            helper_text: 'Enter Valid Mother Phone No'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_name: "Roboto-Bold"
            bold: True


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen4'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(mother_name.text, mother_age.text, mother_occupation.text, mother_ph_no.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen6>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form Mother Information'
            font_size: 25
            halign: 'center'
            bold: True


        Spinner:
            id: spinner_id
            text: "Select Proficient type"
            values: ["Select Proficient type","Student", "Employee", "Business"]
            multiline: False
            size_hint: 1 , None
            bold: True
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen5'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_press: root.add_data(spinner_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen7>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  # Black text color
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'STUDENT TYPE'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: collage_name
            hint_text: 'Enter Collage Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: 'Enter Valid Collage Name'
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: collage_id
            hint_text: 'Enter Collage ID'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: True
            helper_text: "Enter valid Collage ID"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon4
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label2
                text: 'Upload Collage proof'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDTextField:
            id:  college_address
            hint_text: 'Enter College Address'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: 'Enter valid College Address'
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(collage_name.text, college_address.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen8>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Business Type'
            font_size: 25
            halign: 'center'
            bold: True

        MDLabel:
            text: 'STEP-1'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: business_name
            hint_text: 'Enter Business Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True

        MDTextField:
            id: business_location
            hint_text: 'Enter Business Location'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Location"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True

        MDTextField:
            id:  business_address
            hint_text: 'Enter Business Address'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Address"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True

        MDTextField:
            id: business_branch_name
            hint_text: 'Enter Branch Name'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text:" Enter valid Branch Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True
        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(business_name.text,business_location.text,business_address.text,business_branch_name.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen9>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'STEP-2'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: nearest_location
            hint_text: 'Enter Nearest Location '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Nearest location"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: business_type
            hint_text: 'Enter Business Type'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Type"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        Spinner:
            id: no_of_employees_working
            text: "No of Employees Working"
            values: ["No of Employees Working","<50", "50-100", "100-150", "150-200", ">200"]
            multiline: False
            size_hint: 1 , None
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTextField:
            id: year_of_estd
            hint_text: 'Enter Year of Estd'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Year of Estd"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen8'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(nearest_location.text,business_type.text,no_of_employees_working.text,year_of_estd.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen10>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-3'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: industry_type
            hint_text: 'Enter Industry Type '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Industry Type"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: last_six_months_turnover
            hint_text: 'Enter Last 6 Months Turnover'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid 6 months Turnover"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDLabel:
            text: "Last 6 months Bank Statements"
            font_size: 22
            halign: 'center'

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon5
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label1
                text: 'Upload 6M statement proof'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen9'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(industry_type.text,last_six_months_turnover.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen11>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-4'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: director_name
            hint_text: 'Enter Director Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Director Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: director_mobile_number
            hint_text: 'Enter Director Mobile Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Director Mobile Number"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: din
            hint_text: 'Enter DIN'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid DIN"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: cin
            hint_text: 'Enter CIN'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid CIN"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen10'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(director_name.text,director_mobile_number.text,din.text,cin.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen12>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-5'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: reg_office_address
            hint_text: 'Enter Registered Office Address '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Registration Office Address"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
            markup: True


        MDLabel:
            text: "Proof of verification"
            font_size: 22
            halign: 'center'

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon6
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label1
                text: 'Upload Address Proof'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen11'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(reg_office_address.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen13>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Employment Details'
            font_size: 25
            halign: 'center'
            bold: True
        MDTextField:
            id: company_name
            hint_text: 'Enter Company Name'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Company Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: company_pincode
            hint_text: 'Enter Pincode'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Pincode"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: company_country
            hint_text: 'Enter Country'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Country"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: landmark
            hint_text: 'Enter Landmark'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Landmark"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: business_number
            hint_text: 'Enter Business Phone Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Business Phone Number"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen6'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(company_name.text, company_pincode.text, company_country.text, landmark.text, business_number.text )
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen14>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Employment Details'
            font_size: 25
            halign: 'center'
            bold: True   

        MDTextField:              
            id: annual_salary
            hint_text: 'Enter Annual Salary'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text:  "Enter Valid Annual Salary"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:              
            id: designation
            hint_text: 'Enter Designation'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Designation"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDLabel:
            text: "Upload Employee ID"
            font_size: 18
            halign: 'center'

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  # Adjust size as needed
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1 
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon7
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_1()

            MDLabel:
                id: upload_label1
                text: 'Upload ID'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDLabel:
            text: "Upload Last 6 months Bank Statements"
            font_size: 18
            halign: 'center'

        BoxLayout:
            orientation: 'horizontal'
            padding: "10dp"
            spacing: "10dp"
            size_hint: None, None
            size: dp(200), dp(50)  
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.4  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDIconButton:
                icon: 'upload'
                id: upload_icon8
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  
                size_hint_x: None
                width: dp(24)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.file_manager_open_2()

            MDLabel:
                id: upload_label2
                text: 'Upload Statement'
                halign: 'left'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                size_hint_y: None
                height: dp(36)
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen13'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(annual_salary.text, designation.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen15>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Borrower Registration Form'
            font_size: 25
            halign: 'center'
            bold: True

        Spinner:
            id: marital_status_id
            text: "Please Select Marital Status"
            values: ["Select Marital Status","Married", "Un-Married", "Divorced"]
            size_hint: 1 , None
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen7'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(marital_status_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen16>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-1'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: spouse_name
            hint_text: 'Enter Spouse Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter Valid Spouse Name"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: spouse_date_textfield
            hint_text: " Enter Spouse Birth Date"
            on_focus: root.show_date_picker()
            icon_right: "calendar"
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid date Of Birth"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: spouse_mobile
            hint_text: 'Enter Spouse Mobile No'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Spouse Mobile No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: spouse_profession
            hint_text: 'Enter Spouse Profession '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Spouse Profession"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(spouse_name.text, spouse_date_textfield.text, spouse_mobile.text, spouse_profession.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen17>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Step-2'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: spouse_company_name
            hint_text: 'Enter Spouse Company Name '
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: 'Enter Valid Spouse Company Name '
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: spouse_company_address
            hint_text: 'Enter Spouse Company Address'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Spouse Company Address"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id:  spouse_annual_salary
            hint_text: 'Enter Annual Salary'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: 'Enter valid Annual Salary'
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True
        MDTextField:
            id:spouse_office_no
            hint_text: 'Enter Spouse Office Number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text: "Enter valid Spouse Office No"
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen16'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(spouse_company_name.text, spouse_company_address.text, spouse_annual_salary.text, spouse_office_no.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


<BorrowerScreen18>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Applicant Bank Details'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: account_holder_name
            hint_text: 'Enter Account Holder Name '
            helper_text: 'Enter valid account holder name'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        Spinner:
            id: account_type_id
            text: "Select Account Type Option"
            values: ["Select Account Type Option","Savings Account", "Salary Account", "Current Account", "NRI Account", "Re-Curing Account"]
            size_hint: 1 , None
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTextField:
            id: account_number
            hint_text: 'Enter Account number '
            multiline: False
            helper_text: 'Enter valid Account number'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            helper_text_mode: 'on_focus'
            font_name: "Roboto-Bold"
            bold: True

        MDTextField:
            id: bank_name
            hint_text: 'Enter Bank Name '
            helper_text: 'Enter valid Bank Name'
            multiline: False
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            font_name: "Roboto-Bold"
            bold: True
        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen15'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data(account_holder_name.text, account_type_id.text, account_number.text, bank_name.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""

<BorrowerScreen19>:
    MDRectangleFlatButton:
        text: 'HOME'
        text_color: 0, 0, 0, 1  
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: 0.031, 0.463, 0.91, 1
        pos_hint: {'right': 1, 'top': 1}
        on_release: app.root.current()
        size_hint: (0.1, 0.03)
        font_size: "13sp"
        padding: dp(10)

    BoxLayout:
        orientation: 'vertical'
        padding: "40dp"

        MDLabel:
            text: 'Applicant Bank Details'
            font_size: 25
            halign: 'center'
            bold: True

        MDTextField:
            id: ifsc_code
            hint_text: 'Enter Bank ID '
            multiline: False
            helper_text: 'Enter valid Bank ID'
            helper_text_mode: 'on_focus'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            font_name: "Roboto-Bold"
            bold: True

        Spinner:
            id: salary_id
            text: "Select Salary Paid Option"
            values: ["Salary Paid Option","Cash", "Online"]
            multiline: False
            size_hint: 1 , None
            background_color: (0, 0, 0, 0)
            background_normal: ''
            background_color: 1, 1 ,1, 0 
            color: 0, 0, 0, 1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


        MDTextField:
            id: branch_name
            hint_text: 'Enter Branch Name'
            helper_text: 'Enter valid Branch Name'
            hint_text_mode: 'on_focus'
            multiline: False
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            multiline: False
            font_name: "Roboto-Bold"


        GridLayout:
            cols: 2
            spacing: 30
            padding: 20
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"

            MDRaisedButton:
                text: "Back"
                on_release: app.root.current = 'BorrowerScreen18'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"

            MDRaisedButton:
                text: "Submit"
                on_release: root.go_to_borrower_dashboard(ifsc_code.text, branch_name.text, salary_id.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
        Label:
            text: ""


'''
conn = sqlite3.connect('kivymd.db')
cursor = conn.cursor()



class BorrowerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.on_date_selected)

    def show_date_picker(self):
        self.date_picker.open()

    def on_date_selected(self, instance, the_date, a):
        print(f"Selected date: {the_date, the_date.year}")
        self.ids.date_textfield.text = f'{the_date.year}-{the_date.month}-{the_date.day}'

    def add_data(self, name, gender, email, date_of_birth, mobile_number):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        b = 'borrower'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET name = ?, gender = ?, email = ?, date_of_birth = ?,mobile_number = ?,  user_type = ? WHERE customer_id = ?",
                       (name, gender, email, date_of_birth, mobile_number, b, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen1'


class BorrowerScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET profile_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, alternate_mobile_number, alternate_email):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET alternate_mobile_number = ?, alternate_email = ? WHERE customer_id = ?",
                       (alternate_mobile_number, alternate_email, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen2'


class BorrowerScreen2(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET aadhar_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET pan_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def add_data(self, aadhar_number, pan_number):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET aadhar_number = ?, pan_number = ? WHERE customer_id = ?",
                       (aadhar_number, pan_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen3(Screen):
    def add_data(self, street, city, zip_code, state, country):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute(
            "UPDATE registration_table SET street_name = ?, city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
            (street, city, zip_code, state, country, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen4'


class BorrowerScreen4(Screen):
    def add_data(self, father_name, father_age, father_occupation, father_ph_no):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET father_name = ?, father_age = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
            (father_name, father_age, father_occupation, father_ph_no, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen5'


class BorrowerScreen5(Screen):

    def add_data(self, mother_name, mother_age, mother_occupation, mother_ph_no):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET mother_name = ?, mother_age = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
            (mother_name, mother_age, mother_occupation, mother_ph_no, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen6'


class BorrowerScreen6(Screen):

    def add_data(self, spinner_id):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET proficient_type = ? WHERE customer_id = ?",
            (spinner_id, row_id_list[log_index]))
        conn.commit()
        if spinner_id == 'Student':
            self.manager.current = 'BorrowerScreen7'

        elif spinner_id == 'Business':
            self.manager.current = 'BorrowerScreen8'

        elif spinner_id == 'Employee':
            self.manager.current = 'BorrowerScreen13'
        print(id)


class BorrowerScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET collage_id_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, collage_name, college_address):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET collage_name = ?, college_address = ? WHERE customer_id = ?",
            (collage_name, college_address, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen8(Screen):
    def add_data(self, business_name, business_location, business_address, business_branch_name):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET business_name = ?, business_location = ?, business_address = ?, business_branch_name = ? WHERE customer_id = ?",
            (business_name, business_location, business_address, business_branch_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen9'


class BorrowerScreen9(Screen):
    def add_data(self, nearest_location, business_type, no_of_employees_working, year_of_estd):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET nearest_location = ?, business_type = ?, no_of_employees_working = ?, year_of_estd = ? WHERE customer_id = ?",
            (nearest_location, business_type, no_of_employees_working, year_of_estd, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen10'


class BorrowerScreen10(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, industry_type, last_six_months_turnover):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET industry_type = ?, last_six_months_turnover = ? WHERE customer_id = ?",
            (industry_type, last_six_months_turnover, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen11'


class BorrowerScreen11(Screen):
    def add_data(self, director_name, director_mobile_number, DIN, CIN):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET director_name = ?, director_mobile_number = ?, DIN = ?, CIN = ? WHERE customer_id = ?",
            (director_name, director_mobile_number, DIN, CIN, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen12'


class BorrowerScreen12(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET proof_of_verification_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, registered_office_address):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET registered_office_address = ? WHERE customer_id = ?",
            (registered_office_address, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen13(Screen):
    def add_data(self, company_name, company_pincode, company_country, landmark, business_number):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET company_name = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
            (company_name, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen14'


class BorrowerScreen14(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET employee_id_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def add_data(self, annual_salary, designation):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
            (annual_salary, designation, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen15(Screen):
    def add_data(self, marital_status_id):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET marital_status = ? WHERE customer_id = ?",
            (marital_status_id, row_id_list[log_index]))
        conn.commit()

        if marital_status_id == 'Un-Married':
            self.manager.current = 'BorrowerScreen18'

        elif marital_status_id == 'Married':
            self.manager.current = 'BorrowerScreen16'

        elif marital_status_id == 'Divorced':
            self.manager.current = 'BorrowerScreen18'


class BorrowerScreen16(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.on_date_selected)

    def show_date_picker(self):
        self.date_picker.open()

    def on_date_selected(self, instance, the_date, a):
        print(f"Selected date: {the_date, the_date.year}")
        self.ids.spouse_date_textfield.text = f'{the_date.year}-{the_date.month}-{the_date.day}'

    def add_data(self, spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ?, spouse_profession = ? WHERE customer_id = ?",
            (spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen17'


class BorrowerScreen17(Screen):
    def add_data(self, spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ?, spouse_office_no = ? WHERE customer_id = ?",
            (spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen18'


class BorrowerScreen18(Screen):
    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
            (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'BorrowerScreen19'


class BorrowerScreen19(Screen):
    def go_to_borrower_dashboard(self, bank_id, branch_name, salary_id):
        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE registration_table SET bank_id = ?,salary_id = ?, branch_name = ? WHERE customer_id = ?",
                       (bank_id, branch_name, salary_id, row_id_list[log_index]))
        conn.commit()

        self.manager.current = 'DashboardScreen'