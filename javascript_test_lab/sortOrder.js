const firstArg = process.argv[2].toLowerCase();
const secondArg = process.argv[3].toLowerCase();

if (firstArg < secondArg) {
    console.log(-1);
} else if (firstArg === secondArg) {
    console.log(0);
} else {
    console.log(1);
}
