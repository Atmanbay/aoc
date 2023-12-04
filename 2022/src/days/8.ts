export const part1 = (input: string) => {
  const heights = input
    .split("\n")
    .filter(Boolean)
    .map((line) => line.split("").map((val) => Number.parseInt(val)));

  let count = 0;
  for (let r = 0; r < heights.length; r++) {
    for (let c = 0; c < heights[r].length; c++) {
      const currentHeight = heights[r][c];
      if (
        heights.slice(0, r).every((row) => row[c] < currentHeight) ||
        heights.slice(r + 1).every((row) => row[c] < currentHeight) ||
        heights[r].slice(0, c).every((val) => val < currentHeight) ||
        heights[r].slice(c + 1).every((val) => val < currentHeight)
      ) {
        count++;
      }
    }
  }

  return count;
};

const calculateScenicScore = (currentHeight: number, line: number[]) => {
  for (let i = 0; i < line.length; i++) {
    if (line[i] >= currentHeight) {
      return i + 1;
    }
  }

  return line.length;
};

export const part2 = (input: string) => {
  const heights = input
    .split("\n")
    .filter(Boolean)
    .map((line) => line.split("").map((val) => Number.parseInt(val)));

  let maxScore = 0;
  for (let r = 0; r < heights.length; r++) {
    for (let c = 0; c < heights[r].length; c++) {
      const currentHeight = heights[r][c];
      const west = calculateScenicScore(
        currentHeight,
        heights
          .slice(0, r)
          .map((row) => row[c])
          .reverse()
      );
      const east = calculateScenicScore(
        currentHeight,
        heights.slice(r + 1).map((row) => row[c])
      );
      const north = calculateScenicScore(
        currentHeight,
        heights[r].slice(0, c).reverse()
      );
      const south = calculateScenicScore(
        currentHeight,
        heights[r].slice(c + 1)
      );

      let score = west * east * north * south;
      if (score > maxScore) {
        maxScore = score;
      }
    }
  }

  return maxScore;
};
