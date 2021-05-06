//Simple function that, given an array and another function, drops entries from the beginning of the array until it finds one that satisfies that function.

function dropElements(arr, func) {
  while (!func(arr[0])) {
    arr.shift();
  }
  return arr;
}
