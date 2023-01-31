import functions
import PySimpleGUI as sg

label1 = sg.Text("Enter feet")
input1 = sg.Input(key="this_feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="this_inches")

button_convert=sg.Button("Convert")
output_meter = sg.Text(key="output", text_color="green")

convertor_layout = [[label1, input1], [label2, input2], [button_convert, output_meter]]

window = sg.Window ("Convertor", layout=convertor_layout, )

while True:
    event, value = window.read()
    print("1.event:", event)
    print("2.value: ", value)

    cal_feet = int(value["this_feet"])
    cal_inches = int(value["this_inches"])

    cal_meters = functions.convert_to_meter(cal_feet,cal_inches)

    window["output"].update(value=str(cal_meters)+" meters")

    match event:
        case sg.WIN_CLOSED:
            break

window.close()


