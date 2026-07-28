const fs = require("fs");

const arguments = process.argv;
const filePaths = arguments.slice(2);

const index = arguments[1].lastIndexOf("/");
const currentWorkingDirectory = arguments[1].slice(0, index + 1);

let flag = filePaths[0];
if (flag.charAt(0) == "-") {
  flag = filePaths.shift();
}

function splitFile(fileName) {
  const filePath = currentWorkingDirectory + fileName;
  const text = fs.readFileSync(filePath, "utf8").trimEnd();
  return text.split("\n");
}

function printFile(lines) {
  lines.forEach((line) => {
    console.log(line);
  });
}

function executeFlag(lines) {
  if (flag === "-n") {
    return lines.map((line, index) => `${String(index + 1).padStart(6, " ")} ${line}`);
  } else if (flag === "-b") {
    let lineNumber = 1;
    return lines.map((line) => {
      if (line === "") {
        return `${line}`;
      }
      return `${String(lineNumber++).padStart(6, " ")} ${line}`;
    });
  } else {
    return lines;
  }
}

filePaths.forEach((filePath) => {
  let lines = splitFile(filePath);
  lines = executeFlag(lines);
  printFile(lines);
});
