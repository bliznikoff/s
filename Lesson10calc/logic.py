import calc, convert

def button_click(text):
    primer = convert.convert_expression(text)
    result = calc.Calc(primer)
    return result