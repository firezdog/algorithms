//Returns number of permutations of a given string with non-repeating characters.

function permAlone(str) {
    var perms = perm(str);
    for (i=0; i<perms.length; i++) {
        if (perms[i].match(/(.)\1/)) {
            perms.splice(i,1);
            i--;
        }
    }
    return perms.length;
}

//Returns all permutations of a given string using a recursive definition.

function perm(str) {
    var arr = [];
    //Base cases.
    if (str.length === 1) {
        arr.push(str);
    }
    else if (str.length === 2) {
        arr.push(str[0]+str[1], str[1]+str[0]);
    }
    else if (str.length > 2) {
        var character = str[0];
        str = str.slice(1);
        arr = perm(str);
        for (var i=0; i<arr.length; i++) {
            var toChange = arr[i];
            arr.splice(i,1);
            i--;
            for (var j=0; j<=toChange.length; j++) {
                arr.unshift(toChange.substring(0,j) + character + toChange.substring(j));
                i++;
            }
        }
    }
    return arr;
}
