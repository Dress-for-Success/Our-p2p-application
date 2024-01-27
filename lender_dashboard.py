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
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line  # Import Color and Line classes

user_helpers1 = """
<LenderDashboard>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1  # Make the size stretchable

        MDTopAppBar:
            title: "Lender DashBoard"
            elevation: 4
            left_action_items: [['menu', lambda x: app.navigation_draw()]]
            right_action_items: [['clock', lambda x: app.navigation_draw()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            size_hint: 1, 1  # Make the size stretchable

            Button:
                text: "View Profile"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ViewProfileScreen'


            Button:
                text: "View Opening Balance"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()
            Button:
                text: "View Available Balance"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "Request Top-up Amount"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "View Loan Request"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "View Loans"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ViewLoansScreen2'

            Button:
                text: "View Loan Extension"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "View Loan Foreclosure"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "Loan Disbursement"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "View Lost Opportunities"
                size_hint_y: 1
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()


        MDTopAppBar:
            title:"FAQ" 
            custom_action_items:[['help']] 

<ViewProfileScreen>
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
                padding: dp(35)
                spacing: 20
                size_hint_y: None
                height: self.minimum_height



                CustomIconButton:
                    id: selected_image_button
                    on_release: app.file_manager_open()
                    selected_image_source: "path/to/your/default/image.jpg"
                    size_hint: None, None
                 
                MDLabel:
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
               
                MDLabel:
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
                 
                MDLabel:
                    text: ' Mobile Number '
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
                    
                    
                 
                MDLabel:
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
                        id: text_input2
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                
                MDLabel:
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
                        id: text_input3
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
  
                MDLabel:
                    text: ' Alternate email '
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
                        id: text_input4
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
 
                MDLabel:
                    text: ' Government ID1 '
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
                        id: text_input5
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True

                MDLabel:
                    text: ' Government ID2 '
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
                        id: text_input6
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True
  
                MDLabel:
                    text: ' Highest Qualification'
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
                        id: text_input7
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold" 
      
                  
                MDLabel:
                    text: ' Street Name '
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
                        id: text_input8
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                 
                MDLabel:
                    text: ' City Name '
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
                        id: text_input8
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                
                MDLabel:
                    text: ' Zipcode '
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
                        id: text_input9
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                  
                MDLabel:
                    text: ' State Name '
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
                        id: text_input10
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Country Name '
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
                        id: text_input11
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Loan Type '
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
                        id: text_input12
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True

                MDLabel:
                    text: ' Investment '
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
                        id: text_input13
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Lending Period '
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
                        id: text_input14
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
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

                    MDTextField:
                        id: text_input15
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True


                MDLabel:
                    text: ' Account Holder Name '
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
                        id: text_input16
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
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
                        id: text_input17
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



                MDLabel:
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
                        id: text_input18
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Bank Name '
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
                        id: text_input19
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Bank ID '
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
                        id: text_input20
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
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
                        id: text_input21
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
        on_release: app.root.file_manager_open()
        
        
        
<ViewLoansScreen2>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1  # Make the size stretchable

        MDTopAppBar:
            title: "View Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            size_hint: 1, 1  # Make the size stretchable

            Button:
                text: "Open Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ViewProfileScreen'


            Button:
                text: "Closed Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()
            Button:
                text: "Approved Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ApprovedLoansScreen'

            Button:
                text: "Rejected Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.open_balance()

            Button:
                text: "All Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: app.root.current = 'ALlLoansScreen'
                
<ALlLoansScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        ScrollView:
            
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                
                
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 0
                        
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 1, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True
                                
                                
                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True

                            MDLabel:
                                text: 'Loan Status'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                size_hint_x: None
                                width: dp(20)
                                bold: True
                        Widget:
                            size_hint_y: None
                            height: dp(2) 
                            canvas:
                                Color:
                                    rgba: 0, 0, 1, 1
                                Line:
                                    width: dp(0.6)  # Set the width of the line to make it bold
                                    points: self.x, self.y, self.x + self.width, self.y

"""
a = 100
for i in range(a):
    user_helpers1 += '''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: label1
                                text: 'LA1001'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                
                            MDLabel:
                                id: label2
                                text: '2000000'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                            

                            MDLabel:
                                id: label3
                                text: 'Under Process'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                            

                            MDIconButton:
                                id: icon1
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                            
    '''

user_helpers1 += '''
<ApprovedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Approved Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

'''


