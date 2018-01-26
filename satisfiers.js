//Given an array and a predicate, return the first value in the array that satisfies the predicate.

function findElement(arr, func) {
  var pass = arr.filter(func);
  return pass[0];
}
