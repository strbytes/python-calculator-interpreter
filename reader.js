/* Token groups. */
// https://hasnode.byrayray.dev/how-to-generate-an-alphabet-array-with-javascript
const Letters = [...Array(26)].map((_, i) => String.fromCharCode(i + 97)); 
const Numbers = [...Array(10)].map((_, i) => i.toString());
const Terms = ["+", "-"];
const Factors = ["*", "/"];
const Exponents = ["^", "**"];
const Delimiters = ["(", ")"];
const Operators = Terms.concat(Factors).concat(Exponents).concat(Delimiters);

/* Convert an input string into a Buffer of tokens. */
function lexer(s) {
  // const tokens = Buffer();
  const tokens = [];
  let i = 0;
  while (i < s.length) {

    if (Numbers.includes(s[i])) {
      // Parse and validate numbers
      let token = "";
      while (i < s.length && Numbers.includes(s[i])) {
        token += s[i];
        i += 1;
      }
      let literal = parseNumber(token);
      tokens.push(literal);

    } else if (Letters.includes(s[i])) {
      // Parse names
      let token = "";
      while (i < s.length && Letters.includes(s[i])) {
        token += s[i];
        i += 1;
      }
      tokens.push(token);

    } else if (Operators.includes(s[i])) {
      // Parse operators
      tokens.push(s[i]);
      i += 1;
    } else {
      throw `${s[i]} is not a valid token`;
    }
  }
  return tokens;
}

function parseNumber(token) {
  try {
    literal = parseFloat(token);
  } catch {
    throw `${token} is not a valid token`
  }
  if (literal % 1 === 0) {
    literal = parseInt(literal);
  }
  return literal;
}

