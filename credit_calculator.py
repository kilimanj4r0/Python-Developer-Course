import math as m
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=['diff', 'annuity'], default='')
parser.add_argument("--principal", type=int, default=0)
parser.add_argument("--payment", type=int, default=0)
parser.add_argument("--periods", type=int, default=0)
parser.add_argument("--interest", type=float, default=0.0)
args = parser.parse_args()

global interest
interest = args.interest / 100 * (1 / 12)

def testing():
    test = ''
    if args.type != 'diff' and args.type != 'annuity':
        return False
    if not args.principal:
        test += "0"
    if not args.payment:
        test += "0"
    if not args.periods:
        test += "0"
    if not args.interest:
        return False
    if test.count('0') >= 2:
        return False
    elif args.type == 'diff' and args.payment:
        return False
    elif args.principal < 0 or args.payment < 0 or args.periods < 0 or args.interest < 0:
        return False
    else:
        return True

def cprincipal():
    payment = args.payment
    periods = args.periods
    principal = payment / ((interest * m.pow((1 + interest), periods)) / (m.pow((1 + interest), periods) - 1))
    print(f"Your credit principal = {m.ceil(principal)}!")
    overpayment = payment * periods - m.ceil(principal)
    print(f'Overpayment = {overpayment}')

def payment():
    principal = args.principal
    periods = args.periods
    payment = ((interest * m.pow((1 + interest), periods)) / (m.pow((1 + interest), periods) - 1)) * principal
    print(f"Your annuity payment = {m.ceil(payment)}!")
    overpayment = m.ceil(payment) * periods - principal
    print(f'Overpayment = {overpayment}')

def periods():
    principal = args.principal
    payment = args.payment
    periods = m.ceil(m.log((payment / (payment - interest * principal)), (1 + interest)))
    years = periods // 12
    months = periods % 12
    if years == 0:
        print(f"You need {months} months to repay this credit!")
    elif months == 0:
        print(f"You need {years} years to repay this credit!")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")
    overpayment = payment * periods - principal
    print(f'Overpayment = {overpayment}')

def dpayment():
    principal = args.principal
    periods = args.periods
    overpayment = -principal
    for x in range(1, periods + 1):
        xpayment = m.ceil(principal / periods + principal * interest * (1 - (x - 1) / periods))
        overpayment += xpayment
        print(f"Month {x}: paid out {xpayment}")
    print()
    print(f'Overpayment = {overpayment}')


if testing():
    if args.type == 'annuity':
        if not args.principal:
            cprincipal()
        elif not args.periods:
            periods()
        elif not args.payment:
            payment()
    else:
        if not args.principal:
            cprincipal()
        elif not args.periods:
            periods()
        elif not args.payment:
            dpayment()
else:
    print("Incorrect parameters")
