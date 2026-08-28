const fs = require("fs");
const { allowedNodeEnvironmentFlags } = require("process");

const flagHandlers = {
  1: Flag1,
  a: Flaga,
};

let printInList = false;
let showAll = false;

ls(process.argv);

// ----------

function ls(args) {
  const userArgs = getUserArgs(args);
  const currentWorkingDirectory = getCurrentWorkingDirectory(args);
  const fsItems = checkArgsLength(getFsItems(userArgs));

  executeFlags(getFlags(userArgs));

  const dirArgs = getDirArgs(fsItems, currentWorkingDirectory);
  const fileArgs = getFileArgs(fsItems, currentWorkingDirectory);

  print(populateOutput(fsItems, dirArgs, fileArgs, currentWorkingDirectory));
}

function getUserArgs(args) {
  return args.slice(2);
}

function getFsItems(userArgs) {
  return userArgs.filter((arg) => !arg.startsWith("-"));
}

function getCurrentWorkingDirectory(args) {
  const index = args[1].lastIndexOf("/");
  return args[1].slice(0, index);
}

function getFlags(userArgs) {
  return userArgs
    .filter((arg) => arg.startsWith("-"))
    .map((arg) => arg.slice(1))
    .join("");
}

function executeFlags(flags) {
  for (const flag of flags) {
    if (flagHandlers[flag]) flagHandlers[flag]();
    else invalidFlagError();
  }
}

function invalidFlagError() {
  console.error(
    `ls: invalid option -- ${flag}\nusage: ls [-@ABCFGHILOPRSTUWXabcdefghiklmnopqrstuvwxy1%,] [--color=when] [-D format] [file ...]`,
  );
  process.exit(1);
}

function Flag1() {
  printInList = true;
}

function Flaga() {
  showAll = true;
}

function checkArgsLength(fsItems) {
  if (fsItems.length == 0) fsItems.push(".");
  return fsItems;
}

function getDirArgs(fsItems, currentWorkingDirectory) {
  return fsItems.filter((p) => fs.statSync(currentWorkingDirectory + "/" + p).isDirectory());
}

function getFileArgs(fsItems, currentWorkingDirectory) {
  const fileArgs = fsItems.filter((p) => !fs.statSync(currentWorkingDirectory + "/" + p).isDirectory());
  if (showAll == false) removeDotFiles(fileArgs);
  return fileArgs;
}

function populateOutput(fsItems, dirArgs, fileArgs, currentWorkingDirectory) {
  let outputString = "";
  if (fsItems.length == 1) {
    fileArgs.forEach((file) => {
      outputString += file + " ";
    });
    dirArgs.forEach((dir) => {
      outputString += dirOutput(dir, currentWorkingDirectory);
    });
  } else {
    fileArgs.forEach((file) => {
      outputString += file + "\t";
    });
    dirArgs.forEach((dir) => {
      outputString += "\n\n" + dir + ":\n" + dirOutput(dir, currentWorkingDirectory);
    });
  }
  return outputString;
}

function dirOutput(dir, currentWorkingDirectory) {
  let contents = fs.readdirSync(currentWorkingDirectory + "/" + dir);
  let outputStr = "";
  if (showAll) outputStr += ".\t..\t";
  else {
    for (let i = contents.length - 1; i >= 0; i--) {
      contents = removeDotFiles(contents);
    }
  }
  contents.forEach((item) => {
    outputStr += item + "\t";
  });
  return outputStr;
}

function removeDotFiles(fileList) {
  for (let i = fileList.length - 1; i >= 0; i--) {
    if (fileList[i][0] == ".") fileList.splice(i, 1);
  }
  return fileList;
}

function print(outputString) {
  let output = outputString;
  if (printInList) output = makeList(output);
  console.log(output.trimEnd());
}

function makeList(outputString) {
  return outputString.replaceAll("\t", "\n").replaceAll("\n\n", "\n");
}
