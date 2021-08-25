function iqTest(numbers){
  let arr = numbers.split(' ').map(n => +n);
  if (arr.length < 3) return 1;
  for (let i = 1; i < arr.length; i++){
    let sum = arr[i-1] + arr[i];
    if (sum % 2 === 0) continue;
    let diff = arr.slice(i-2)[0];
    if ((arr[i-1] + diff) % 2 === 1) return i;
    if ((arr[i] + diff) % 2 === 1) return i+1;
  }
  return null;
}