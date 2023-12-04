const getSignalStrength = (cycles: number[], index: number) => {
  return cycles[index - 1] * index;
};

export const part1 = (input: string) => {
  const cycles = input
    .split("\n")
    .filter(Boolean)
    .reduce(
      (cycles: number[], current: string) => {
        const command = current.split(" ");
        const lastValue = cycles[cycles.length - 1];
        if (command[0] === "noop") {
          cycles.push(lastValue);
        } else {
          cycles.push(lastValue);
          cycles.push(lastValue + Number.parseInt(command[1]));
        }

        return cycles;
      },
      [1]
    );

  return (
    getSignalStrength(cycles, 20) +
    getSignalStrength(cycles, 60) +
    getSignalStrength(cycles, 100) +
    getSignalStrength(cycles, 140) +
    getSignalStrength(cycles, 180) +
    getSignalStrength(cycles, 220)
  );
};

export const part2 = (input: string) => {
  const cycles = input
    .split("\n")
    .filter(Boolean)
    .reduce(
      (cycles: number[], current: string) => {
        const command = current.split(" ");
        const lastValue = cycles[cycles.length - 1];
        if (command[0] === "noop") {
          cycles.push(lastValue);
        } else {
          cycles.push(lastValue);
          cycles.push(lastValue + Number.parseInt(command[1]));
        }

        return cycles;
      },
      [1]
    );

  const columns = 40;
  const screen: string[][] = [[], [], [], [], [], []];
  cycles.forEach((cycle, index) => {
    // no clue why I have to do this
    if (index === 240) {
      return;
    }

    const row = Math.floor(index / columns);
    const col = index - row * columns;

    if (Math.abs(cycle - col) <= 1) {
      screen[row][col] = "#";
    } else {
      screen[row][col] = ".";
    }
  });

  screen.forEach((line) => {
    console.log(line.join(""));
  });

  return "";
};
