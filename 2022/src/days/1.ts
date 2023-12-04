const getTotals = (input: string) => {
  const elfInventories = input.split("\n\n").map((inv) =>
    inv
      .split("\n")
      .filter(Boolean)
      .map((i) => Number.parseInt(i))
  );

  return elfInventories.map((ei) => {
    return ei.reduce((partialSum, a) => partialSum + a, 0);
  });
};

export const part1 = (input: string) => {
  const elfTotals = getTotals(input);

  return Math.max(...elfTotals);
};

export const part2 = (input: string) => {
  const elfTotals = getTotals(input);

  const topThree = elfTotals.sort((a, b) => b - a).slice(0, 3);
  return topThree.reduce((partialSum, a) => partialSum + a, 0);
};
