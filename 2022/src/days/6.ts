export const part1 = (input: string) => {
  const chunkSize = 4;
  for (let i = 0; i < input.length; i++) {
    if (new Set(input.substring(i, i + chunkSize)).size === chunkSize) {
      return i + chunkSize;
    }
  }
};

export const part2 = (input: string) => {
  const chunkSize = 14;
  for (let i = 0; i < input.length; i++) {
    if (new Set(input.substring(i, i + chunkSize)).size === chunkSize) {
      return i + chunkSize;
    }
  }
};
