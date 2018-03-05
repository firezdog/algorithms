//Determines the sum of the indexes of values in array adding up to the arg.  Each index can only be used once...

function pairwise(arr, arg) {
  var sum = 0;
  loop1: for (var i=0; i < arr.length; i++) {
    for (var j=i+1; j < arr.length; j++) {
      loop2: if (arr[i] + arr[j] === arg) {
         sum += i + j;
         arr[i] = undefined;
         arr[j] = undefined;
         continue loop1;
      }
    }
  }
  return sum;
}

pairwise([0, 0, 0, 0, 1, 1], 1);
