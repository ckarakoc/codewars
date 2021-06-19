function highAndLow(numbers){
  // Beware: Math.max(...[]) === -Infinity (Javascript (╯°□°）╯︵ ┻━┻)
  return Math.max(...numbers.split(' ').map(x=>+x)) + " " + Math.min(...numbers.split(' ').map(x=>+x));
}