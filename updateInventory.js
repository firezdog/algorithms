function updateInventory(arr1, arr2) {
  // All inventory must be accounted for or you're fired!
  arr1 = arr2.reduce(function(init, current) {
    found = false;
    for (var i=0; i<init.length; i++) {
      if (init[i][1] === current[1]) {
        init[i][0] += current[0];
        found = true;
      }
    }
    if (found === false) {
      init.push(current);
    }
    return init;
  },arr1);
  return arr1.sort(function(a,b) {
    if (a[1]>b[1]) {
      return 1;
    }
    else if (a[1] === b[1]) {
      return 0;
    }
    else {
      return -1;
    }
  });
}
