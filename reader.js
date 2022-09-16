const lexer = require('./lexer');
const TokenBuffer = require('./buffer');

function reader(s) {
  return new TokenBuffer(lexer(s));
}

