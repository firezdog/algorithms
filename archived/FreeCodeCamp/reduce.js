function reduce(arr, callback, initial) {
    if (initial) {
        var i = 0;
        var accumulator = initial;
    } else {
        var i = 1;
        var accumulator = arr[0]
    }
    while (i < arr.length) {
        accumulator = callback(accumulator, arr[i], i, arr);
        i++;
    }
    return accumulator;
}

var arr = [[1,2],[3,4,5]];

function callback(accumulator, item) {
    return accumulator.concat(item);
}

console.log(reduce(arr, callback));
