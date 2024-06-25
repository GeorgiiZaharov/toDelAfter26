import re
def extract_numbers_before_x(expression):# вытасивает кооэфиценты перед x из строки
    return re.findall(r'([-+]?\d+)x', expression)

def extract_integers(expression):# вытасивает кооэфиценты НЕ перед x из строки
    return re.findall(r'([-+]?\d+)(?!x)', expression)

task =  "3x+34=2x+1"
# ставим кооэфиценты перед x
task = task.replace("+x", "+1x")
task = task.replace("-x", "-1x")
# делим на 2 части (right hand, left hand)
lh, rh = task.split('=')
if lh.startswith("x"):
    lh = "1" + lh
if rh.startswith("x"):
    rh = "1" + rh

# собираем кооэфиценты при x в одну сторону
cofs_with_x = eval(f"0 + {''.join(extract_numbers_before_x(lh))} - (0 + {''.join(extract_numbers_before_x(rh))} + 0)")

# без x в другую
cofs_without_x = eval(f"0 + {''.join(extract_integers(rh))} - (0 + {''.join(extract_integers(lh))} + 0)")

if cofs_with_x == 0:
    if cofs_without_x == 0:
        print("UNLIM")
    else:
        print("NO RESULT")
else:
    print(f"x={cofs_without_x/cofs_with_x}")
