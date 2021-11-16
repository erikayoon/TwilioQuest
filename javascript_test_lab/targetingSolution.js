class TargetingSolution {
    constructor(coords) {
        this.x = coords['x'];
        this.y = coords['y'];
        this.z = coords['z'];
    }
    target() {
        return `(${this.x}, ${this.y}, ${this.z})`;
    }
}

/* TEST CASE
const m = new TargetingSolution({
    x: 10,
    y: 15,
    z: 900,
  });
  
  console.log(m.target()); // would print "(10, 15, 900)"
  */