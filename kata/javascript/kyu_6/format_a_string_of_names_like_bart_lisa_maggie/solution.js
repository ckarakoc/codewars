function list(names){
  return names.map(p => p.name).join(', ').replace(/,(?=[^,]*$)/, ' &'); // (?= ...) === look-ahead
}