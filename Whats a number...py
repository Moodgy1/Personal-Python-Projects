import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkfont

class NumberDescriptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Description App")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=12)

        self.number_label = tk.Label(
            self.master, text="Enter a number:", font=self.custom_font, bg="#f0f0f0"
        )
        self.number_label.pack(pady=10)

        self.number_entry = tk.Entry(
            self.master, font=self.custom_font, width=10, justify="center"
        )
        self.number_entry.pack(pady=5)

        self.describe_button = tk.Button(
            self.master,
            text="Describe Number",
            font=self.custom_font,
            command=self.describe_number,
            bg="#4CAF50",
            fg="white",
        )
        self.describe_button.pack(pady=5)

        self.description_text = scrolledtext.ScrolledText(
            self.master,
            width=60,
            height=15,
            font=self.custom_font,
            wrap=tk.WORD,
            state="disabled",
        )
        self.description_text.pack(pady=10)

    def describe_number(self):
        try:
            number = int(self.number_entry.get())
            if abs(number) > 1_000_000_000:
                raise ValueError("Number out of range. Please enter a number between 0 and 1,000,000,000.")
            self.description_text.config(state="normal")
            self.description_text.delete(1.0, tk.END)
            descriptions = [
                f"The number itself: {number}",
                f"The position of the number in a sequence: {self.ordinal(number)}",
                f"The number written out in words: {self.number_to_words(number)}",
                f"Even: {self.is_even(number)}, Odd: {self.is_odd(number)}",
                f"Prime: {self.is_prime(number)}, Composite: {self.is_composite(number)}",
                f"Positive: {self.is_positive(number)}, Negative: {self.is_negative(number)}, Zero: {self.is_zero(number)}",
                f"Integer: {self.is_integer(number)}, Decimal: Not Applicable, Fraction: Not Applicable",
                f"Rational: {self.is_rational(number)}, Irrational: {self.is_irrational(number)}",
                f"Real: {self.is_real(number)}, Imaginary: Not Applicable, Complex: Not Applicable",
                f"The distance of the number from zero on the number line: {self.absolute_value(number)}",
                f"Scientific Notation: {self.scientific_notation(number)}",
                f"Factors: {self.factors(number)}",
                f"Multiples (1-10): {self.multiples(number)}",
                f"Divisibility: {self.divisibility(number)}",
                f"Powers: {self.powers(number)}",
                f"Roots: {self.roots(number)}",
                f"Reciprocal: {self.reciprocal(number)}",
                f"Surd: {self.surd(number)}",
                f"Fibonacci: {self.is_fibonacci(number)}",
                f"Perfect Number: {self.is_perfect(number)}",
                f"Deficiency: {self.deficiency(number)}",
                f"Mersenne Prime: {self.is_mersenne_prime(number)}",
                f"Abundancy Index: {self.abundancy_index(number)}",
                f"Aliquot Sum: {self.aliquot_sum(number)}",
                f"Narcissistic: {self.is_narcissistic(number)}",
            ]
            if abs(number) <= 10_000_000:
                descriptions.append(f"Taxicab Number: {self.is_taxicab_number(number)}")
            for desc in descriptions:
                self.description_text.insert(tk.END, desc + "\n\n")
            self.description_text.config(state="disabled")
        except ValueError as e:
            self.description_text.config(state="normal")
            self.description_text.delete(1.0, tk.END)
            self.description_text.insert(tk.END, str(e))
            self.description_text.config(state="disabled")

    def ordinal(self, num):
        if 10 <= num % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
        return str(num) + suffix

    def number_to_words(self, num):
        under_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        above_100 = {100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}

        if num < 20:
            return under_20[int(num)]
        if num < 100:
            return tens[int(num) // 10] + ("" if num % 10 == 0 else " " + under_20[int(num) % 10])
        # find the appropriate pivot
        pivot = max([key for key in above_100.keys() if key <= num])
        return (
            self.number_to_words(num // pivot)
            + " "
            + above_100[pivot]
            + ("" if num % pivot == 0 else " " + self.number_to_words(num % pivot))
        )

    def is_even(self, num):
        return num % 2 == 0

    def is_odd(self, num):
        return not self.is_even(num)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_composite(self, num):
        return not self.is_prime(num) and num > 1

    def is_positive(self, num):
        return num > 0

    def is_negative(self, num):
        return num < 0

    def is_zero(self, num):
        return num == 0

    def is_integer(self, num):
        return num == int(num)

    def is_decimal(self, num):
        return False

    def is_fraction(self, num):
        return False

    def is_rational(self, num):
        return num == int(num) or num == round(num)

    def is_irrational(self, num):
        return not self.is_rational(num)

    def is_real(self, num):
        return num == int(num) or num == round(num)

    def is_imaginary(self, num):
        return not self.is_real(num) and num != 0

    def is_complex(self, num):
        return self.is_real(num) or self.is_imaginary(num)

    def absolute_value(self, num):
        return abs(num)

    def scientific_notation(self, num):
        return f"{num:.2e}"

    def factors(self, num):
        factors_list = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors_list.append(i)
                if i != num // i:
                    factors_list.append(num // i)
        return sorted(factors_list)

    def multiples(self, num):
        multiples_list = [num * i for i in range(1, 11)]
        return multiples_list

    def divisibility(self, num):
        divisibility_list = [i for i in range(2, num) if num % i == 0]
        return divisibility_list

    def powers(self, num):
        square = num ** 2
        cube = num ** 3
        higher_powers = [num ** i for i in range(4, 11)]  # Higher powers up to the 10th
        return f"Square: {square}, Cube: {cube}, Higher Powers: {higher_powers}"

    def roots(self, num):
        root = num ** 0.5
        cube_root = num ** (1 / 3)
        higher_roots = [num ** (1 / i) for i in range(4, 11)]  # Higher roots up to the 10th
        return f"Square Root: {root}, Cube Root: {cube_root}, Higher Roots: {higher_roots}"

    def reciprocal(self, num):
        if num != 0:
            return 1 / num
        return "Undefined"

    def surd(self, num):
        return f"√{num}"

    def is_fibonacci(self, num):
        def is_perfect_square(x):
            return int(x ** 0.5) ** 2 == x

        return is_perfect_square(5 * num ** 2 + 4) or is_perfect_square(5 * num ** 2 - 4)

    def is_perfect(self, num):
        if num < 1:
            return False
        return sum(self.factors(num)[:-1]) == num

    def deficiency(self, num):
        if num < 1:
            return "Undefined"
        return sum(self.factors(num)[:-1]) - num

    def is_mersenne_prime(self, num):
        if num < 2:
            return False
        m = num + 1
        return (m & (m - 1)) == 0 and self.is_prime(num)

    def abundancy_index(self, num):
        if num == 0:
            return "Undefined"
        return sum(self.factors(num)) / num

    def aliquot_sum(self, num):
        return sum(self.factors(num)[:-1])

    def is_narcissistic(self, num):
        num_str = str(num)
        num_len = len(num_str)
        return num == sum(int(digit) ** num_len for digit in num_str)

    def is_taxicab_number(self, num):
        if abs(num) > 10_000_000:
            return "Calculation skipped for large number"
        count = 0
        for x in range(1, int(num ** (1 / 3)) + 1):
            for y in range(x, int(num ** (1 / 3)) + 1):
                if x ** 3 + y ** 3 == num:
                    count += 1
                    if count > 1:
                        return True
        return False

def main():
    root = tk.Tk()
    app = NumberDescriptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

#Made By: Mohamaed
#Special thanks to Asser, Ezz, and Adam
#This code is licensed under the MIT License.
#https://opensource.org/licenses/MIT