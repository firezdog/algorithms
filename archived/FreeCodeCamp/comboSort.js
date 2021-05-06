function comboSort(arr, pirate) {
    for (i=0; i < pirate.length; i++) {
        console.log(i);
        for (j=0; j < arr.length; j++) {
            if (pirate[i] < arr[j]) {
                arr.splice(j,0,pirate[i]);
                break;
            }
        }
    }
    return arr;
}

console.log(comboSort([2,4,6,8,10],[1,3,5,7,9]));