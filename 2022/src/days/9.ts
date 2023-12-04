export const part1 = (input: string) => {
  const moves = input
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      const split = line.split(" ");
      return {
        direction: split[0],
        steps: Number.parseInt(split[1]),
      } as const;
    });

  const headLocation = { x: 0, y: 0 };
  const tailLocations: { x: number; y: number }[] = [{ x: 0, y: 0 }];

  moves.forEach((move) => {
    const tailLocation = tailLocations[tailLocations.length - 1];
    for (let i = 0; i < move.steps; i++) {
      const lastHeadLocation = { ...headLocation };

      switch (move.direction) {
        case "L":
          headLocation.x--;
          break;
        case "U":
          headLocation.y++;
          break;
        case "R":
          headLocation.x++;
          break;
        case "D":
          headLocation.y--;
          break;
      }

      const xDiff = Math.abs(headLocation.x - tailLocation.x);
      const yDiff = Math.abs(headLocation.y - tailLocation.y);

      if (xDiff > 1 || yDiff > 1) {
        tailLocations.push(lastHeadLocation);
      }
    }
  });

  return new Set(tailLocations.map((tl) => `${tl.x},${tl.y}`)).size;
};

type Location = {
  x: number;
  y: number;
};

export const part2 = (input: string) => {
  const moves = input
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      const split = line.split(" ");
      return {
        direction: split[0],
        steps: Number.parseInt(split[1]),
      } as const;
    });

  const knots: Location[] = [
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
    { x: 0, y: 0 },
  ];
  const tail = knots.length - 1;
  const visited: Set<string> = new Set();

  moves.forEach((move) => {
    for (let s = 0; s < move.steps; s++) {
      switch (move.direction) {
        case "L":
          knots[0].x--;
          break;
        case "U":
          knots[0].y++;
          break;
        case "R":
          knots[0].x++;
          break;
        case "D":
          knots[0].y--;
          break;
      }

      for (let i = 1; i < knots.length; i++) {
        if (
          Math.abs(knots[i - 1].x - knots[i].x) > 1 ||
          Math.abs(knots[i - 1].y - knots[i].y) > 1
        ) {
          if (knots[i - 1].x !== knots[i].x) {
            knots[i].x +=
              (knots[i - 1].x - knots[i].x) /
              Math.abs(knots[i - 1].x - knots[i].x);
          }

          if (knots[i - 1].y !== knots[i].y) {
            knots[i].y +=
              (knots[i - 1].y - knots[i].y) /
              Math.abs(knots[i - 1].y - knots[i].y);
          }

          if (i == tail) {
            visited.add(`${knots[i].x},${knots[i].y}`);
          }
        }
      }
    }
  });

  return visited.size;
};
