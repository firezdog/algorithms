//Function to translate a string into pig-latin:
//If the string begins with a consonant-cluster, the consonant-cluster is moved to the end and supplemented with "ay".
//If the string begins with a vowel, it is supplemented with "way".
//"eight" should become "eightway"; "clone" should become "oneclay".
//etc.

function translatePigLatin(str) {
  var pos = str.search(/[aeiou]/);
  if (pos !== 0) {
    var end = str.slice(0, pos);
    var begin = str.slice(pos, str.length);
    return begin + end + "ay";
  }
  else {
    return str + "way";
  }
}
