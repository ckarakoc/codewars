function duplicateCount(text){
  let counter = {}
  Array.from(text.toLowerCase()).forEach(c => counter[c] ? counter[c] += 1 : counter[c] = 1);
  return Object.values(counter).filter(a => a > 1).length;
}