const getPriority = (character: string) => {
  const charCode = character.toLowerCase().charCodeAt(0) - 96;
  if (character === character.toLowerCase()) {
    return charCode;
  } else {
    return charCode + 26;
  }
};

export const part1 = (input: string) => {
  return input
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      const half = Math.ceil(line.length / 2);
      const firstHalf = line.substring(0, half);
      const secondHalf = line.substring(half);
      const match = firstHalf.match(`[${secondHalf}]`);
      return getPriority(match[0]);
    })
    .reduce((partialSum, a) => partialSum + a, 0);
};

export const part2 = (input: string) => {
  let sum = 0;
  const lines = input.split("\n").filter(Boolean);
  for (let i = 0; i < lines.length; i = i + 3) {
    let group = lines.slice(i, i + 3).map((line) => line.split(""));
    let badge = group[0].filter(
      (v) => group[1].includes(v) && group[2].includes(v)
    )[0];

    sum += getPriority(badge);
  }

  return sum;
};
