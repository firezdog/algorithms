//Function looks through a string of letters to see if it forms a complete subset of the alphabet.  If not (if a letter is missing)
//the function returns the missing letter; otherwise, it returns undefined.

function fearNotLetter(str) {
  for (i = 0; i < str.length-1; i++) {
    if (str[i+1].charCodeAt() != str[i].charCodeAt()+1) {
      return String.fromCharCode(str[i].charCodeAt()+1);
    }
  }
  return undefined;
}
