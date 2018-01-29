//Given a binary representation of a unicode string, this function translates that string back into letters.

function binaryAgent(str) {
  var binaryArray = str.split(" ");
  var unicodeArray = [];
  var charArray = [];
  binaryArray.forEach(function(element) {
    unicodeArray.push(convertBinary(element));
  });
  unicodeArray.forEach(function(element) {
    charArray.push(String.fromCharCode(element));
  });
  return charArray.join("");
}

function convertBinary(str) {
   var sum = 0;
  for (var i = str.length -1; i >= 0; i--) {
    var j = str.length - i - 1;
    sum += str[i]*Math.pow(2,j);
    console.log(sum);
  }
  return sum;
}
