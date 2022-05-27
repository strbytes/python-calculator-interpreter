# python-calculator-interpreter

A simple calculator interpreter that can evaluate one-line expressions with only primitive operators and numbers. Eventually I want to implement this in JavaScript and allow a user to enter expressions using a web mockup of a calculator, something like a TI-30.

It seems to work right now, accoring roughly to how I remember my middle-school TI-30 and TI-84 working.

To run, run calc.py with Python. Can evaluate simple arithmetic expressions and predefined functions. Do not include whitespace in your expressions. Examples:

> \>1+1

> 2

> \>sqrt(2)

> 1.4142135623730951

> \>1+2log(2)

> 2.386294361119891

> \>(1+2)^2+1

> 10

Grammar specs, roughly speaking, are:

Evaluate arithmetic expressions using standard binary operators and order of operations. e.g., 1 + 2 \* 3 = 7

No whitespace - will need to implement a 'small minus' to indicate negation in the final product.

Allow implicit multiplication - a number or expression end immediately before another number or expression start will automatically multiply those two values. e.g., 2sqrt(4) = 4, sqrt(4)2 = 4, sqrt(4)sqrt(4) = 4

Allow implicit paren closing - If a paren is opened, end the expression with a close but if left unclosed and the expression ends, just evaluate it anyways. e.g., 2sqrt(4 = 4
