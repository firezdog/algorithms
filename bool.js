//Function that separates Boolean and non-Boolean objects.  IMHO kind of silly -- but the challenge drives home the point that "==" is
//not equal to "===", since 1==true but 1 !=== true.

function booWho(bool) {
  if (bool === true || bool === false) {
    return true;
  }
  else {
    return false;
  }
}
