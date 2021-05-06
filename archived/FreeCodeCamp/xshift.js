function xshift(x, arr) {
    len = arr.length - 1;
    while (x>0) {
        temp = arr[len];
        for (var i=len; i>0; i--) {
            arr[i] = arr[i-1];
        }
        arr[0]=temp;
        x--;
    }
    console.log(arr);
}