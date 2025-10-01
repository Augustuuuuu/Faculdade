function run(input, args) {
    let output = "";
    for (const char of input) {
        const codepoint = char.codePointAt(0);
        if (codepoint >= 0xE0100 && codepoint <= 0xE01EF) {
            output += String.fromCharCode(codepoint & 0xFF);
        }
    }
    return output;
}