import random
import string
from math import radians, sin, cos, tan, asin, acos, atan
from decimal import Decimal


# region Global Variables

ONEPLACE = Decimal(10) ** -1
TWOPLACES = Decimal(10) ** -2
THREEPLACES = Decimal(10) ** -3

rounding_num = THREEPLACES

separators = {
		0: "--------------------",
		1: "-Input--------------",
		2: "-Output-------------",
		3: "-Commands-----------"
}

# endregion


# region Utility Functions

def separator(separator_index):
	print("")
	print(separators[separator_index])
	print("")


def add(x, y, fp=rounding_num):
	return Decimal(x + y).quantize(fp)


def sub(x, y, fp=rounding_num):
	return Decimal(x - y).quantize(fp)


def mul(x, y, fp=rounding_num):
	return Decimal(x * y).quantize(fp)


def div(x, y, fp=rounding_num):
	try:
		val = Decimal(x / y).quantize(fp)
	except ZeroDivisionError:
		val = 0
	return val


def qnt(x, fp=rounding_num):
	return Decimal(x).quantize(fp)

# endregion


# region Main Functions

def basic_calc():
	separator(1)

	print("Enter Number 1:")
	num1 = Decimal(float(input("--> ")))

	print("Enter Number 2:")
	num2 = Decimal(float(input("--> ")))

	separator(2)

	print("Addition = " + str(add(num1, num2)))
	print("Subtraction = " + str(sub(num1, num2)))
	print("Multiplication = " + str(mul(num1, num2)))
	try:
		print("Division = " + str(div(num1, num2)))
	except ZeroDivisionError:
		print("Division = ZeroDivisionError")

	separator(0)


def tax_calc():
	separator(1)

	print("Enter Money Amount:")
	money_amount = Decimal(float(input("--> ")))

	print("Enter Tax Percent:")
	tax_percent = Decimal(float(input("--> ")) / 100)

	separator(2)

	tax_amount = mul(money_amount, tax_percent)
	total_amount = add(money_amount, tax_amount)

	print("Tax amount = " + str(tax_amount) + "$")
	print("Total amount = " + str(total_amount) + "$")

	separator(2)


def compound_interest():
	separator(1)

	print("Enter the Principal:")
	principal = float(input("--> "))

	print("Enter the Rate (15 = 15%):")
	rate = float(input("--> "))

	print("Enter Number of Times Per Year:")
	num_times = float(input("--> "))

	print("Enter Time Number:")
	time = float(input("--> "))

	separator(2)

	amount = principal * pow((1 + (rate / num_times)), num_times * time)
	print("Compound Interest Amount = ", amount)

	total_amount = principal + amount
	print("Total Amount = ", total_amount)

	separator(0)


def pop_change():
	separator(1)

	print("Enter Base Population:")
	base_population = Decimal(float(input("--> ")))

	print("Enter Rate of Change (1.4 = 1.4%):")
	rate_of_change = Decimal(float(input("--> ")) / 100)

	separator(2)

	annual = round(mul(base_population, rate_of_change, TWOPLACES))
	monthly = round(div(annual, 12, TWOPLACES))
	weekly = round(div(annual, 52, TWOPLACES))
	daily = round(div(annual, 365, TWOPLACES))

	print("Annual amount = " + str(annual))
	print("Monthly amount = " + str(monthly))
	print("Weekly amount = " + str(weekly))
	print("Daily amount = " + str(daily))

	separator(0)


def sal_calc():
	separator(1)

	print("Enter the input type: \n'a' = Annual \n'm' = monthly \n'bm' = Bi-Monthly \n'w' = Weekly \n'bw' = Bi-Weekly\n")

	input_type = input("--> ")

	if input_type == 'a':
		print("Enter an Annual Salary:")
		num = float(input("--> "))

		m = div(num, 12)
		bm = div(num, 24)
		w = div(num, 52)
		bw = div(num, 26)

		print("Monthly Salary = " + str(qnt(m)))
		print("Bi-Monthly Salary = " + str(qnt(bm)))
		print("Weekly Salary = " + str(qnt(w)))
		print("Bi-Weekly Salary = " + str(qnt(bw)))
	elif input_type == 'm':
		print("Enter a Monthly Salary:")
		num = float(input("--> ")) * 12

		a = num
		bm = div(num, 24)
		w = div(num, 52)
		bw = div(num, 26)

		print("Annual Salary = " + str(qnt(a)))
		print("Bi-Monthly Salary = " + str(qnt(bm)))
		print("Weekly Salary = " + str(qnt(w)))
		print("Bi-Weekly Salary = " + str(qnt(bw)))
	elif input_type == 'bm':
		print("Enter a Bi-Monthly Salary:")
		num = float(input("--> ")) * 24

		a = num
		m = div(num, 12)
		w = div(num, 52)
		bw = div(num, 26)

		print("Annual Salary = " + str(qnt(a)))
		print("Monthly Salary = " + str(qnt(m)))
		print("Weekly Salary = " + str(qnt(w)))
		print("Bi-Weekly Salary = " + str(qnt(bw)))
	elif input_type == 'w':
		print("Enter a Weekly Salary:")
		num = float(input("--> ")) * 52

		a = num
		m = div(num, 12)
		bm = div(num, 24)
		bw = div(num, 26)

		print("Annual Salary = " + str(qnt(a)))
		print("Monthly Salary = " + str(qnt(m)))
		print("Bi-Monthly Salary = " + str(qnt(bm)))
		print("Bi-Weekly Salary = " + str(qnt(bw)))
	elif input_type == 'bw':
		print("Enter a Bi-Weekly Salary:")
		num = float(input("--> ")) * 26

		a = num
		m = div(num, 12)
		bm = div(num, 24)
		w = div(num, 52)

		print("Annual Salary = " + str(qnt(a)))
		print("Monthly Salary = " + str(qnt(m)))
		print("Bi-Monthly Salary = " + str(qnt(bm)))
		print("Weekly Salary = " + str(qnt(w)))
	else:
		print("Enter an annual salary:")
		num = float(input("--> "))

		m = div(num, 12)
		bm = div(num, 24)
		w = div(num, 52)
		bw = div(num, 26)

		print("Monthly Salary = " + str(qnt(m)))
		print("Bi-Monthly Salary = " + str(qnt(bm)))
		print("Weekly Salary = " + str(qnt(w)))
		print("Bi-Weekly Salary = " + str(qnt(bw)))


