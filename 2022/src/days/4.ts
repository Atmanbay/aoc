export const part1 = (input: string) => {
  const regex = /\d+/g;
  let sum = 0;
  input
    .split("\n")
    .filter(Boolean)
    .forEach((line) => {
      const [aStart, aEnd, bStart, bEnd] = line
        .match(regex)
        .map((val) => Number.parseInt(val));

      if (
        (aStart <= bStart && aEnd >= bEnd) ||
        (bStart <= aStart && bEnd >= aEnd)
      ) {
        sum++;
      }
    });

  return sum;
};

export const part2 = (input: string) => {
  const regex = /\d+/g;
  let sum = 0;
  input
    .split("\n")
    .filter(Boolean)
    .forEach((line) => {
      const [aStart, aEnd, bStart, bEnd] = line
        .match(regex)
        .map((val) => Number.parseInt(val));

      if (aStart <= bEnd && aEnd >= bStart) {
        sum++;
      }
    });

  return sum;
};
