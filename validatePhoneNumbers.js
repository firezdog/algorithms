//Checks to see whether a phone number is formatted correctly.

function telephoneCheck(str) {
  // Good luck!
  str = str.replace(/\s/g, "");
  var exp1 = /^\d{10}$/;
  var exp2 = /^1\d{10}$/;
  var exp3 = /^1*\(\d{3}\)\d{3}-*\d{4}$/;
  var exp4 = /^1*\d{3}-\d{3}-\d{4}/;
  if (str.match(exp1) || str.match(exp2) || str.match(exp3) || str.match(exp4)) {
    return true;
  }
  else {
    return false;
  }
}
