const Globals = {
    "+": (x, y) => x + y,
    "-": (x, y) => x - y,
    "*": (x, y) => x * y,
    "/": (x, y) => x / y,
    "^": Math.pow,
    "log": Math.log,
    "sqrt": Math.sqrt,
    "neg": (x) => -x,
    "pi": Math.PI,
    "e": Math.E,
}

class Expression {
  #args;
  constructor(...args) {
    this.#args = args;
  }
  
  eval() {
    throw "Superclass method not implemented"
  }
  
  toString() {
    return this.constructor.name + "(" + this.#args + ")";
  }
}

class BinaryExpr extends Expression {
  #left;
  #operator;
  #right;

  constructor(left, operator, right) {
    super(left, operator, right);
    this.#left = left;
    this.#operator = operator;
    this.#right = right;
  }
  
  eval() {
    let left = this.#left.eval();
    let operator = Globals[this.#operator];
    let right = this.#right.eval();
    return operator(left, right);
  }
}

class CallExpr extends Expression {
  #operator;
  #operand;
  
  constructor(operator, operand) {
    super(operator, operand);
    this.#operator = operator;
    this.#operand = operand;
  }
  
  eval() {
    let operator = Globals[this.#operator];
    let operand = this.#operand.eval();
    return operator(operand);
  }
}

class Literal extends Expression {
  #value;
  
  constructor(value) {
    super(value);
    this.#value = value;
  }

  eval() {
    if (typeof this.#value == 'number') {
      return this.#value;
    } else {
      return Globals[this.#value];
    }
  }
}

module.exports = {BinaryExpr, CallExpr, Literal};

