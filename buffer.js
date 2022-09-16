/**
 * Stores a series of tokens to be used by the parser, and provides a queue-
 * like interface for accessing them.
 */ 
class TokenBuffer {
  #tokens;
  #index = 0;
  
  constructor(tokens) {
    this.#tokens = tokens;
  }
  
  /**
   * Returns the current token in the buffer. Undefined response indicates end 
   * of buffer.
   */
  get current() {
    return this.#tokens[this.#index];
  }

  /**
   * Returns the next token in the buffer. Undefined response indicates end of 
   * buffer.
   */
  get next() {
    return this.#tokens[this.#index + 1];
  }

  /**
   * Returns the next token in the buffer and advances the index. WIll throw
   * an exception if called past the end of the buffer.
   */
  pop() {
    if (this.#index == this.#tokens.length) {
      throw "Reached end of buffer";
    }
    let token = this.current;
    this.#index += 1;
    return token;
  }
}

module.exports = TokenBuffer;

