type Monkey = {
  items: number[];
  itemsInspected: number;
  operation: (old: number) => number;
  test: (value: number) => boolean;
  ifTrue: number;
  ifFalse: number;
};

export const part1 = (input: string) => {
  // hehe
  const regex =
    /Monkey\s(\d+):\s+Starting\sitems:\s((\d+,?\s?)+)\s{3}Operation:\snew\s=\sold\s(.)\s(\w+)\s{3}Test:\sdivisible\sby\s(\d+)\s{5}If\strue:\sthrow\sto\smonkey\s(\d+)\s{5}If\sfalse:\sthrow\sto\smonkey\s(\d+)/g;

  const matches = input.matchAll(regex);
  const monkeys = [...matches].map((match) => {
    const items = match[2].split(", ").map((val) => Number.parseInt(val));

    let operation: (old: number) => number;
    const value = match[5];
    if (value.match(/\d+/)) {
      if (match[4] === "+") {
        operation = (old: number) => old + Number.parseInt(value);
      } else {
        operation = (old: number) => old * Number.parseInt(value);
      }
    } else {
      if (match[4] === "+") {
        operation = (old: number) => old + old;
      } else {
        operation = (old: number) => old * old;
      }
    }

    let test = (old: number) => old % Number.parseInt(match[6]) === 0;
    let ifTrue = Number.parseInt(match[7]);
    let ifFalse = Number.parseInt(match[8]);

    return {
      items,
      itemsInspected: 0,
      operation,
      test,
      ifTrue,
      ifFalse,
    } as Monkey;
  });
  const roundCount = 20;

  for (let r = 0; r < roundCount; r++) {
    monkeys.forEach((monkey) => {
      const items = monkey.items;
      monkey.items = [];
      items.forEach((item) => {
        monkey.itemsInspected++;
        let newValue = Math.floor(monkey.operation(item) / 3);
        if (monkey.test(newValue)) {
          monkeys[monkey.ifTrue].items.push(newValue);
        } else {
          monkeys[monkey.ifFalse].items.push(newValue);
        }
      });
    });
  }

  let topTwo = monkeys
    .sort((a, b) => b.itemsInspected - a.itemsInspected)
    .slice(0, 2);

  return topTwo[0].itemsInspected * topTwo[1].itemsInspected;
};

export const part2 = (input: string) => {
  // hehe
  const regex =
    /Monkey\s(\d+):\s+Starting\sitems:\s((\d+,?\s?)+)\s{3}Operation:\snew\s=\sold\s(.)\s(\w+)\s{3}Test:\sdivisible\sby\s(\d+)\s{5}If\strue:\sthrow\sto\smonkey\s(\d+)\s{5}If\sfalse:\sthrow\sto\smonkey\s(\d+)/g;

  let modulo = 1;
  const matches = input.matchAll(regex);
  const monkeys = [...matches].map((match) => {
    const items = match[2].split(", ").map((val) => Number.parseInt(val));

    let operation: (old: number) => number;
    const value = match[5];
    if (value.match(/\d+/)) {
      if (match[4] === "+") {
        operation = (old: number) => old + Number.parseInt(value);
      } else {
        operation = (old: number) => old * Number.parseInt(value);
      }
    } else {
      if (match[4] === "+") {
        operation = (old: number) => old + old;
      } else {
        operation = (old: number) => old * old;
      }
    }

    modulo = modulo * Number.parseInt(match[6]);
    let test = (old: number) => old % Number.parseInt(match[6]) === 0;
    let ifTrue = Number.parseInt(match[7]);
    let ifFalse = Number.parseInt(match[8]);

    return {
      items,
      itemsInspected: 0,
      operation,
      test,
      ifTrue,
      ifFalse,
    } as Monkey;
  });
  const roundCount = 10000;

  for (let r = 1; r <= roundCount; r++) {
    monkeys.forEach((monkey) => {
      const items = monkey.items;
      monkey.items = [];
      items.forEach((item) => {
        monkey.itemsInspected++;
        let newValue = monkey.operation(item) % modulo;
        if (monkey.test(newValue)) {
          monkeys[monkey.ifTrue].items.push(newValue);
        } else {
          monkeys[monkey.ifFalse].items.push(newValue);
        }
      });
    });
  }

  let topTwo = monkeys
    .sort((a, b) => b.itemsInspected - a.itemsInspected)
    .slice(0, 2);

  return topTwo[0].itemsInspected * topTwo[1].itemsInspected;
};
