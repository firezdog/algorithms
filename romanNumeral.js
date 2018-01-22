//Function to convert a number to a roman numeral -- works into the 5000 range.

function convertToRoman(num) {
  
  var ones = num%10;
  var onesaf = ones%10%5;
  var onesf = (ones-ones%5)/5;
  var tens = (num%100-num%10)/10;
  var tensaf = tens%10%5;
  var tensf = (tens-tens%5)/5;
  var hundreds = (num%1000-num%100)/100;
  var hundredsaf = hundreds%10%5;
  var hundredsf = (hundreds-hundreds%5)/5;
  var thousands = (num%10000-num%1000)/1000;
  var thousandsaf = thousands%10%5;
  var thousandsf = (thousands-thousands%5)/5;
  
  romone=[];
  romfive=[];
  romten=[];
  romtenfive=[];
  romhun=[];
  romhunfive=[];
  romthou=[];
  
  for (let i=0; i<onesaf; i++){
    romone.push("I");
  }
  romone = romone.join("");  
  if (onesf == 1) {
    romfive.push("V");
  }  
  if (ones == 4 && onesf == 0) {
    romone = ["IV"];
    romfive = [];
  }
  if (ones == 9) {
    romone = ["IX"];
    romfive = [];
  }
  
  for (let i=0; i<tensaf; i++){
    romten.push("X");
  }
  romten = romten.join("");
  if (tensf == 1) {
    romtenfive.push("L");
  }
  if (tens == 4 && tensf == 0) {
    romten = ["XL"];
    romtenfive = [];
  }
  if (tens == 9) {
    romten = ["XC"];
    romtenfive = [];
  }

  
  for (let i=0; i<hundredsaf; i++){
    romhun.push("C");
  }
  romhun = romhun.join("");
  if (hundredsf == 1) {
    romhunfive.push("D");
  }
  if (hundreds == 4 && hundredsf == 0) {
    romhun = ["CD"];
    romhunfive = [];
  }
  if (hundreds == 9) {
    romhun = ["CM"];
    romhunfive = [];
  }

  
  for (let i=0; i<thousandsaf; i++){
    romthou.push("M");
  }
  romthou = romthou.join("");
  
  return romthou + romhunfive + romhun + romtenfive + romten + romfive + romone;

  
}
