//Flattens an array -- that is, pulls out all elements from the array (and the arrays in the array and the arrays in the arrays in the array...) recursively. Originally went a layer too deep before getting into the recursion.

function steamrollArray(arr) {
  newarr = [];
  arr.forEach(function(element) {
    if (!Array.isArray(element)) {
      newarr.push(element);
    }
    else {
      newarr = newarr.concat(steamrollArray(element));
    }
  });
  return newarr;
}
