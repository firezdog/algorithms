//Very simple function that converts common punctuation to UTF equivalents. To improve it I would look for a way
//to search and replace in one fell swoop.

function convertHTML(str) {
  str = str.replace(/&/g,"&amp;");
  str = str.replace(/</g, "&lt;");
  str = str.replace(/>/g, "&gt;");
  str = str.replace(/"/g, "&quot;");
  str = str.replace(/'/g, "&apos;");
  return str;
}