def sct():
	separator(1)

	print("Enter an Angle:")
	angle = Decimal(radians(float(input("--> "))))

	separator(2)

	ang_sin = sin(angle)
	ang_cos = cos(angle)
	ang_tan = tan(angle)

	print("Sine = " + str(qnt(ang_sin)))
	print("Cosine = " + str(qnt(ang_cos)))
	print("Tangent = " + str(qnt(ang_tan)))

	separator(0)


def sct2():
	separator(1)

	print("Enter an Angle:")
	angle = Decimal(radians(float(input("--> "))))

	separator(2)

	ang_asin = asin(angle)
	ang_acos = acos(angle)
	ang_atan = atan(angle)

	print("Arc Sine = " + str(qnt(ang_asin)))
	print("Arc Cosine = " + str(qnt(ang_acos)))
	print("Arc Tangent = " + str(qnt(ang_atan)))

	separator(0)


def c2f():
	separator(1)

	print("Enter Temperature in Centigrade:")
	centigrade = float(input("--> "))

	separator(2)

	fahrenheit_calc = 1.8 * centigrade + 32
	print(str(qnt(centigrade)) + " Centigrade in Fahrenheit = " + str(qnt(fahrenheit_calc)))

	separator(0)


def f2c():
	separator(1)

	print("Enter Temperature in Fahrenheit: ")
	fahrenheit = float(input("--> "))

	separator(2)

	centigrade_calc = (fahrenheit - 32) * (5.0 / 9.0)
	print(str(qnt(fahrenheit)) + " Fahrenheit in Centigrade = " + str(qnt(centigrade_calc)))

	separator(0)


def rand_num():
	separator(1)

	print("Enter Min Number:")
	min_num = float(input("--> "))

	print("Enter Max Number:")
	max_num = float(input("--> "))

	print("Enter Number Count:")
	count = int(input("--> "))

	separator(2)

	roll_array = []
	for i in range(0, count):
		roll = random.randrange(min_num, max_num + 1)
		roll_array.append(roll)

	print("Unsorted List:")
	print(str(roll_array))

	print("")

	roll_array.sort()
	print("Sorted List:")
	print(str(roll_array))

	print("")

	for i in range(int(min_num), int(max_num + 1)):
		print(str(i) + " appears " + str(roll_array.count(i)) + " times")

	separator(0)


# Only works in python 3.6 or later
def rpg():
	try:
		import secrets

		alphabet = string.ascii_letters + string.digits
		passwords = []

		separator(1)

		try:
			pass_length = int(input("Enter password length --> "))
		except ValueError:
			pass_length = 8
		if pass_length == 0:
			pass_length = 8
		password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
		passwords.append(password)

		separator(2)
		print(passwords[-1])
		separator(0)

		with open("Generated Passwords.txt", "a") as f:
			print("", file = f)
			print(passwords[-1], file = f)

	except ImportError:
		print("")
		print("The Random Password Generator only works in python 3.6 or newer!")
		print("")

# endregion


if __name__ == '__main__':

	loop = True

	def cli_help():
		separator(3)
		for i in help_list:
			print(i, "=", help_list[i])
		separator(0)


	commands = {
		"bc": basic_calc,
		"tc": tax_calc,
		"ci": compound_interest,
		"pc": pop_change,
		"sc": sal_calc,
		"sct": sct,
		"sct2": sct2,
		"c2f": c2f,
		"f2c": f2c,
		"numgen": rand_num,
		"rpg": rpg,
		"help": cli_help,
		"quit": quit
	}

	help_list = {
		"bc": "Basic Calculator",
		"tc": "Tax Calculator",
		"ci": "Compound Interest Calculator",
		"pc": "Population Change Calculator",
		"sc": "Basic Salary Calculator",
		"sct": "Sin, Cos, Tan",
		"sct2": "ASin, ACos, ATan",
		"c2f": "Centigrade to Fahrenheit",
		"f2c": "Fahrenheit to Centigrade",
		"numgen": "Random Number Generator",
		"rpg": "Random Password Generator",
		"help": "Shows this list",
		"quit": "Quit the application"
	}

	while loop:
		print("Enter a command: ")
		user_input = input("--> ")

		try:
			func = commands[user_input]
			func()
		except KeyError:
			print("")
			if user_input == "":
				print("Not a valid command!")
			else:
				print(user_input + " is not a valid command!")
			print("")
