function highAndLow($numbers) {
  $numbers_arr = explode(" ", $numbers);
  return max($numbers_arr) . " " . min($numbers_arr);
}