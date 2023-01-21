export default function is_correct_Sentence(str) {
    // Calculate the length of the string.
    var len = str.length;

    // Check that the first character lies in [A-Z].
    // Otherwise return false.
    if (
    str[0].charCodeAt(0) < "A".charCodeAt(0) ||
    str[0].charCodeAt(0) > "Z".charCodeAt(0)
    )
    return false;

    // If the last character is not a full stop(.)
    // no need to check further.
    // if (str[len - 1] !== ".") return false;

    // Maintain 2 states. Previous and current state
    // based on which vertex state you are.
    // Initialise both with 0 = start state.
    var prev_state = 0,
    curr_state = 0;

    // Keep the index to the next character in the string.
    var index = 1;

    // Loop to go over the string.
    while (index <= str.length) {
    // Set states according to the input characters
    // in the string and the rule defined in the description.
    // If current character is [A-Z]. Set current state as 0.
    if (
        str[index].charCodeAt(0) >= "A".charCodeAt(0) &&
        str[index].charCodeAt(0) <= "Z".charCodeAt(0)
    )
        curr_state = 0;
    // If current character is a space.
    // Set current state as 1.
    else if (str[index] === " ") curr_state = 1;
    // If current character is [a-z].
    // Set current state as 2.
    else if (
        str[index].charCodeAt(0) >= "a".charCodeAt(0) &&
        str[index].charCodeAt(0) <= "z".charCodeAt(0)
    )
        curr_state = 2;
    // If current state is a dot(.).
    // Set current state as 3.
    else if (str[index] === "." || str[index] === "?" || str[index] === "!") curr_state = 3;

    // Validates all current state with previous state
    // for the rules in the description of the problem.
    if (prev_state === curr_state && curr_state !== 2) return false;

    if (prev_state === 2 && curr_state === 0) return false;

    // If we have reached last state and previous state
    // is not 1, then check next character. If next character
    // is '\0', then return true, else false
    if (curr_state === 3 && prev_state !== 1)
        return index + 1 == str.length;

    index++;

    // Set previous state as current state
    // before going over to the next character.
    prev_state = curr_state;
    }
    return false;
}
