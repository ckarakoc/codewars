function tickets(peopleInLine) {
  let change = { 25: 0, 50:0, 100:0 }
  for (const m of peopleInLine) {
    change[m]++;
    let count = m;
    while (count > 50 && change[50]) {
      count -= 50;
      change[50]--;
    }
    while (count > 25 && change[25]) {
      count -= 25;
      change[25]--;
    }
    if (count !== 25) return "NO";
  }
  return "YES";
}