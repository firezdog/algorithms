//Find the least common multiple of all elements in a range.

function smallestCommons(arr) {
  arr = arr.sort();
  var max = maxMult(arr);
  for (var i = arr[0]; i<max; i++){
    var passed = true;
    for (var j=arr[0]; j<=arr[1]; j++) {
      if (i%j !== 0) {
        passed = false;
        break;
      }
  }
  if (passed == true) {
    return i;
  }
}
}

function maxMult(arr) {
  var max = arr[0];
  for (var i= arr[0]+1; i <= arr[1]; i++){
    max *= i;
  }
  return max;
}
