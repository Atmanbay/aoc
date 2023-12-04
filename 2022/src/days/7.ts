type Directory = {
  name: string;
  size: number;
  subdirectories: Directory[];
  parentDirectory: Directory;
};

const getAllDirectories = (input: string) => {
  const regex = /(.*?)\s(.*?)(?:\s(\S+))?\n/g;
  const matches = input.matchAll(regex);

  let rootDirectory: Directory;
  let currentDirectory: Directory;
  [...matches].forEach((line) => {
    if (line[2] === "cd") {
      if (line[3] === "/") {
        rootDirectory = {
          name: line[3],
          size: 0,
          subdirectories: [],
          parentDirectory: null,
        };
        currentDirectory = rootDirectory;
      } else if (line[3] === "..") {
        currentDirectory = currentDirectory.parentDirectory;
      } else {
        currentDirectory = currentDirectory.subdirectories.find(
          (cd) => cd.name === line[3]
        );
      }
    } else if (line[1] === "dir") {
      currentDirectory.subdirectories.push({
        name: line[2],
        size: 0,
        subdirectories: [],
        parentDirectory: currentDirectory,
      });
    } else if (line[2] !== "ls") {
      currentDirectory.size += Number.parseInt(line[1]);
    }
  });

  return rootDirectory;
};

const getDirectorySize = (
  directory: Directory,
  callback?: (size: number) => void
) => {
  let size = directory.size;
  directory.subdirectories.forEach(
    (sb) => (size += getDirectorySize(sb, callback))
  );

  if (callback) {
    callback(size);
  }

  directory.size = size;
  return size;
};

export const part1 = (input: string) => {
  let totalSize = 0;
  let callback = (size: number) => {
    if (size <= 100000) {
      totalSize += size;
    }
  };

  const rootDirectory = getAllDirectories(input);
  getDirectorySize(rootDirectory, callback);
  return totalSize;
};

export const part2 = (input: string) => {
  let directorySizes: number[] = [];
  let callback = (size: number) => {
    directorySizes.push(size);
  };

  const rootDirectory = getAllDirectories(input);
  getDirectorySize(rootDirectory, callback);

  const totalDiskSize = 70000000;
  const minUnusedSpace = 30000000;
  const remainingSpace = totalDiskSize - rootDirectory.size;
  const minNeededToFree = minUnusedSpace - remainingSpace;

  directorySizes = directorySizes.sort((a, b) => a - b);
  for (let i = 0; i < directorySizes.length; i++) {
    if (directorySizes[i] >= minNeededToFree) {
      return directorySizes[i];
    }
  }
};
