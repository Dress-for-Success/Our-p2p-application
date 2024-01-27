from kivy import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3

bd = """
<DashboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Borrower DashBoard"
            elevation: 2
            left_action_items: [['menu', lambda x: app.on_menu_button_press()]]
            right_action_items: [['account', lambda x: root.on_profile_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}

            Button:
                text: "My Commitments"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            Button:
                text: "Opening Balance"
                background_color: 0.529, 0.807, 0.922, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "My Returns"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "New Loan requests"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()


            Button:
                text: "View Loans"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ViewLoansScreen'
            Button:
                text: "Today's Due"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "Application Tracker"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ApplicationTrackerScreen'

            Button:
                text: "Discount Coupons"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "Loan Foreclose"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "View Profile"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

        MDTopAppBar:
            title:"FAQ" 
            custom_action_items:[['help']]

<ProfileScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: 35
                spacing: 20
                size_hint_y: None
                height: self.minimum_height



                CustomIconButton:
                    id: selected_image_button
                    on_release: app.file_manager_open()
                    selected_image_source: "path/to/your/default/image.jpg"
                    size_hint: None, None
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Customer ID '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width


                    MDTextField:
                        id: customer_id
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        readonly: True
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' Full Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        id: edit_button
                        size_hint: None, None
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"


                    MDTextField:
                        id: username
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Profile Status '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width


                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        readonly: True

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Date Of Birth '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:20   
                    Label:
                        text: ' Gender '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
                        text: ' User Age '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Mobile number '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Government ID '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' Pan Number'
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold" 
                        readonly: True         
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:5   
                    Label:
                        text: ' City '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Last Confirm '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Mother Tongue '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Spouse Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Spouse Mobile '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:120   
                    Label:
                        text: ' Spouse Company Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:130   
                    Label:
                        text: ' Spouse Company Address'
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:100   
                    Label:
                        text: ' Spouse Profession '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:40   
                    Label:
                        text: ' User Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:130   
                    Label:
                        text: ' Registration Approve Date '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:10   
                    Label:
                        text: ' About '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Address Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Building Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' House Landmark '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
                        text: ' House No '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
                        text: ' Pincode '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Qualification '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:1
                    Label:
                        text: ' State '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:5   
                    Label:
                        text: ' Street '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Another Email '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Company Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' Organization Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' Employment Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Business No '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:100   
                    Label:
                        text: ' Company Landmark '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' Company Address '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:75   
                    Label:
                        text: ' Annual Salary '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:75   
                    Label:
                        text: ' Designation '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:80   
                    Label:
                        text: ' Account Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Account Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:90   
                    Label:
                        text: ' Account Number '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Branch Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' IFSC Code '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:65  
                    Label:
                        text: ' Salary Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:65   
                    Label:
                        text: ' Select Bank '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:55   
                    Label:
                        text: ' Net Bank '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Father Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' Father Age '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' Mother Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:60   
                    Label:
                        text: ' Mother Age '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:70   
                    Label:
                        text: ' College Name '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:50   
                    Label:
                        text: ' College ID '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:88   
                    Label:
                        text: ' College Address '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True


                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_x: None
                    height: dp(40) 
                    padding:103   
                    Label:
                        text: ' Running Home Loan '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"





<CustomIconButton@MDRectangleFlatButton>:
    selected_image_source: ""
    size_hint: None, None
    size: dp(100), dp(100)
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: 174/255, 214/255, 241/255, 1
        Ellipse:
            size: self.size
            pos: self.pos 
    MDIconButton:
        icon: 'camera-plus'
        on_release: app.file_manager_open()

<ApplicationTrackerScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Application Tracker"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
        BoxLayout:
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)
            MDLabel:
                text: 'Application Received'
                font_size: dp(20)
                bold: True
            MDLabel:
                text: "Congratulations! Your first loan application with P2P has been received. Please wait while we process the loan. You can check the status here"
            MDGridLayout:
                cols: 2

                MDIconButton:
                    icon: "checkbox-marked-circle"
                    theme_text_color: "Custom"

                    text_color: 12/255, 105/255, 171/255, 1
                MDLabel:
                    text: "Application for #loanamount sent"


            MDGridLayout:
                cols: 2

                MDIconButton:
                    icon: "checkbox-marked-circle"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                MDLabel:
                    text: "Waiting for approval"

            MDGridLayout:
                cols: 2

                MDIconButton:
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                MDLabel:
                    text: "Loan is approved for #loanamount"

            MDGridLayout:
                cols: 2

                MDIconButton:
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                MDLabel:
                    text: "Loan is under disbursal process"

            MDGridLayout:
                cols: 2

                MDIconButton:
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                MDLabel:
                    text: "Loan credited to a/c xxxxxxxxxxx"


<ViewLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}

            Button:
                text: "Open Loans"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'OpenLoansScreen'


            Button:
                text: "Closed Loans"
                background_color: 0.529, 0.807, 0.922, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "Approved Loans"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            Button:
                text: "Rejected Loans"
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()


            Button:
                text: "Under Process Loans"
                text_color: 0, 0, 0, 1
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


<OpenLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1 
            padding: dp(50)

            Widget:
                size_hint_y: None
                height: 5
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Change color if needed
                    Line:
                        points: self.x, self.y, self.x + self.width, self.y
            MDGridLayout:
                cols: 4
                padding: dp(15)
                spacing: dp(5)

                MDLabel:
                    text: "Loan ID"
                    size_hint_y: None

                MDLabel:
                    text: "Loan Status"
                MDLabel:
                    text: "Loan ID"
                MDLabel:
                    text: "Loan Status"
            MDGridLayout:
                cols: 4
                padding: dp(15)
                spacing: dp(5)

                MDLabel:
                    text: "Loan ID"

                MDLabel:
                    text: "Loan Status"
                MDLabel:
                    text: "Loan ID"
                MDLabel:
                    text: "Loan Status"



"""

conn = sqlite3.connect('kivymd.db')
cursor = conn.cursor()


class DashboardScreen(Screen):
    def on_profile_button_press(self):
        self.manager.current = 'ProfileScreen'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cursor.execute('select name from registration_table')
        name = cursor.fetchall()
        print(name)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'


class ApplicationTrackerScreen(Screen):
    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'


class ViewLoansScreen(Screen):
    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'


class OpenLoansScreen(Screen):
    def on_back_button_press(self):
        self.manager.current = 'ViewLoansScreen'

class ImageDialogContent(BoxLayout):
    def __init__(self, image_path, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Image(source=image_path))


