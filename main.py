from gi.repository import Gtk
from eval import simple_eval


class CalcWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Python Calculator")
        self.set_size_request(300, 180)

        self.timeout_id = None

        def calculate(button):
            currentText = self.MainContainer.grid_container.entry.get_text()
            newText = simple_eval(currentText)
            newText = str(newText)
            self.MainContainer.grid_container.entry.set_text(newText)

        def clearText(button):
            self.MainContainer.grid_container.entry.set_text("0")

        def entryText(button):
            buttonLabel = button.button_value

            currentText = self.MainContainer.grid_container.entry.get_text()

            if (currentText == "0"):
                self.MainContainer.grid_container.entry.set_text(buttonLabel)

            else:
                newText = "".join((currentText, buttonLabel))
                self.MainContainer.grid_container.entry.set_text(newText)

        self.MainContainer = Gtk.Grid()
        self.add(self.MainContainer)

        self.MainContainer.grid_container = Gtk.Grid()
        self.MainContainer.grid_container.set_column_homogeneous(True)
        self.MainContainer.grid_container.set_row_homogeneous(True)
        self.MainContainer.attach(self.MainContainer.grid_container, 0, 0, 5, 5)

        self.MainContainer.grid_container.entry = Gtk.Entry()
        self.MainContainer.grid_container.entry.set_text("0")
        self.MainContainer.grid_container.entry.set_editable(True)
        self.MainContainer.grid_container.entry.set_hexpand(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.entry, 0, 0, 5, 1)

        self.MainContainer.grid_container.buttons_row_one = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_one.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_one.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_one, 0, 1, 5, 1)

        self.MainContainer.grid_container.buttons_row_one.button_seven = Gtk.Button("7")
        self.MainContainer.grid_container.buttons_row_one.button_seven.button_value = "7"
        self.MainContainer.grid_container.buttons_row_one.button_seven.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_one.attach(self.MainContainer.grid_container.buttons_row_one.button_seven, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_one.button_eight = Gtk.Button("8")
        self.MainContainer.grid_container.buttons_row_one.button_eight.button_value = "8"
        self.MainContainer.grid_container.buttons_row_one.button_eight.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_one.attach(self.MainContainer.grid_container.buttons_row_one.button_eight, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_one.button_nine = Gtk.Button("9")
        self.MainContainer.grid_container.buttons_row_one.button_nine.button_value = "9"
        self.MainContainer.grid_container.buttons_row_one.button_nine.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_one.attach(self.MainContainer.grid_container.buttons_row_one.button_nine, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_one.button_multiply = Gtk.Button("X")
        self.MainContainer.grid_container.buttons_row_one.button_multiply.button_value = "*"
        self.MainContainer.grid_container.buttons_row_one.button_multiply.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_one.attach(self.MainContainer.grid_container.buttons_row_one.button_multiply, 3, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_one.button_divide = Gtk.Button("÷")
        self.MainContainer.grid_container.buttons_row_one.button_divide.button_value = "/"
        self.MainContainer.grid_container.buttons_row_one.button_divide.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_one.attach(self.MainContainer.grid_container.buttons_row_one.button_divide, 4, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_two = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_two.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_two.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_two, 0, 2, 5, 1)

        self.MainContainer.grid_container.buttons_row_two.button_four = Gtk.Button("4")
        self.MainContainer.grid_container.buttons_row_two.button_four.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_two.button_four.button_value = "4"
        self.MainContainer.grid_container.buttons_row_two.attach(self.MainContainer.grid_container.buttons_row_two.button_four, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_two.button_five = Gtk.Button("5")
        self.MainContainer.grid_container.buttons_row_two.button_five.button_value = "5"
        self.MainContainer.grid_container.buttons_row_two.button_five.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_two.attach(self.MainContainer.grid_container.buttons_row_two.button_five, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_two.button_six = Gtk.Button("6")
        self.MainContainer.grid_container.buttons_row_two.button_six.button_value = "6"
        self.MainContainer.grid_container.buttons_row_two.button_six.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_two.attach(self.MainContainer.grid_container.buttons_row_two.button_six, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_two.button_plus = Gtk.Button("+")
        self.MainContainer.grid_container.buttons_row_two.button_plus.button_value = "+"
        self.MainContainer.grid_container.buttons_row_two.button_plus.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_two.attach(self.MainContainer.grid_container.buttons_row_two.button_plus, 3, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_two.button_minus = Gtk.Button("-")
        self.MainContainer.grid_container.buttons_row_two.button_minus.button_value = "-"
        self.MainContainer.grid_container.buttons_row_two.button_minus.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_two.attach(self.MainContainer.grid_container.buttons_row_two.button_minus, 4, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_three = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_three.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_three.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_three, 0, 3, 5, 1)

        self.MainContainer.grid_container.buttons_row_three.button_one = Gtk.Button("1")
        self.MainContainer.grid_container.buttons_row_three.button_one.button_value = "1"
        self.MainContainer.grid_container.buttons_row_three.button_one.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_three.attach(self.MainContainer.grid_container.buttons_row_three.button_one, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_three.button_two = Gtk.Button("2")
        self.MainContainer.grid_container.buttons_row_three.button_two.button_value = "2"
        self.MainContainer.grid_container.buttons_row_three.button_two.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_three.attach(self.MainContainer.grid_container.buttons_row_three.button_two, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_three.button_three = Gtk.Button("3")
        self.MainContainer.grid_container.buttons_row_three.button_three.button_value = "3"
        self.MainContainer.grid_container.buttons_row_three.button_three.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_three.attach(self.MainContainer.grid_container.buttons_row_three.button_three, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_three.button_no_remain = Gtk.Button("//")
        self.MainContainer.grid_container.buttons_row_three.button_no_remain.button_value = "//"
        self.MainContainer.grid_container.buttons_row_three.button_no_remain.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_three.attach(self.MainContainer.grid_container.buttons_row_three.button_no_remain, 3, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_three.button_just_remain = Gtk.Button("MOD")
        self.MainContainer.grid_container.buttons_row_three.button_just_remain.button_value = "%"
        self.MainContainer.grid_container.buttons_row_three.button_just_remain.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_three.attach(self.MainContainer.grid_container.buttons_row_three.button_just_remain, 4, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_four = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_four.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_four.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_four, 0, 4, 5, 1)

        self.MainContainer.grid_container.buttons_row_four.button_decimal_point = Gtk.Button(".")
        self.MainContainer.grid_container.buttons_row_four.button_decimal_point.button_value = "."
        self.MainContainer.grid_container.buttons_row_four.button_decimal_point.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_four.attach(self.MainContainer.grid_container.buttons_row_four.button_decimal_point, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_four.button_zero = Gtk.Button("0")
        self.MainContainer.grid_container.buttons_row_four.button_zero.button_value = "0"
        self.MainContainer.grid_container.buttons_row_four.button_zero.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_four.attach(self.MainContainer.grid_container.buttons_row_four.button_zero, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_four.button_clear = Gtk.Button("A/C")
        self.MainContainer.grid_container.buttons_row_four.button_clear.connect("clicked", clearText)
        self.MainContainer.grid_container.buttons_row_four.attach(self.MainContainer.grid_container.buttons_row_four.button_clear, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_four.button_enter = Gtk.Button("Enter")
        self.MainContainer.grid_container.buttons_row_four.button_enter.connect("clicked", calculate)
        self.MainContainer.grid_container.buttons_row_four.attach(self.MainContainer.grid_container.buttons_row_four.button_enter, 3, 0, 2, 1)

        self.MainContainer.grid_container.buttons_row_five = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_five.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_five.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_five, 0, 5, 5, 1)

        self.MainContainer.grid_container.buttons_row_five.button_power = Gtk.Button("**")
        self.MainContainer.grid_container.buttons_row_five.button_power.button_value = "**"
        self.MainContainer.grid_container.buttons_row_five.button_power.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_five.attach(self.MainContainer.grid_container.buttons_row_five.button_power, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_five.button_bitwise_invert = Gtk.Button("~")
        self.MainContainer.grid_container.buttons_row_five.button_bitwise_invert.button_value = "~"
        self.MainContainer.grid_container.buttons_row_five.button_bitwise_invert.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_five.attach(self.MainContainer.grid_container.buttons_row_five.button_bitwise_invert, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_five.button_bitwise_or = Gtk.Button("|")
        self.MainContainer.grid_container.buttons_row_five.button_bitwise_or.button_value = "|"
        self.MainContainer.grid_container.buttons_row_five.button_bitwise_or.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_five.attach(self.MainContainer.grid_container.buttons_row_five.button_bitwise_or, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_five.button_lper = Gtk.Button("(")
        self.MainContainer.grid_container.buttons_row_five.button_lper.button_value = "("
        self.MainContainer.grid_container.buttons_row_five.button_lper.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_five.attach(self.MainContainer.grid_container.buttons_row_five.button_lper, 3, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_five.button_rper = Gtk.Button(")")
        self.MainContainer.grid_container.buttons_row_five.button_rper.button_value = ")"
        self.MainContainer.grid_container.buttons_row_five.button_rper.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_five.attach(self.MainContainer.grid_container.buttons_row_five.button_rper, 4, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_six = Gtk.Grid()
        self.MainContainer.grid_container.buttons_row_six.set_column_homogeneous(True)
        self.MainContainer.grid_container.buttons_row_six.set_row_homogeneous(True)
        self.MainContainer.grid_container.attach(self.MainContainer.grid_container.buttons_row_six, 0, 6, 5, 1)

        self.MainContainer.grid_container.buttons_row_six.button_and = Gtk.Button("&")
        self.MainContainer.grid_container.buttons_row_six.button_and.button_value = " & "
        self.MainContainer.grid_container.buttons_row_six.button_and.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_six.attach(self.MainContainer.grid_container.buttons_row_six.button_and, 0, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_six.button_is = Gtk.Button("IS")
        self.MainContainer.grid_container.buttons_row_six.button_is.button_value = " is "
        self.MainContainer.grid_container.buttons_row_six.button_is.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_six.attach(self.MainContainer.grid_container.buttons_row_six.button_is, 1, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_six.button_lshift = Gtk.Button("<<")
        self.MainContainer.grid_container.buttons_row_six.button_lshift.button_value = " << "
        self.MainContainer.grid_container.buttons_row_six.button_lshift.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_six.attach(self.MainContainer.grid_container.buttons_row_six.button_lshift, 2, 0, 1, 1)

        self.MainContainer.grid_container.buttons_row_six.button_rshift = Gtk.Button(">>")
        self.MainContainer.grid_container.buttons_row_six.button_rshift.button_value = " >> "
        self.MainContainer.grid_container.buttons_row_six.button_rshift.connect("clicked", entryText)
        self.MainContainer.grid_container.buttons_row_six.attach(self.MainContainer.grid_container.buttons_row_six.button_rshift, 3, 0, 1, 1)


calc = CalcWindow()
calc.connect("delete-event", Gtk.main_quit)
calc.show_all()
Gtk.main()