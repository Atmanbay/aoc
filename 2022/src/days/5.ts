export const part1 = (input: string) => {
  const split = input.split("\n\n").filter(Boolean);
  const state: string[][] = [[], [], [], [], [], [], [], [], []];

  split[0]
    .split("\n")
    .reverse()
    .slice(1)
    .forEach((line) => {
      const cells = line.match(/(\s{4})|(\[\w\])/g);
      cells.forEach((cell, index) => {
        const letter = cell.match(/\w/);
        if (letter) {
          state[index].push(letter[0]);
        }
      });
    });

  const regex = /move (\d+) from (\d+) to (\d+)/g;
  const moves = [...split[1].matchAll(regex)].map((match) => {
    return {
      count: Number.parseInt(match[1]),
      from: Number.parseInt(match[2]) - 1,
      to: Number.parseInt(match[3]) - 1,
    };
  });

  moves.forEach((move) => {
    for (let i = 0; i < move.count; i++) {
      const crate = state[move.from].pop();
      state[move.to].push(crate);
    }
  });

  let message = "";
  state.forEach((col) => (message += col.pop()));
  return message;
};

export const part2 = (input: string) => {
  const split = input.split("\n\n").filter(Boolean);
  const state: string[][] = [[], [], [], [], [], [], [], [], []];

  split[0]
    .split("\n")
    .reverse()
    .slice(1)
    .forEach((line) => {
      const cells = line.match(/(\s{4})|(\[\w\])/g);
      cells.forEach((cell, index) => {
        const letter = cell.match(/\w/);
        if (letter) {
          state[index].push(letter[0]);
        }
      });
    });

  const regex = /move (\d+) from (\d+) to (\d+)/g;
  const moves = [...split[1].matchAll(regex)].map((match) => {
    return {
      count: Number.parseInt(match[1]),
      from: Number.parseInt(match[2]) - 1,
      to: Number.parseInt(match[3]) - 1,
    };
  });

  moves.forEach((move) => {
    const moving = state[move.from].splice(
      state[move.from].length - move.count
    );
    state[move.to].push(...moving);
  });

  let message = "";
  state.forEach((col) => (message += col.pop()));
  return message;
};
