def convert_to_meter(ft, inch):
    """convert answer to meter
    receiving two arguments (feet, inches)
    return 1 value (meter) """
    meter1 = ft * 0.3048
    meter2 = inch * 0.0254
    meter = meter1 + meter2
    return meter

if __name__ == "__main__":
    dev_input_ft = int(input("Enter ft: "))
    dev_input_inch = int(input("Enter inch: "))
    dev_ans = convert_to_meter(dev_input_ft, dev_input_inch)
    print("Answer in meter: ", dev_ans)