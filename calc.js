const read = require('./reader');
const readlineSync = require('readline-sync');

function repl() {
  while (true) {
    try {
      console.log(read(readlineSync.question("> ")).eval());
    } catch (e) {
        console.log(e);
    }
  }
}

if (require.main === module) {
  repl();
}
