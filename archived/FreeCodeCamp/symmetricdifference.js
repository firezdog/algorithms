//Calculates the symmetric difference of two arrays -- 
//currently limited: only works if arrays are formatted as sets (no repeating entries.)

function diffArray(arr1, arr2) {
  var newArr = arr1.concat(arr2);
  newArr = newArr.filter(function (value, index, array) {
                var elOut = array.slice(0,index).concat(array.slice(index+1,array.length));
  return elOut.indexOf(value) == -1;
                });
  return newArr;
}
