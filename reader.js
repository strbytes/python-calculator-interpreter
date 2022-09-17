const lexer = require('./lexer');
const TokenBuffer = require('./buffer');
const parser = require('./parser')

function reader(s) {
  return parser(new TokenBuffer(lexer(s)));
}

module.exports = reader;
