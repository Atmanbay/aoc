const part1Dict = {
  "A X": 4,
  "A Y": 8,
  "A Z": 3,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 7,
  "C Y": 2,
  "C Z": 6,
};

export const part1 = (input: string) => {
  return input
    .split("\n")
    .filter(Boolean)
    .map((line) => part1Dict[line])
    .reduce((partialSum, current) => partialSum + current, 0);
};

const part2Dict = {
  "A X": 3,
  "A Y": 4,
  "A Z": 8,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 2,
  "C Y": 6,
  "C Z": 7,
};

export const part2 = (input: string) => {
  return input
    .split("\n")
    .filter(Boolean)
    .map((line) => part2Dict[line])
    .reduce((partialSum, current) => partialSum + current, 0);
};
