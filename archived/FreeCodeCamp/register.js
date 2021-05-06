//Returns change for a given amount of cash tendered for a given price based on contents of the "cash register."  Doesn't handle marginal cases where, e.g., you are owed 50 cents but the register has 2 dimes, a nickle, and a quarter (trickier problem). Just goes down from highest to lowest denominations until amount owed is filled. Could be improved with Array.prototype.reduce...

function checkCashRegister(price, cash, cid) {
  var change = [["ONE HUNDRED", 0.00], ["TWENTY", 0.00], ["TEN", 0.00], ["FIVE", 0.00], ["ONE", 0.00], ["QUARTER", 0.00], ["DIME", 0.00], ["NICKEL", 0.00], ["PENNY", 0.00]];
  cash *= 100; //change everything to pennies to avoid rounding problems
  price *= 100;
  var toChange = cash - price;
  var totalInRegister = total(cid);
  // Here is your change, ma'am.
  if (totalInRegister < toChange) {
    return "Insufficient Funds";
  }
  else if (totalInRegister === toChange) {
    return "Closed";
  }
  else {
    while (toChange >= 100*100) {
      if (cid[8][1] > 0) {
        cid[8][1] -= 100;
        change[0][1] += 100;
        toChange -= 100*100;
      }
      else {
        break;
      }
    }
      while (toChange >= 20*100) {
      if (cid[7][1] > 0) {
        cid[7][1] -= 20;
        change[1][1] += 20;
        toChange -= 20*100;
      }
      else {
        break;
      }
      }
      while (toChange >= 10*100) {
      if (cid[6][1] > 0) {
        cid[6][1] -= 10;
        change[2][1] += 10;
        toChange -= 10*100;
      }
      else {
        break;
      }
      }
      while (toChange >= 5*100) {
      if (cid[5][1] > 0) {
        cid[5][1] -= 5;
        change[3][1] += 5;
        toChange -= 5*100;
      }
      else {
        break;
      }
      }
      while (toChange >= 1*100) {
      if (cid[4][1] > 0) {
        cid[4][1] -= 1;
        change[4][1] += 1;
        toChange -= 1*100;
      }
      else {
        break;
      }
      }
      while (toChange >= 25) {
        if (cid[3][1] > 0) {
          cid[3][1] -= 0.25;
          change[5][1] += 0.25;
          toChange -= 25;
        }
        else {
          break;
        }
      }
      while (toChange >= 10) {
        if(cid[2][1] > 0) {
          cid[2][1] -= 0.1;
          change[6][1] += 0.10;
          toChange -= 10;
        }
        else {
          break;
        }
      }
      while (toChange >= 5) {
        if(cid[1][1] > 0) {
          cid[1][1] -= 0.05;
          change[7][1] += 0.05;
          toChange -= 5;
        }
        else {
          break;
        }
      }
        while (toChange >= 1) {
        if(cid[0][1] > 0) {
          cid[0][1] -= 0.01;
          change[8][1] += 0.01;
          toChange -= 1;
        }
        else {
          break;
        }
      }
      if (toChange > 0) {
        return "Insufficient Funds";
      }
  }
  for (var i=0; i<change.length;i++) {
    if (change[i][1] > 0) {
      continue;
    }
    else {
      change.splice(i,1);
      i--;
    }
  }
    return change;
}

function total(arr) {
  var totalValue = 0;
  for (var i = 0; i < arr.length; i++) {
    totalValue += arr[i][1]*100;
  }
  return totalValue; //in pennies to avoid rounding problems
}
