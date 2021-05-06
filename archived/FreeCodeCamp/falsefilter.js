function falseSort(arr, callback) {
    for (i=arr.length-1; i>=0; i--) {
        if (!callback(arr[i])) {
            let temp = arr[i];
            arr.splice(i,1);
            arr.push(temp);
        }
    }
    return arr;
}

//example callback for test

function isEven(number) {
    if(number % 2 == 0) {
        return true;
    } else {
        return false;
    }
}

console.log(falseSort([1,3,5,2,4,6], isEven));