var life_status = process.argv[2];

if (life_status == 0) {
    console.log('alive');
} else if (life_status == 1) {
    console.log('flowering');
} else if (life_status == 2) {
    console.log('shedding');
} else {
    console.log('other');
}