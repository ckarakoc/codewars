function chromosomeCheck(sperm) {
  if (sperm.endsWith('Y'))
    return "Congratulations! You're going to have a son.";
  return "Congratulations! You're going to have a daughter.";
}