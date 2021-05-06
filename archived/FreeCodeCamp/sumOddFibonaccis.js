//Function to return the sum of all odd Fibonacci numbers less than a given number.  The function
//is supposed, first, to create an array of all Fibonacci numbers up to the given number (ideally you would get
//the first Fibonacci greater than the number into the array) and, second, to loop through all elements of the array 
//less than the given number, adding together those that happen to be odd.

function sumFibs(num) {
    var fibs = [1,1];
    for (var i = 1; fibs[i] <num; i++){
        fibs.push(fibs[i-1]+fibs[i]);    
    }
    var sum = 0;
    for (i = 0; fibs[i] <= num; i++) {
      if (fibs[i] %2 == 1) {
        sum += fibs[i];
    }
  }
  return sum;
}
