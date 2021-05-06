//Assume that the function uniteUnique() takes as argument an array of arrays. The function as defined below is supposed to
//collect the elements of the arrays into an array, then remove all duplicates from the array while preserving the order.
//The test as presented by FreeCodeCamp required that the first elements of the array be kept, the latter removed -- which necessitated
//Going through the array in reverse order, as I discovered after repeated trials and (admittedly) random experimentation.
//I am sure there are more efficient and elegant ways of accomplishing this, but this patched-together version does the job for now.

function uniteUnique(arr) {  
  //creates an array that joins the elements of all the arguments -- assumes that the arguments are all arrays.
  var newarr = [];
  for (var i in arguments) {
    arguments[i].forEach(function(element){ 
        newarr.push(element);
    });
  }
  
  //start at the end of the array and count down -- the tests FCC uses prefer that we keep the first value and throw out the later values, so we proceed in this way to ensure the first value "survives".
  for (i=newarr.length; i >= 0; i--) {
    //if everything up to ("slice") the value and ("concat") everything after ("slice") the value still includes ("indexOf") the value...
      if (newarr.slice(0,i).concat(newarr.slice(i+1,newarr.length)).indexOf(newarr[i])>-1) {
        //reform the array from everything up to the value and everything after the value (chop it out).
        newarr = newarr.slice(0,i).concat(newarr.slice(i+1,newarr.length));
      }
  }
  return newarr;
 }