conn = sqlite3.connect('kivymd.db')
cursor = conn.cursor()
class LenderDashboard(Screen):
    def homepage(self):
        self.manager.current = 'MainScreen'

class ALlLoansScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = self.ids.box1.height
        for i in range(a+1):
            h += 150
        self.ids.box1.height = h
        print(h)
    def on_back_button_press(self):
        self.manager.current = 'ViewLoansScreen2'


class ViewProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        cursor.execute('select * from registration_table')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute('select * from registration_table')
        row = cursor.fetchall()

        customer_id = []
        name = []
        gender = []
        date_of_birth = []
        mobile_number = []
        alternate_email = []
        aadhar = []
        pan = []
        qualification = []
        street = []
        city = []
        zip = []
        state = []
        country = []
        loan_type = []
        investment = []
        lending = []
        user_type = []
        acc_name = []
        acc_type = []
        acc_number = []
        bank_name = []
        bank_id = []
        branch_name = []
        for i in row:
            customer_id.append(str(i[0]))
            name.append(str(i[1]))
            gender.append(str(i[5]))
            date_of_birth.append(str(i[6]))
            mobile_number.append(str(i[2]))
            alternate_email.append(str(i[9]))
            aadhar.append(str(i[11]))
            pan.append(str(i[12]))
            qualification.append(str(i[15]))
            street.append(str(i[21]))
            city.append(str(i[23]))
            zip.append(str(i[24]))
            state.append(str(i[24]))
            country.append(str(i[25]))
            loan_type.append(str(i[38]))
            investment.append(str(i[39]))
            lending.append(str(i[40]))
            user_type.append(str(i[-2]))
            acc_name.append(str(i[-35]))
            acc_type.append(str(i[-34]))
            acc_number.append(str(i[-33]))
            bank_name.append(str(i[-32]))
            bank_id.append(str(i[-31]))
            branch_name.append(str(i[-30]))
            print(i)

        self.ids.customer_id.text = str(customer_id[log_index])
        self.ids.username.text = str(name[log_index])
        self.ids.text_input1.text = str(mobile_number[log_index])
        self.ids.text_input2.text = str(date_of_birth[log_index])
        self.ids.text_input3.text = str(gender[log_index])
        self.ids.text_input4.text = str(alternate_email[log_index])
        self.ids.text_input5.text = str(aadhar[log_index])
        self.ids.text_input6.text = str(pan[log_index])
        self.ids.text_input7.text = str(qualification[log_index])
        self.ids.text_input8.text = str(street[log_index])
        self.ids.text_input9.text = str(city[log_index])
        self.ids.text_input10.text = str(state[log_index])
        self.ids.text_input11.text = str(country[log_index])
        self.ids.text_input12.text = loan_type[log_index]
        self.ids.text_input13.text = str(investment[log_index])
        self.ids.text_input14.text = str(lending[log_index])
        self.ids.text_input15.text = user_type[log_index]
        self.ids.text_input16.text = str(acc_name[log_index])
        self.ids.text_input17.text = str(acc_type[log_index])
        self.ids.text_input18.text = str(acc_number[log_index])
        self.ids.text_input19.text = str(bank_name[log_index])
        self.ids.text_input20.text = str(bank_id[log_index])
        self.ids.text_input21.text = str(branch_name[log_index])


        print(street)
    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'

class ViewLoansScreen2(Screen):
    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'

class ApprovedLoansScreen(Screen):
    pass

class ImageDialogContent(BoxLayout):
    def __init__(self, image_path, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Image(source=image_path))

    def file_manager_open(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        self.file_manager.show('/')

    def select_path(self, path):
        self.exit_manager()
        self.display_selected_image(path)

    def display_selected_image(self, image_path):
        dialog = MDDialog(
            title="Selected Image",
            type="custom",
            content_cls=ImageDialogContent(image_path),
            buttons=[
                MDRaisedButton(
                    text="Close", on_release=lambda x: self.close_dialog(dialog)
                )
            ],
        )
        dialog.open()

    def show_image(self, image_name):
        if platform == 'android':
            image_path = f'assets/{image_name}'
        else:
            image_path = image_name
        self.display_selected_image(image_path)

    def close_dialog(self, dialog):
        dialog.dismiss()

    def exit_manager(self, *args):
        self.file_manager.close()

    def toggle_text_field_editable(self, text_input):
        text_input.readonly = not text_input.readonly

