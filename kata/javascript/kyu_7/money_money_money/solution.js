function calculateYears(principal, interest, tax, desired) {
  for (years = 0;principal < desired; years++)
    principal += principal * interest * (1-tax);
  return years;
}