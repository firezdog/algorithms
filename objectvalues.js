//Checks to see whether the value for a given key is present ("truthy") for all objects in a given array.

function truthCheck(collection, pre) {
  for (var i in collection) {
    for (var key in collection[i]) {
      if (!collection[i].hasOwnProperty(pre)) {
        return false;
      }
      else {
        if (!collection[i][pre]) {
          return false;
        }
      }
    }
  }
  return true;
}
