function squareDigits(num){
  res = '';
  for (c of num.toString())
    res += String(c**2);
  return Number(res);
}