//Calculate the symmetric difference of two or more arrays.

function sym(args) {
  var result = args;
  for (i=1; i<arguments.length; i++) {
    result = diff(result, arguments[i]);
  }
  return process(result);
}

function process(arr) {
  var newarr = [];
  arr.reduce(function(acc, value) {
    if (newarr.length === 0) {
      newarr.push(acc);
    }
    var result = true;
    for (var i=0; i<newarr.length; i++) {
      if (newarr[i] === value) {
        result = false;
        break;
      }
    }
    if (result) {
      newarr.push(value);
    }
  });
  return newarr;
}

function diff(arr1, arr2) {
  var result1 = check(arr1,arr2);
  var result2 = check(arr2,arr1);
  return result1.concat(result2);
}

function check(arr1, arr2) {
  var result = [];
  for (var i=0; i<arr1.length; i++) {
    if (arr2.reduce(function(test, value) {
      if(arr1[i] === value) {
        test = false;
      }  
      return test;
    },true)) {
      result.push(arr1[i]);
    }
  }
  return result;
}
