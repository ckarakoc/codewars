function openOrSenior(data){
  return data.map(info => info[0] >= 55 && info[1] > 7 ? 'Senior' : 'Open');
}