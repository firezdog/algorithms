//Another rather messy experiment with RegEx. The goal is to take a string representing a sentence or phrase using
//various kinds of word breaks, uncapitalize all words, and replace those breaks with "-". A bit too ad-hoc.

function spinalCase(str) {
  //If the break is '-', a capital letter, or a space, add another break.
  var newstr = str.replace(/(-|[A-Z]|\s)/g, " $&");
  //If the break is an underscore, get rid of it.
  newstr = newstr.replace(/_/g,"");
  //make everything lower-case.
  newstr = newstr.toLowerCase();
  //Get rid of the first space.
  newstr = newstr.replace(/^\s*/,'');
  //Using the spaces we added, split the string into words.
  var arr = newstr.split(/\s+/);
  //Get rid of any extra dashes (for dashes used as word-breaks).
  return arr.join("-").replace(/-+/g,'-').replace(/^-/,'');
}
