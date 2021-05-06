//Given input of one or two variables, either (a) adds the two variables together or (b) creates a function that adds the given variable to its argument. Returns undefined if either variable is not a number.

function addTogether(a, b) { 
  if (arguments.length === 1) {
      if (typeof a === "number") {
        x = a;
        return function(y) {
          if (typeof y === 'number') {
            return x + y;
          }
          else {
            return undefined;
          }
        };
      }
    }
 if (arguments.length === 2) {
      if (typeof a === 'number' && typeof b === 'number') {
        return arguments[0] + arguments[1]; 
      }
      else { return undefined; }
    }
}
