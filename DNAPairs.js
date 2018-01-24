//This function "repairs" an incomplete "string" of DNA.  For instance, if the string is "GCC", each element of the string
//is matched with its DNA pair to produce the array [["G","C"],["C","G"],["C","G"]].

function pairElement(str) {
  var str = str.split("");
  for (const l in str) {
    switch (str[l]) {
      case "A":
        str[l] = ["A","T"];
        break;
      case "T":
        str[l] = ["T", "A"];
        break;
      case "G":
        str[l] = ["G", "C"];
        break;
      case "C":
        str[l] = ["C", "G"];
        break;
    }
  }
  return str;
}
