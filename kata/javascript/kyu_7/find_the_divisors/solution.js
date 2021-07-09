function divisors(integer) {  
  res = [];
  for(i = 2; i <= Math.floor(integer/2); i++)
    if(integer % i === 0)
      res.push(i);
  if (res.length === 0)
    return `${integer} is prime`;
  return res;
};