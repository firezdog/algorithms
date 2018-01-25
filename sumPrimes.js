//Function sumPrime(num) returns the sum of all primes up to and including that number.

function sumPrime(num) {
  var primes = getPrimes(num);
  return primes.reduce(getSum);
}

function getPrimes(num) {
  var primes = [];
  for (var i=2; i<=num; i++) {
    var prime = 1;
    for (var j=2; j<i; j++) {
      if (i%j==0) {
        prime = 0;
        break;
      }
    }
    if (prime==1) {
      primes.push(i);
    }
  }
  return primes;
}

function getSum(total, next) {
  return total + next;
}
