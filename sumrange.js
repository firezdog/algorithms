function sumAll(arr) {
  var count = 0;
  var min = arr.reduce(function(a,b) {
    return Math.min(a,b);
  });
  var max = arr.reduce(function(a,b){
    return Math.max(a,b);
  });
  for (i=min; i <= max; i++){
    count += i;
  }
  return count;
}
