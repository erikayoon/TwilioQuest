var plant_status = process.argv[2];
var plant_dryness = process.argv[3];

if (plant_status == 0 && plant_dryness > 10) {
    console.log('WATER');
}