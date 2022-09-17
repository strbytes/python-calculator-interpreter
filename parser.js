const BinaryExpr = require("./expr").BinaryExpr;
const CallExpr = require("./expr").CallExpr;
const Literal = require("./expr").Literal;

/*
 * Built-in operators.
 */
const Terms = ["+", "-"];
const Factors = ["*", "/"];
const Exponents = ["^"];
const Delimiters = ["(", ")"];

/*
 * Covert a TokenBuffer into a nested Expression structure.
 */
function parser(source) {
  let expression = factor(source);
  while (Terms.includes(source.current)) {
    let operator = source.pop();
    let right = factor(source);
    expression = new BinaryExpr(expression, operator, right);
  }
  return expression;
}

function factor(source) {
  let expression = exponent(source);
  while (Factors.includes(source.current)) {
    let operator = source.pop();
    let right = exponent(source);
    expression = new BinaryExpr(expression, operator, right);
  }
  return expression;  
}

function exponent(source) {
  let expression = callExpr(source);
  while (Exponents.includes(source.current)) {
    let operator = source.pop();
    let right = callExpr(source);
    expression = new BinaryExpr(expression, operator, right);
  }
  return expression;  
}

function callExpr(source) {
  if (is_name(source.current) && source.next === "(") {
    let operator = source.pop();
    let operand = literal(source);
    return new CallExpr(operator, operand);
  }
  return literal(source);
}

function literal(source) {
  if (is_literal(source.current) || is_name(source.current)) {
    return new Literal(source.pop());
  // } else if (is_name(source.current) && source.next !== "(") {
  //   return new Literal(source.pop());
  } else if (source.current === "(") {
    source.pop();
    let expression = parser(source);
    if (source.current === ")") {
      source.pop()
    }
    return expression;
  } else {
    throw `Invalid literal ${source.current}`;
  }
}

function is_literal(token) {
  return (typeof token === "number");
}

function is_name(token) {
  return /^[a-zA-Z]+$/.test(token);
}

module.exports = parser;
